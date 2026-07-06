# Daggerheart Character Sheet

A web-based character sheet application for the Daggerheart TTRPG, built with Python (Flask) and vanilla JavaScript.

## Setup

### Requirements
- Python 3.8+
- Flask (`pip install flask`)

### Running
```bash
python app.py
```
Open `http://127.0.0.1:5000` in a browser.

## Architecture

### Backend (`app.py`)
 - Flask app with routes:
   - `GET /` — Renders the character sheet with current data, items, and class data
   - `POST /save` — Accepts JSON body, saves to the active character's file under `characters/`
   - `GET /api/characters` — Lists all characters from `characters_index.json`
   - `POST /api/characters/create` — Creates a new character and sets it as active
   - `POST /api/characters/select` — Sets the active character by ID
   - `POST /api/characters/delete` — Deletes a character and its data file
   - `GET /items` — Returns all items (weapons/armors) from `items_data.json`
   - `POST /items/save` — Saves items list to `items_data.json`
   - `GET /class-data` — Returns class/ancestry/community options and hope features
   - `POST /class-data/save` — Saves class data to `class_data.json`
- Default data defined in `DEFAULT_DATA`, `DEFAULT_ITEMS`, `DEFAULT_CLASS_DATA` dicts
- Custom Jinja2 filter `make_item_ref` for generating item reference strings

### Frontend (`templates/index.html`)
- Jinja2 template rendered server-side with current data pre-populated
- All field interaction happens client-side; only explicit Save triggers a server write
- Client-side data is collected via `collectFormData()`

### Styles (`static/style.css`)
- Dark theme with `#1a1a2e` background, `#16213e` section cards, `#e94560` accent
- Modal overlay for item and character details management

## Layout

### Character Bar
- **Character dropdown** — Select from existing characters (format: `<Name> - Level <Level> <Class>`)
- **+ New** (green) — Creates a new character with a prompted name and switches to it
- **Delete** (red) — Deletes the selected character and its data file

### Header
- **Items** (green) — Opens the Item Management modal for adding/editing/deleting weapons and armors
- **Details** (orange) — Opens the Character Details modal for managing class/ancestry/community options and hope features
- **Load** (blue) — Opens a file picker to load a `.json` character file into the browser
- **Download** (purple) — Exports current form data (compressed — weapon/armor fields stored as references)
- **Save** (red) — Persists current browser state to the Flask server

### Character Info
| Field | Type | Notes |
|-------|------|-------|
| Class | dropdown | Editable via Details modal |
| Name | text | |
| Pronouns | text | |
| Ancestry | dropdown | Editable via Details modal |
| Community | dropdown | Editable via Details modal |
| Subclass | text | |
| Level | number | |

### Stats & Attributes (two-column)
**Left column:**
| Field | Type | Notes |
|-------|------|-------|
| Evasion | number | |
| Armor | number | 0–12, controls Marked Armor count |
| Marked Armor | checkboxes | Dynamically generated based on Armor value |

**Right column:**
| Field | Type | Notes |
|-------|------|-------|
| Agility, Strength, Finesse, Instinct, Presence, Knowledge | number + checkbox | Each has an associated proficiency checkbox |

### Combat (two-column)
**Left column:**
| Field | Type | Notes |
|-------|------|-------|
| Damage Threshold 1 | number | Labeled "Minor Damage" above, "Major Damage" below |
| Damage Threshold 2 | number | Labeled "Severe Damage" below |
| HP | number | 0–12, controls Marked HP count |
| Marked HP | checkboxes | Dynamically generated based on HP value |
| Stress | number | 0–12, controls Marked Stress count |
| Marked Stress | checkboxes | Dynamically generated based on Stress value |
| Hope | checkboxes | 6 fixed checkboxes |
| Scars | number | 0–6, disables hope checkboxes right-to-left |
| Hope Feature | text | Displayed below Hope/Scars, depends on selected class |

