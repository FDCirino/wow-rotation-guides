#!/usr/bin/env python3
"""Validate all rotation guide YAML files."""

import yaml
import glob
import sys
import os

GUIDES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'guides')

REQUIRED_FIELDS = ['specId', 'className', 'specName', 'role', 'patch']
VALID_ROLES = ['DPS', 'Tank', 'Healer']

def validate_file(filepath):
    errors = []
    rel_path = os.path.relpath(filepath, GUIDES_DIR)

    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f'YAML parse error: {e}']

    if not isinstance(data, dict):
        return ['File does not contain a YAML mapping']

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f'Missing required field: {field}')

    if not isinstance(data.get('specId'), int):
        errors.append(f'specId must be an integer, got {type(data.get("specId")).__name__}')

    if data.get('role') and data['role'] not in VALID_ROLES:
        errors.append(f'Invalid role "{data["role"]}", must be one of {VALID_ROLES}')

    # Hero talent guides must have heroTalent field
    filename = os.path.basename(filepath)
    if filename != 'guide.yaml' and 'heroTalent' not in data:
        errors.append(f'Hero talent guide missing heroTalent field')

    # Check maintenanceBuffs structure
    buffs = data.get('maintenanceBuffs')
    if buffs is not None:
        if not isinstance(buffs, list):
            errors.append('maintenanceBuffs must be a list')
        else:
            for i, buff in enumerate(buffs):
                if not isinstance(buff, dict):
                    errors.append(f'maintenanceBuffs[{i}] must be a mapping')
                elif 'spellName' not in buff:
                    errors.append(f'maintenanceBuffs[{i}] missing spellName')

    # Check rotation structure
    rotation = data.get('rotation')
    if rotation is not None:
        if not isinstance(rotation, dict):
            errors.append('rotation must be a mapping')

    # Check cooldowns structure (list for v3, string for v1/v2)
    cooldowns = data.get('cooldowns')
    if cooldowns is not None:
        if not isinstance(cooldowns, (list, str)):
            errors.append('cooldowns must be a list or string')

    # Check for mismatched quotes (common YAML pitfall)
    with open(filepath) as f:
        for i, line in enumerate(f, 1):
            s = line.strip()
            if (s.startswith('- "') and s.endswith("'")) or (s.startswith("- '") and s.endswith('"')):
                errors.append(f'Mismatched quotes at line {i}')

    return errors


def main():
    patterns = [
        os.path.join(GUIDES_DIR, '*', '*', '*', '*.yaml'),
    ]

    files = []
    for pattern in patterns:
        files.extend(sorted(glob.glob(pattern)))

    if not files:
        print(f'No guide files found in {GUIDES_DIR}')
        sys.exit(1)

    ok = 0
    fail = 0

    for f in files:
        rel = os.path.relpath(f, GUIDES_DIR)
        errors = validate_file(f)
        if errors:
            fail += 1
            print(f'FAIL {rel}')
            for e in errors:
                print(f'     {e}')
        else:
            ok += 1
            print(f'OK   {rel}')

    print()
    if fail > 0:
        print(f'VALIDATION FAILED: {fail} file(s) have errors, {ok} passed.')
        sys.exit(1)
    else:
        print(f'All {ok} files passed validation.')


if __name__ == '__main__':
    main()
