# Contributing to WoW Rotation Guides

Thank you for helping improve WowCoach! These guides directly power the AI Coach's rotation advice.

## How to Edit a Guide (No Developer Tools Required)

### Step 1: Find the guide file

Browse the [guides/](guides/12.0.1/) directory or use the table in [README.md](README.md) to find your spec and hero talent.

### Step 2: Click the pencil icon

On the file's GitHub page, click the pencil icon (top right of the file content) to edit in your browser.

If you don't have write access, GitHub will automatically fork the repo for you.

### Step 3: Make your changes

Edit the YAML directly. Keep the formatting consistent:
- Use spaces, not tabs
- Keep numbered lists sequential (1, 2, 3...)
- Wrap long lines in the rotation/concepts sections

### Step 4: Submit your changes

1. Scroll down to "Propose changes"
2. Write a brief description of what you changed and why
3. Click "Propose changes"
4. On the next page, click "Create pull request"

That's it! A maintainer will review your changes and merge them.

## What Makes a Good Contribution

### Do

- Fix incorrect rotation priorities based on reputable sources (Icy Veins, Maxroll, Method, Wowhead)
- Update guides for new patches
- Add missing abilities or talent interactions for the correct hero talent
- Fix wrong cooldown durations
- Improve coaching tips to be more actionable
- Include a link to your source in the PR description

### Don't

- Add abilities from the wrong hero talent tree (e.g., don't put Demolish in a Mountain Thane guide)
- Change metadata fields (`specId`, `className`, `specName`, `heroTalent`)
- Restructure the YAML schema
- Add speculative or unverified information
- Copy large blocks of text from guide websites

## Guide Schema Quick Reference

Every guide has these sections:

| Section | Purpose |
|---------|---------|
| `specId` / `className` / `specName` | Identifies the spec (don't change) |
| `heroTalent` | Which hero talent tree this guide covers |
| `resourceManagement` | How the spec generates and spends resources |
| `maintenanceBuffs` | Buffs to keep active with target uptimes |
| `rotation` | Priority lists for single-target, AoE, and opener |
| `cooldowns` | Major cooldowns with timers and usage tips |
| `concepts` | Key mechanics and interactions to understand |
| `commonMistakes` | What players frequently do wrong |
| `tankingGuide` | (Tanks only) Survival priorities, defensive CDs, resource management |

### Rotation format

Rotations are numbered priority lists. The AI Coach reads these top-to-bottom:

```yaml
rotation:
  singleTarget: |-
    1. Cast Avatar on cooldown.
    2. Cast Demoralizing Shout on cooldown.
    3. Cast Ravager on cooldown.
    ...
```

Mark optional/talented abilities with `(if talented)` so the AI Coach can skip them for players who don't have them:

```yaml
    5. Cast Champion's Spear (if talented).
```

## Questions?

Open an issue on this repo or reach out on the WowCoach Discord.
