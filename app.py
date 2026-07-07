import json
import os
import uuid
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DATA_FILE = "character_data.json"
ITEMS_FILE = "items_data.json"
REFERENCE_ITEMS_FILE = "reference_items_data.json"
CLASS_DATA_FILE = "class_data.json"
CHARACTERS_DIR = "characters"
CHARACTERS_INDEX = "characters_index.json"

DEFAULT_DATA = {
    "class_name": "", "name": "", "pronouns": "", "ancestry": "", "community": "", "subclass": "",
    "level": 1,
    "evasion": 0,
    "armor": 0, "marked_armor": [],
    "agility": 0, "strength": 0, "finesse": 0, "instinct": 0, "presence": 0, "knowledge": 0,
    "agility_chk": False, "strength_chk": False, "finesse_chk": False,
    "instinct_chk": False, "presence_chk": False, "knowledge_chk": False,
    "damage_threshold_1": 0, "damage_threshold_2": 0,
    "hp": 7, "marked_hp": [], "stress": 6, "marked_stress": [],
    "hope": [False, False, False, False, False, False], "scars": 0,
    "experience_0": "", "experience_1": "", "experience_2": "", "experience_3": "", "experience_4": "",
    "bonus_0": 0, "bonus_1": 0, "bonus_2": 0, "bonus_3": 0, "bonus_4": 0,
    "experience_chk_0": False, "experience_chk_1": False, "experience_chk_2": False, "experience_chk_3": False, "experience_chk_4": False,
    "gold": 0, "handfuls": 0, "bags": 0, "chests": 0,
    "weapon_proficiency": 0,
    "primary_weapon_ref": "",
    "primary_weapon": "",
    "primary_trait": "", "primary_range": "", "primary_damage_dice": "", "primary_type": "",
    "primary_name": "", "primary_feature": "",
    "primary_burden": "", "secondary_burden": "",
    "multiclass_class": "", "multiclass_domain": "", "multiclass_subclass": "",
    "secondary_weapon_ref": "",
    "secondary_weapon": "",
    "secondary_trait": "", "secondary_range": "", "secondary_damage_dice": "", "secondary_type": "",
    "secondary_name": "", "secondary_feature": "",
    "armor_ref": "",
    "armor_text": "",
    "base_threshold_1": 0, "base_threshold_2": 0, "base_score": 0,
    "feature_name": "", "feature": "",
    "tier2_trait_marks": [], "tier2_hp_slots": [], "tier2_stress_slots": [],
    "tier2_experience_bonus": False, "tier2_domain_card": False, "tier2_evasion_bonus": False,
    "tier3_trait_marks": [], "tier3_hp_slots": [], "tier3_stress_slots": [],
    "tier3_experience_bonus": False, "tier3_domain_card": False, "tier3_evasion_bonus": False,
    "tier3_upgraded_subclass": False,
    "tier3_proficiency": [], "tier3_multiclass": [],
    "tier4_trait_marks": [], "tier4_hp_slots": [], "tier4_stress_slots": [],
    "tier4_experience_bonus": False, "tier4_domain_card": False, "tier4_evasion_bonus": False,
    "tier4_upgraded_subclass": False,
    "tier4_proficiency": [], "tier4_multiclass": [],
    "guardian_unstoppable_die": 1, "guardian_unstoppable_active": False,
    "wizard_chosen_number": 1,
    "companion_name": "", "companion_evasion": 10,
    "companion_species": "", "companion_description": "",
    "companion_exp_name_0": "", "companion_exp_value_0": 0,
    "companion_exp_name_1": "", "companion_exp_value_1": 0,
    "companion_exp_name_2": "", "companion_exp_value_2": 0,
    "companion_exp_name_3": "", "companion_exp_value_3": 0,
    "companion_exp_name_4": "", "companion_exp_value_4": 0,
    "companion_attack": "",
    "companion_range": "Melee",
    "companion_damage_die": "d6",
    "companion_stress": 0, "companion_marked_stress": [],
    "companion_training_intelligent": [],
    "companion_training_light_dark": False,
    "companion_training_light_dark_hope": False,
    "companion_training_creature_comfort": False,
    "companion_training_armored": False,
    "companion_training_vicious": [],
    "companion_training_resilient": [],
    "companion_training_bonded": False,
    "companion_training_aware": []
}

DEFAULT_ITEMS = []

