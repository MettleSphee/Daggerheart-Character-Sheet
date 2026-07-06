# Changelog

## [Unreleased]

### Initial implementation
- Created Flask application with character sheet fields: Name, Pronouns, Heritage, Subclass, Level, Evasion, Armor, Spent Armor, Agility/Strength/Finesse/Instinct/Presence/Knowledge (with checkmarks), Damage Threshold 1 & 2, HP, Marked HP, Stress, Marked Stress, Hope, Experience 1–5, Gold/Handfuls/Bags/Chests, Weapon Proficiency, Primary Weapon (Trait/Range/Damage Dice/Type/Name/Feature), Secondary Weapon (Trait/Range/Damage Dice/Type/Name/Feature), Armor (text), Base Threshold 1 & 2, Base Score, Name (feature), Feature
- Dark theme styling
- Save button persists all data to `character_data.json` via POST

### Spent Armor → Marked Armor checkboxes
- Replaced numeric Spent Armor with Marked Armor: dynamic checkbox count tied to Armor value
- Same treatment for Marked HP (tied to HP) and Marked Stress (tied to Stress)
- Renamed Spent Armor to Marked Armor

### HP/Stress defaults, bounds, field sizing
- HP default set to 7, Stress default to 6
- HP, Stress, Armor capped at max 12 with `min`/`max` attributes
- Fields shortened with `.field-short` class (90px)

### Hope → 6 checkboxes + Scars
- Replaced numeric Hope with 6 fixed checkboxes
- Added Scars numeric field (0–6)
- Scars disables/clears hope checkboxes from right to left

### Experience rework
- Changed from 5 horizontal labeled fields to vertical rows under a single "Experience" heading
- Each row: text field + Bonus numeric (1–5) + disable checkbox
- Added "Bonus" column header
- Disable checkbox grays out and disables both fields (values preserved)
- Bonus default changed from 1 to 0

### Equipped Armor grouping
- Grouped Armor (text), Base Thresholds, Base Score, Name, Feature under "Equipped Armor" heading

### Layout restructure
- Added Class field to left of Name
- Moved Level to right of Subclass in same row
- Stats section: left column (Evasion, Armor, Marked Armor), right column (Agility–Knowledge in one row)
- Combat section: left column (Damage Thresholds, HP/Marked HP, Stress/Marked Stress, Hope/Scars), right column (Primary Weapon, Secondary Weapon)
- Stress/Marked Stress moved under HP/Marked HP
- Experience and Gold moved to left column under Hope/Scars
- Weapon Proficiency moved above Primary Weapon in right column
- Equipped Armor stays as standalone section at bottom

### Damage threshold labels
- Compact two-line labels: Minor/Damage, Major/Damage, Severe/Damage
- Labels stacked vertically via flex column

### Gold section
- Added "Gold" heading
- Compact field widths with centered text
- Added read-only Total field: `Gold + Handfuls×10 + Bags×100 + Chests×1000`

### Header buttons (Load/Download/Save)
- Added Load button (opens file picker for `.json` files)
- Added Download button (exports as `"{Class} - {Name}.json"`)
- Loaded data populates browser form only; Save required to persist to server
- Disabled form inputs now properly included in data collection (fix for experience checkboxes hiding values)

### Weapon field compaction
- Weapon sub-fields (Trait, Range, Damage Dice, Type) given narrower min-width (70px) to fit in one row

### Documentation
- Added `Documentation.md`
- Added `changelog.md`

### Items & Armor management (SPEC_2)
- Added item management modal (Items button in header) with add/edit/delete for weapons and armors
- Weapons stored with fields: Weapon, Trait, Range, Damage Dice, Type, Name, Feature
- Armors stored with fields: Armor, Base Threshold 1, Base Threshold 2, Base Score, Name, Feature
- Items have type selector (Weapon/Armor) in the edit form
- Items can be downloaded, uploaded, and saved to server via `items_data.json`
- Primary/Secondary weapon dropdowns populated from saved weapons; selecting one populates character sheet fields as read-only
- Equipped Armor dropdown populated from saved armors; selecting one populates fields as read-only
- Download JSON uses `<type>_<weapon>_<name>` reference convention; weapon/armor fields omitted from download
- Load character JSON expands item references by looking up items

### Character details (SPEC_2)
- Heritage split into two separate fields: Ancestry (dropdown) and Community (dropdown)
- Class changed from text to dropdown, populated from editable class list
- Added Character Details modal (Details button) to manage class, ancestry, community options
- Added Hope Feature text per class, editable in details modal and displayed under Hope/Scars on the sheet
- Added `class_data.json` for persisting class options, ancestry options, community options, and hope features

### Character management
- Added multi-character support with individual character files stored in `characters/` directory
- Added character selector bar at top of page with dropdown showing `<Name> - Level <Level> <Class>` format
- Added + New button to create characters (prompts for name), Delete button to remove characters
- Added API endpoints: `/api/characters` (list), `/api/characters/create` (create), `/api/characters/select` (switch), `/api/characters/delete` (remove)
- Legacy `character_data.json` auto-migrated to new format on first run
- Character index entries auto-update on save (name/level/class)