**Right column:**
| Field | Type | Notes |
|-------|------|-------|
| Weapon Proficiency | number | |
| Primary Weapon | dropdown + text | Dropdown selects from saved weapons; fields auto-filled and read-only |
| Trait, Range, Damage Dice, Type | text (read-only) | Populated from selected weapon item |
| Name, Feature | text (read-only) | Populated from selected weapon item |
| Secondary Weapon | dropdown + text | Same as Primary Weapon |

### Experience
| Field | Type | Notes |
|-------|------|-------|
| Experience (0–4) | text | Five rows, each with a bonus field and disable checkbox |
| Bonus (0–4) | number | 0–5, one per experience row |
| Disable checkbox | checkbox | When checked, grays out and disables both the experience text and bonus for that row (values preserved) |

### Gold
| Field | Type | Notes |
|-------|------|-------|
| Gold | number | |
| Handfuls | number | |
| Bags | number | |
| Chests | number | |
| Total | number | Read-only, auto-calculated: `Gold + Handfuls×10 + Bags×100 + Chests×1000` |

### Equipped Armor
| Field | Type | Notes |
|-------|------|-------|
| Select Armor | dropdown | Dropdown selects from saved armors |
| Armor | text (read-only) | Populated from selected armor item |
| Base Threshold 1 | number (read-only) | Populated from selected armor item |
| Base Threshold 2 | number (read-only) | Populated from selected armor item |
| Base Score | number (read-only) | Populated from selected armor item |
| Name | text (read-only) | Populated from selected armor item |
| Feature | text (read-only) | Populated from selected armor item |

## Data Files

- **`characters_index.json`** — Index of all characters (id, name, level, class) and active character
- **`characters/{id}.json`** — Individual character sheet data files
- **`items_data.json`** — Persisted list of weapon and armor items
- **`class_data.json`** — Persisted class/ancestry/community options and hope features

## Item Management

Items (weapons and armors) are managed via the Items button in the header. The modal provides:
- A list of all saved items with Edit/Delete buttons
- Add Item button to create new items
- Download Items to export as JSON
- Upload Items to import from JSON
- Save Items to persist to server

Item fields:
- **Weapons**: Type (auto=weapon), Weapon, Trait, Range, Damage Dice, Type (damage), Name, Feature
- **Armors**: Type (auto=armor), Armor, Base Threshold 1, Base Threshold 2, Base Score, Name, Feature

## Character Details Management

The Details button opens a modal for editing:
- Class options (add/remove)
- Ancestry options (add/remove)
- Community options (add/remove)
- Hope Feature text for each class

## Data Persistence

- **Server save**: Character data → `characters/{id}.json`, Items → `items_data.json`, Class data → `class_data.json`
- **Download/Upload**: Character data exported/imported as `.json` files via the browser. Weapon/armor fields are compressed to reference strings (format: `<type>_<weapon/armor>_<name>`)
- **Items Download/Upload**: Items can be exported/imported separately
- **Chk-group arrays**: Array fields (`marked_armor`, `marked_hp`, `marked_stress`, `hope`) are stored as boolean arrays

## Interactive Behaviors

- **Armor/HP/Stress → checkboxes**: Changing the numeric value adds or removes checkboxes in the corresponding "Marked" group
- **Scars → Hope**: Increasing Scars disables and clears hope checkboxes from right to left (e.g., Scars=2 disables the 2 rightmost hope boxes)
- **Experience disable**: Checking a row's disable checkbox grays out (`opacity: 0.35`) and disables the text and bonus inputs, but does not clear their values
- **Gold Total**: Recalculated on any change to Gold, Handfuls, Bags, or Chests
- **Weapon/Armor dropdowns**: Selecting an item from the dropdown populates the corresponding read-only fields. Selecting "Empty" clears them.
- **Class → Hope Feature**: Changing the class dropdown updates the hope feature text displayed under Hope/Scars
- **Character management**: Switching characters reloads the page; create/delete operations redirect to the updated character list