DEFAULT_CLASS_DATA = {
    "classes": ["Bard", "Blood Hunter", "Druid", "Guardian", "Ranger", "Rogue", "Seraph", "Sorcerer", "Warrior", "Wizard"],
    "ancestries": ["Clank", "Drakona", "Dwarf", "Elf", "Faerie", "Faun", "Firbolg", "Fungril", "Galapa", "Giant", "Goblin", "Halfling", "Human", "Infernis", "Katari", "Orc", "Ribbet", "Simiah"],
    "communities": ["Highborne", "Loreborne", "Orderborne", "Ridgeborne", "Seaborne", "Slyborne", "Underborne", "Wanderborne", "Wildborne"],
    "domains": ["Arcana", "Blade", "Blood", "Bone", "Codex", "Grace", "Midnight", "Sage", "Splendor", "Valor"],
    "class_domains": {
        "Bard": ["Codex", "Grace"],
        "Blood Hunter": ["Blood", "Blade"],
        "Druid": ["Arcana", "Sage"],
        "Guardian": ["Blade", "Valor"],
        "Ranger": ["Bone", "Sage"],
        "Rogue": ["Grace", "Midnight"],
        "Seraph": ["Splendor", "Valor"],
        "Sorcerer": ["Arcana", "Midnight"],
        "Warrior": ["Blade", "Bone"],
        "Wizard": ["Codex", "Splendor"]
    },
    "class_subclasses": {
        "Bard": ["Troubadour", "Wordsmith"],
        "Blood Hunter": ["Ghost Slayer", "Mutant", "Lycan"],
        "Druid": ["Warden of the Elements", "Warden of Renewal"],
        "Guardian": ["Stalwart", "Vengeance"],
        "Ranger": ["Beastbound", "Wayfinder"],
        "Rogue": ["Nightwalker", "Syndicate"],
        "Seraph": ["Divine Wielder", "Winged Sentinel"],
        "Sorcerer": ["Elemental Origin", "Primal Origin"],
        "Warrior": ["Call of the Brave", "Call of the Slayer"],
        "Wizard": ["School of Knowledge", "School of War"]
    },
    "hope_features": {
        "Bard": "Make a Scene: Spend 3 Hope to temporarily Distract a target within Close range, giving them a -2 penalty to their Difficulty.",
        "Blood Hunter": "**Blood Maledict**: Spend 3 Hope to target a creature within Far range or in a vision from your Grim Psychometry. Until you finish a rest, take Severe damage, or use this feature again, you have advantage on all action rolls against the target.",
        "Druid": "Evolution: Spend 3 Hope to transform into a Beastform without marking a Stress. When you do, choose one trait to raise by +1 until you drop out of that Beastform.",
        "Guardian": "Frontline Tank: Spend 3 Hope to clear 2 Armor Slots.",
        "Ranger": "Hold Them Off: Spend 3 Hope when you succeed on an attack with a weapon to use that same roll against two additional adversaries within range of the attack.",
        "Rogue": "Rogue's Dodge: Spend 3 Hope to gain a +2 bonus to your Evasion until the next time an attack succeeds against you. Otherwise, this bonus lasts until your next rest.",
        "Seraph": "Life Support: Spend 3 Hope to clear a Hit Point on an ally within Close range.",
        "Sorcerer": "Volatile Magic: Spend 3 Hope to reroll any number of your damage dice on an attack that deals magic damage.",
        "Warrior": "No Mercy: Spend 3 Hope to gain a +1 bonus to your attack rolls until your next rest.",
        "Wizard": "Not This Time: Spend 3 Hope to force an adversary within Far range to reroll an attack or damage roll."
    },
    "class_features": {}
}

def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_characters_index():
    return load_json(CHARACTERS_INDEX, {"characters": [], "active": None})

def save_characters_index(index):
    save_json(CHARACTERS_INDEX, index)

def get_active_character_id():
    index = get_characters_index()
    return index.get("active") or (index["characters"][0]["id"] if index["characters"] else None)

def get_character_data(char_id):
    if not char_id:
        return dict(DEFAULT_DATA)
    path = os.path.join(CHARACTERS_DIR, f"{char_id}.json")
    raw = load_json(path, None)
    if raw is None:
        return dict(DEFAULT_DATA)
    if "heritage" in raw and "ancestry" not in raw:
        raw["ancestry"] = raw.pop("heritage")
    data = dict(DEFAULT_DATA)
    data.update(raw)
    return data

def save_character_data(char_id, data):
    os.makedirs(CHARACTERS_DIR, exist_ok=True)
    save_json(os.path.join(CHARACTERS_DIR, f"{char_id}.json"), data)

def update_character_index_entry(char_id, data):
    index = get_characters_index()
    for c in index["characters"]:
        if c["id"] == char_id:
            c["name"] = data.get("name", "Unnamed")
            c["level"] = data.get("level", 1)
            c["class_name"] = data.get("class_name", "")
            break
    save_characters_index(index)

def migrate_legacy_data():
    if os.path.exists(DATA_FILE) and not os.path.exists(CHARACTERS_INDEX):
        raw = load_json(DATA_FILE, None)
        if raw:
            if "heritage" in raw and "ancestry" not in raw:
                raw["ancestry"] = raw.pop("heritage")
            char_id = str(uuid.uuid4())
            os.makedirs(CHARACTERS_DIR, exist_ok=True)
            save_character_data(char_id, raw)
            index = {
                "characters": [{
                    "id": char_id,
                    "name": raw.get("name", "Unnamed"),
                    "level": raw.get("level", 1),
                    "class_name": raw.get("class_name", "")
                }],
                "active": char_id
            }
            save_characters_index(index)

