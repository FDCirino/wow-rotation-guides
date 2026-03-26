# WoW Rotation Guides

Community-maintained rotation guides for [WowCoach](https://wowcoach.gg) AI Coach. These YAML files power the AI's understanding of how each spec should be played.

## How It Works

When you ask the WowCoach AI Coach about your rotation, it reads the guide for your spec and hero talent to understand priority lists, cooldown usage, common mistakes, and (for tanks) survival priorities. Better guides = better coaching.

## Contributing

**You don't need to be a developer.** If you know WoW class mechanics, you can improve these guides.

1. Find your spec in the [guide directory](#guide-directory) below
2. Click the **Edit** link
3. Make your changes in the browser
4. Submit — GitHub will create a pull request automatically
5. A maintainer reviews and merges

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions with screenshots.

### What to contribute

- Fix incorrect rotation priorities
- Update guides for new patches
- Add missing abilities or mechanics
- Fix wrong cooldown timers or descriptions
- Improve coaching tips
- Add missing hero talent interactions

### What NOT to change

- Don't change `specId`, `className`, or `specName` fields
- Don't restructure the YAML schema
- Don't add abilities from the wrong hero talent tree

## Guide Directory

| Class | Spec | Hero Talents | Edit |
|-------|------|-------------|------|
| Death Knight | Blood | [Deathbringer](guides/12.0.1/death-knight/blood/deathbringer.yaml), [San'layn](guides/12.0.1/death-knight/blood/sanlayn.yaml) | [edit](../../edit/main/guides/12.0.1/death-knight/blood/) |
| Death Knight | Frost | [Deathbringer](guides/12.0.1/death-knight/frost/deathbringer.yaml), [Rider of the Apocalypse](guides/12.0.1/death-knight/frost/rider-of-the-apocalypse.yaml) | [edit](../../edit/main/guides/12.0.1/death-knight/frost/) |
| Death Knight | Unholy | [Rider of the Apocalypse](guides/12.0.1/death-knight/unholy/rider-of-the-apocalypse.yaml), [San'layn](guides/12.0.1/death-knight/unholy/sanlayn.yaml) | [edit](../../edit/main/guides/12.0.1/death-knight/unholy/) |
| Demon Hunter | Havoc | [Aldrachi Reaver](guides/12.0.1/demon-hunter/havoc/aldrachi-reaver.yaml), [Fel-Scarred](guides/12.0.1/demon-hunter/havoc/fel-scarred.yaml) | [edit](../../edit/main/guides/12.0.1/demon-hunter/havoc/) |
| Demon Hunter | Vengeance | [Aldrachi Reaver](guides/12.0.1/demon-hunter/vengeance/aldrachi-reaver.yaml), [Annihilator](guides/12.0.1/demon-hunter/vengeance/annihilator.yaml) | [edit](../../edit/main/guides/12.0.1/demon-hunter/vengeance/) |
| Druid | Balance | [Elune's Chosen](guides/12.0.1/druid/balance/elunes-chosen.yaml), [Keeper of the Grove](guides/12.0.1/druid/balance/keeper-of-the-grove.yaml) | [edit](../../edit/main/guides/12.0.1/druid/balance/) |
| Druid | Feral | [Druid of the Claw](guides/12.0.1/druid/feral/druid-of-the-claw.yaml), [Wildstalker](guides/12.0.1/druid/feral/wildstalker.yaml) | [edit](../../edit/main/guides/12.0.1/druid/feral/) |
| Druid | Guardian | [Druid of the Claw](guides/12.0.1/druid/guardian/druid-of-the-claw.yaml), [Elune's Chosen](guides/12.0.1/druid/guardian/elunes-chosen.yaml) | [edit](../../edit/main/guides/12.0.1/druid/guardian/) |
| Druid | Restoration | [Keeper of the Grove](guides/12.0.1/druid/restoration/keeper-of-the-grove.yaml), [Wildstalker](guides/12.0.1/druid/restoration/wildstalker.yaml) | [edit](../../edit/main/guides/12.0.1/druid/restoration/) |
| Evoker | Augmentation | [Chronowarden](guides/12.0.1/evoker/augmentation/chronowarden.yaml), [Scalecommander](guides/12.0.1/evoker/augmentation/scalecommander.yaml) | [edit](../../edit/main/guides/12.0.1/evoker/augmentation/) |
| Evoker | Devastation | [Flameshaper](guides/12.0.1/evoker/devastation/flameshaper.yaml), [Scalecommander](guides/12.0.1/evoker/devastation/scalecommander.yaml) | [edit](../../edit/main/guides/12.0.1/evoker/devastation/) |
| Evoker | Preservation | [Chronowarden](guides/12.0.1/evoker/preservation/chronowarden.yaml), [Flameshaper](guides/12.0.1/evoker/preservation/flameshaper.yaml) | [edit](../../edit/main/guides/12.0.1/evoker/preservation/) |
| Hunter | Beast Mastery | [Dark Ranger](guides/12.0.1/hunter/beast-mastery/dark-ranger.yaml), [Pack Leader](guides/12.0.1/hunter/beast-mastery/pack-leader.yaml) | [edit](../../edit/main/guides/12.0.1/hunter/beast-mastery/) |
| Hunter | Marksmanship | [Dark Ranger](guides/12.0.1/hunter/marksmanship/dark-ranger.yaml), [Sentinel](guides/12.0.1/hunter/marksmanship/sentinel.yaml) | [edit](../../edit/main/guides/12.0.1/hunter/marksmanship/) |
| Hunter | Survival | [Pack Leader](guides/12.0.1/hunter/survival/pack-leader.yaml), [Sentinel](guides/12.0.1/hunter/survival/sentinel.yaml) | [edit](../../edit/main/guides/12.0.1/hunter/survival/) |
| Mage | Arcane | [Spellslinger](guides/12.0.1/mage/arcane/spellslinger.yaml), [Sunfury](guides/12.0.1/mage/arcane/sunfury.yaml) | [edit](../../edit/main/guides/12.0.1/mage/arcane/) |
| Mage | Fire | [Frostfire](guides/12.0.1/mage/fire/frostfire.yaml), [Sunfury](guides/12.0.1/mage/fire/sunfury.yaml) | [edit](../../edit/main/guides/12.0.1/mage/fire/) |
| Mage | Frost | [Frostfire](guides/12.0.1/mage/frost/frostfire.yaml), [Spellslinger](guides/12.0.1/mage/frost/spellslinger.yaml) | [edit](../../edit/main/guides/12.0.1/mage/frost/) |
| Monk | Brewmaster | [Master of Harmony](guides/12.0.1/monk/brewmaster/master-of-harmony.yaml), [Shado-Pan](guides/12.0.1/monk/brewmaster/shado-pan.yaml) | [edit](../../edit/main/guides/12.0.1/monk/brewmaster/) |
| Monk | Mistweaver | [Conduit of the Celestials](guides/12.0.1/monk/mistweaver/conduit-of-the-celestials.yaml), [Master of Harmony](guides/12.0.1/monk/mistweaver/master-of-harmony.yaml) | [edit](../../edit/main/guides/12.0.1/monk/mistweaver/) |
| Monk | Windwalker | [Conduit of the Celestials](guides/12.0.1/monk/windwalker/conduit-of-the-celestials.yaml), [Shado-Pan](guides/12.0.1/monk/windwalker/shado-pan.yaml) | [edit](../../edit/main/guides/12.0.1/monk/windwalker/) |
| Paladin | Holy | [Herald of the Sun](guides/12.0.1/paladin/holy/herald-of-the-sun.yaml), [Lightsmith](guides/12.0.1/paladin/holy/lightsmith.yaml) | [edit](../../edit/main/guides/12.0.1/paladin/holy/) |
| Paladin | Protection | [Lightsmith](guides/12.0.1/paladin/protection/lightsmith.yaml), [Templar](guides/12.0.1/paladin/protection/templar.yaml) | [edit](../../edit/main/guides/12.0.1/paladin/protection/) |
| Paladin | Retribution | [Herald of the Sun](guides/12.0.1/paladin/retribution/herald-of-the-sun.yaml), [Templar](guides/12.0.1/paladin/retribution/templar.yaml) | [edit](../../edit/main/guides/12.0.1/paladin/retribution/) |
| Priest | Discipline | [Oracle](guides/12.0.1/priest/discipline/oracle.yaml), [Voidweaver](guides/12.0.1/priest/discipline/voidweaver.yaml) | [edit](../../edit/main/guides/12.0.1/priest/discipline/) |
| Priest | Holy | [Archon](guides/12.0.1/priest/holy/archon.yaml), [Oracle](guides/12.0.1/priest/holy/oracle.yaml) | [edit](../../edit/main/guides/12.0.1/priest/holy/) |
| Priest | Shadow | [Archon](guides/12.0.1/priest/shadow/archon.yaml), [Voidweaver](guides/12.0.1/priest/shadow/voidweaver.yaml) | [edit](../../edit/main/guides/12.0.1/priest/shadow/) |
| Rogue | Assassination | [Deathstalker](guides/12.0.1/rogue/assassination/deathstalker.yaml), [Fatebound](guides/12.0.1/rogue/assassination/fatebound.yaml) | [edit](../../edit/main/guides/12.0.1/rogue/assassination/) |
| Rogue | Outlaw | [Fatebound](guides/12.0.1/rogue/outlaw/fatebound.yaml), [Trickster](guides/12.0.1/rogue/outlaw/trickster.yaml) | [edit](../../edit/main/guides/12.0.1/rogue/outlaw/) |
| Rogue | Subtlety | [Deathstalker](guides/12.0.1/rogue/subtlety/deathstalker.yaml), [Trickster](guides/12.0.1/rogue/subtlety/trickster.yaml) | [edit](../../edit/main/guides/12.0.1/rogue/subtlety/) |
| Shaman | Elemental | [Farseer](guides/12.0.1/shaman/elemental/farseer.yaml), [Stormbringer](guides/12.0.1/shaman/elemental/stormbringer.yaml) | [edit](../../edit/main/guides/12.0.1/shaman/elemental/) |
| Shaman | Enhancement | [Stormbringer](guides/12.0.1/shaman/enhancement/stormbringer.yaml), [Totemic](guides/12.0.1/shaman/enhancement/totemic.yaml) | [edit](../../edit/main/guides/12.0.1/shaman/enhancement/) |
| Shaman | Restoration | [Farseer](guides/12.0.1/shaman/restoration/farseer.yaml), [Totemic](guides/12.0.1/shaman/restoration/totemic.yaml) | [edit](../../edit/main/guides/12.0.1/shaman/restoration/) |
| Warlock | Affliction | [Hellcaller](guides/12.0.1/warlock/affliction/hellcaller.yaml), [Soul Harvester](guides/12.0.1/warlock/affliction/soul-harvester.yaml) | [edit](../../edit/main/guides/12.0.1/warlock/affliction/) |
| Warlock | Demonology | [Diabolist](guides/12.0.1/warlock/demonology/diabolist.yaml), [Soul Harvester](guides/12.0.1/warlock/demonology/soul-harvester.yaml) | [edit](../../edit/main/guides/12.0.1/warlock/demonology/) |
| Warlock | Destruction | [Diabolist](guides/12.0.1/warlock/destruction/diabolist.yaml), [Hellcaller](guides/12.0.1/warlock/destruction/hellcaller.yaml) | [edit](../../edit/main/guides/12.0.1/warlock/destruction/) |
| Warrior | Arms | [Colossus](guides/12.0.1/warrior/arms/colossus.yaml), [Slayer](guides/12.0.1/warrior/arms/slayer.yaml) | [edit](../../edit/main/guides/12.0.1/warrior/arms/) |
| Warrior | Fury | [Mountain Thane](guides/12.0.1/warrior/fury/mountain-thane.yaml), [Slayer](guides/12.0.1/warrior/fury/slayer.yaml) | [edit](../../edit/main/guides/12.0.1/warrior/fury/) |
| Warrior | Protection | [Colossus](guides/12.0.1/warrior/protection/colossus.yaml), [Mountain Thane](guides/12.0.1/warrior/protection/mountain-thane.yaml) | [edit](../../edit/main/guides/12.0.1/warrior/protection/) |

## Schema

See [schema/guide-schema.yaml](schema/guide-schema.yaml) for the full field reference.

## License

[CC BY-SA 4.0](LICENSE) - These guides represent community knowledge about World of Warcraft gameplay. WoW and all related content are trademarks of Blizzard Entertainment.
