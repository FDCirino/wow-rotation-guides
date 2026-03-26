#!/usr/bin/env python3
"""
Sync guides from human-readable structure to WowCoach's specId-based structure.

Usage: python sync-to-wowcoach.py <source_guides_dir> <dest_rotation_guides_review_dir>

Example:
  python sync-to-wowcoach.py ./guides /path/to/wowcoach/rotation-guides-review
"""

import yaml
import glob
import os
import shutil
import sys


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    files = sorted(glob.glob(os.path.join(src_dir, '*', '*', '*', '*.yaml')))
    if not files:
        print(f'No guide files found in {src_dir}')
        sys.exit(1)

    copied = 0
    for f in files:
        with open(f) as fh:
            data = yaml.safe_load(fh)

        spec_id = data.get('specId')
        hero_talent = data.get('heroTalent', '').lower().replace(' ', '-').replace("'", '')
        filename = os.path.basename(f)

        if filename == 'guide.yaml':
            # Base spec guide
            dest = os.path.join(dst_dir, str(spec_id), 'guide.yaml')
        else:
            # Hero talent guide
            dest = os.path.join(dst_dir, str(spec_id), hero_talent, 'guide.yaml')

        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(f, dest)
        rel_src = os.path.relpath(f, src_dir)
        rel_dst = os.path.relpath(dest, dst_dir)
        print(f'{rel_src} -> {rel_dst}')
        copied += 1

    print(f'\nSynced {copied} files.')


if __name__ == '__main__':
    main()