migrate_legacy_data()

def load_items():
    return load_json(ITEMS_FILE, list(DEFAULT_ITEMS))

def load_default_items():
    return load_json(REFERENCE_ITEMS_FILE, list(DEFAULT_ITEMS))

def save_items(items):
    save_json(ITEMS_FILE, items)

def load_class_data():
    raw = load_json(CLASS_DATA_FILE, None)
    if raw is None:
        return dict(DEFAULT_CLASS_DATA)
    cd = dict(DEFAULT_CLASS_DATA)
    cd.update(raw)
    return cd

def save_class_data(data):
    save_json(CLASS_DATA_FILE, data)

def make_item_ref(item):
    name = item.get("weapon") or item.get("armor") or item.get("name", "")
    if item.get("type") == "armor":
        return f"armor_{name}"
    return f"weapon_{name}"

@app.route("/")
def index():
    index_data = get_characters_index()
    active_id = index_data.get("active")
    if not active_id and index_data["characters"]:
        active_id = index_data["characters"][0]["id"]
        index_data["active"] = active_id
        save_characters_index(index_data)
    data = get_character_data(active_id) if active_id else dict(DEFAULT_DATA)
    items = load_items()
    default_items = load_default_items()
    class_data = load_class_data()
    return render_template("index.html", data=data, characters=index_data["characters"], active_id=active_id, items=items, default_items=default_items, class_data=class_data, default_ancestries=DEFAULT_CLASS_DATA["ancestries"])

@app.route("/save", methods=["POST"])
def save():
    index_data = get_characters_index()
    active_id = index_data.get("active")
    if not active_id:
        return jsonify({"status": "error", "message": "No active character"}), 400
    incoming = request.json
    current = get_character_data(active_id)
    current.update(incoming)
    save_character_data(active_id, current)
    update_character_index_entry(active_id, current)
    return jsonify({"status": "ok"})

@app.get("/api/characters")
def list_characters():
    index_data = get_characters_index()
    return jsonify(index_data["characters"])

@app.post("/api/characters/create")
def create_character():
    name = request.json.get("name", "").strip() or "Unnamed"
    char_id = str(uuid.uuid4())
    data = dict(DEFAULT_DATA)
    data["name"] = name
    os.makedirs(CHARACTERS_DIR, exist_ok=True)
    save_character_data(char_id, data)
    index = get_characters_index()
    index["characters"].append({
        "id": char_id,
        "name": name,
        "level": 1,
        "class_name": ""
    })
    index["active"] = char_id
    save_characters_index(index)
    return jsonify({"status": "ok", "id": char_id})

@app.post("/api/characters/select")
def select_character():
    char_id = request.json.get("id")
    index = get_characters_index()
    if any(c["id"] == char_id for c in index["characters"]):
        index["active"] = char_id
        save_characters_index(index)
        return jsonify({"status": "ok"})
    return jsonify({"status": "error", "message": "Character not found"}), 404

@app.post("/api/characters/delete")
def delete_character():
    char_id = request.json.get("id")
    index = get_characters_index()
    index["characters"] = [c for c in index["characters"] if c["id"] != char_id]
    path = os.path.join(CHARACTERS_DIR, f"{char_id}.json")
    if os.path.exists(path):
        os.remove(path)
    if index["active"] == char_id:
        index["active"] = index["characters"][0]["id"] if index["characters"] else None
    save_characters_index(index)
    return jsonify({"status": "ok"})

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(load_items())

@app.route("/items/save", methods=["POST"])
def save_items_route():
    incoming = request.json
    if not isinstance(incoming, list):
        return jsonify({"status": "error", "message": "Expected a list"}), 400
    save_items(incoming)
    return jsonify({"status": "ok"})

@app.route("/class-data", methods=["GET"])
def get_class_data():
    return jsonify(load_class_data())

@app.route("/class-data/save", methods=["POST"])
def save_class_data_route():
    incoming = request.json
    cd = load_class_data()
    if "ancestries" in incoming:
        cd["ancestries"] = incoming["ancestries"]
    save_class_data(cd)
    return jsonify({"status": "ok"})

@app.template_filter("make_item_ref")
def template_make_item_ref(item):
    name = item.get("weapon") or item.get("armor") or item.get("name", "")
    if item.get("type") == "armor":
        return f"armor_{name}"
    return f"weapon_{name}"

@app.template_filter("tier_from_level")
def tier_from_level(level):
    if level >= 8: return 4
    if level >= 5: return 3
    if level >= 2: return 2
    return 1

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
