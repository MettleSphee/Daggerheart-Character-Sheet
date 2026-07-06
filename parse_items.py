"""Extract weapons and armor from MHTML reference files and output reference_items_data.json."""
import re, json, quopri

def load_decoded(path):
    with open(path, 'rb') as f:
        raw = f.read()
    return quopri.decodestring(raw).decode('utf-8')

def extract_feature(html_section):
    """Extract full feature text from a feature table cell: 'FeatName: Description'"""
    m = re.search(r'<strong>([^<]*)</strong>\s*(.*?)</td>', html_section, re.DOTALL)
    if not m:
        return ''
    name = m.group(1).strip().rstrip(':').strip()
    desc = m.group(2).strip()
    if not name and not desc:
        return ''
    if not desc:
        return name
    if not name:
        return desc
    return f'{name}: {desc}'

def parse_weapons(path):
    html = load_decoded(path)
    weapons = []
    for m in re.finditer(
        r'<tr\s+class="weapon"[^>]*?data-name="([^"]*)"[^>]*?data-cat="([^"]*)"[^>]*?data-damage_type="([^"]*)"[^>]*?data-trait="([^"]*)"[^>]*?data-range="([^"]*)"[^>]*?data-die="([^"]*)"[^>]*?data-burden="([^"]*)"',
        html):
        name, cat, dmg_type, trait, range_, die, burden = m.groups()
        rest = html[m.end():m.end()+1000]
        dmg_m = re.search(r'<td\s+class="damage">([^<]*)<', rest)
        damage_text = dmg_m.group(1).strip() if dmg_m else ''
        damage_dice = re.sub(r'\s+(phy|mag|phy or mag)$', '', damage_text, flags=re.IGNORECASE)
        damage_dice = re.sub(r'\bd(\d+)', lambda m: 'D' + m.group(1), damage_dice)
        damage_dice = re.sub(r'\s*\+\s*', ' + ', damage_dice)
        # Find feature column
        fi = rest.find('<td class="feature">')
        if fi >= 0:
            feat_cell = rest[fi:fi+600]
            feature = extract_feature(feat_cell)
        else:
            feature = ''
        weapons.append({
            "name": name,
            "type": "weapon",
            "trait": trait,
            "range": range_,
            "damage_dice": damage_dice,
            "damage_type": dmg_type,
            "burden": burden,
            "feature": feature
        })
    return weapons

def parse_armor(path):
    html = load_decoded(path)
    armors = []
    for m in re.finditer(
        r'<tr\s+class="armourPiece"[^>]*?data-name="([^"]*)"[^>]*?data-tier="(\d+)"[^>]*?data-thresholds="([^"]*)"[^>]*?data-score="(\d+)"[^>]*?data-feature="([^"]*)"',
        html):
        name, tier, thresholds, score, data_feature = m.groups()
        thresholds = thresholds.replace('/', '').strip()
        parts = thresholds.split()
        bt1 = parts[0] if parts else ''
        bt2 = parts[-1] if len(parts) > 1 else ''
        try: bt1 = int(bt1)
        except: pass
        try: bt2 = int(bt2)
        except: pass
        # Extract full feature from the feature column
        rest = html[m.end():m.end()+1000]
        fi = rest.find('<td class="feature">')
        if fi >= 0:
            feat_cell = rest[fi:fi+600]
            feature = extract_feature(feat_cell)
        else:
            feature = data_feature  # fallback
        armors.append({
            "name": name,
            "type": "armor",
            "base_threshold_1": bt1,
            "base_threshold_2": bt2,
            "base_score": int(score),
            "feature": feature
        })
    return armors

weapons = parse_weapons(r'References\Weapons _ Daggerheart.org.mhtml')
armor = parse_armor(r'References\Armor _ Daggerheart.org.mhtml')

seen_names = set()
all_items = []
for w in weapons:
    if w['name'] not in seen_names:
        all_items.append(w)
        seen_names.add(w['name'])
for a in armor:
    if a['name'] not in seen_names:
        all_items.append(a)
        seen_names.add(a['name'])

with open('reference_items_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_items, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(weapons)} weapons and {len(armor)} armors")
print(f"Total unique items: {len(all_items)}")
for a in armor:
    print(f"  Armor: {a['name']} (BT1={a['base_threshold_1']}, BT2={a['base_threshold_2']})")
print(f"\nWritten to reference_items_data.json")
