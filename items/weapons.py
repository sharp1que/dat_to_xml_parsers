import os
import xml.etree.ElementTree as ET

from class_generator.base import *
from class_generator.generated_classes import *

items: dict[str, AbstractItemInfo] = dict()
datapack_items = dict()

item_baseinfos: dict[str, ItemBaseinfo] = dict()
item_names: dict[str, ItemName] = dict()

item_icons: dict[str, str] = dict()
item_types: dict[str, str] = dict()


diff = []

missing: dict[str, AbstractItemInfo] = dict()

# enum EItemType
# {
#     ITEM_WEAPON,
#     ITEM_ARMOR,
#     ITEM_ACCESSARY,
#     ITEM_QUESTITEM,
#     ITEM_ASSET,
#     ITEM_ETCITEM
# };


# enum EEtcItemType
# {
#     ITEME_NONE,
#     ITEME_SCROLL,
#     ITEME_ARROW,
#     ITEME_POTION,
#     ITEME_SPELLBOOK,
#     ITEME_RECIPE,
#     ITEME_MATERIAL,
#     ITEME_PET_COLLAR,
#     ITEME_CASTLE_GUARD,
#     ITEME_DYE,
#     ITEME_SEED,
#     ITEME_SEED2,
#     ITEME_HARVEST,
#     ITEME_LOTTO,
#     ITEME_RACE_TICKET,
#     ITEME_TICKET_OF_LORD,
#     ITEME_LURE,
#     ITEME_CROP,
#     ITEME_MATURECROP,
#     ITEME_ENCHT_WP,
#     ITEME_ENCHT_AM,
#     ITEME_BLESS_ENCHT_WP,
#     ITEME_BLESS_ENCHT_AM,
#     ITEME_COUPON,
#     ITEME_ELIXIR,
#     ITEME_ENCHT_ATTR,
#     ITEME_ENCHT_ATTR_CURSED,
#     ITEME_BOLT,
#     ITEME_ENCHT_ATTR_INC_PROP_ENCHT_WP,
#     ITEME_ENCHT_ATTR_INC_PROP_ENCHT_AM,
#     ITEME_ENCHT_ATTR_CRYSTAL_ENCHANT_AM,
#     ITEME_ENCHT_ATTR_CRYSTAL_ENCHANT_WP,
#     ITEME_ENCHT_ATTR_ANCIENT_CRYSTAL_ENCHANT_AM,
#     ITEME_ENCHT_ATTR_ANCIENT_CRYSTAL_ENCHANT_WP,
#     ITEME_ENCHT_ATTR_RUNE,
#     ITEME_ENCHT_ATTRT_RUNE_SELECT,
#     ITEME_TELEPORTBOOKMARK,
#     ITEME_CHANGE_ATTR,
#     ITEME_SOULSHOT,
#     ITEME_SHAPE_SHIFTING_WP,
#     ITEME_BLESS_SHAPE_SHIFTING_WP,
#     ITEME_SHAPE_SHIFTING_WP_FIXED,
#     ITEME_SHAPE_SHIFTING_AM,
#     ITEME_BLESS_SHAPE_SHIFTING_AM,
#     ITEME_SHAPE_SHIFTING_AM_FIXED,
#     ITEME_SHAPE_SHIFTING_HAIRACC,
#     ITEME_BLESS_SHAPE_SHIFTING_HAIRACC,
#     ITEME_SHAPE_SHIFTING_HAIRACC_FIXED,
#     ITEME_RESTORE_SHAPE_SHIFTING_WP,
#     ITEME_RESTORE_SHAPE_SHIFTING_AM,
#     ITEME_RESTORE_SHAPE_SHIFTING_HAIRACC,
#     ITEME_RESTORE_SHAPE_SHIFTING_ALLITEM,
#     ITEME_BLESS_INC_PROP_ENCHT_WP,
#     ITEME_BLESS_INC_PROP_ENCHT_AM,
#     ITEME_CARD_EVENT,
#     ITEME_SHAPE_SHIFTING_ALLITEM_FIXED,
#     ITEME_MULTI_ENCHT_WP,
#     ITEME_MULTI_ENCHT_AM,
#     ITEME_MULTI_INC_PROB_ENCHT_WP,
#     ITEME_MULTI_INC_PROB_ENCHT_AM,
#     ITEME_NICK_COLOR_OLD,
#     ITEME_NICK_COLOR_NEW,
#     ITEME_ENSOUL_STONE,
#     ITEME_ENCHT_AG,
#     ITEME_BLESS_ENCHT_AG,
#     ITEME_MULTI_ENCHT_AG,
#     ITEME_ANCIENT_CRYSTAL_ENCHANT_AG,
#     ITEME_INC_PROP_ENCHT_AG,
#     ITEME_BLESS_INC_PROP_ENCHT_AG,
#     ITEME_MULTI_INC_PROB_ENCHT_AG,
#     ITEME_LOCK_ITEM,
#     ITEME_UNLOCK_ITEM,
#     ITEME_BULLET,
#     ITEME_MAGIC_LAMP,
#     ITEME_COSTUME_BOOK,
#     ITEME_COSTUME_BOOK_RD_ALL,
#     ITEME_COSTUME_BOOK_RD_PART,
#     ITEME_COSTUME_BOOK_1,
#     ITEME_COSTUME_BOOK_2,
#     ITEME_COSTUME_BOOK_3,
#     ITEME_COSTUME_BOOK_4,
#     ITEME_COSTUME_BOOK_5,
#     ITEME_POLY_ENCHANT_WP,
#     ITEME_POLY_ENCHANT_AM,
#     ITEME_POLY_INC_ENCHANT_PROP_WP,
#     ITEME_POLY_INC_ENCHANT_PROP_AM,
#     ITEME_CURSED_ENCHANT_WP,
#     ITEME_CURSED_ENCHANT_AM,
#     ITEME_BLESS_UPGRADE,
#     ITEME_ORB,
#     ITEME_ITEM_RESTORE_COIN,
#     ITEME_SPECIAL_ENCHT_WP,
#     ITEME_SPECIAL_ENCHT_AM,
#     ITEME_NICK_COLOR_ICON,
#     ITEME_TRADE_TICKET,
#     ITEME_PET_FOODER,
#     ITEME_VITAL_POTION,
#     ITEME_RELICS_SUMMON
# };

def parse_baseinfos():
    with open('ItemBaseInfo_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            baseinfo = ItemBaseinfo.from_string(line)
            item_baseinfos.setdefault(baseinfo.id, baseinfo)

def parse_weapons():
    with open('Weapongrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            weapon = Weapongrp.from_string(line)
            items.setdefault(weapon.object_id, weapon)
            item_types.setdefault(weapon.object_id, weapon.get_item_type())

def parse_armor():
    with open('Armorgrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            armor = Armorgrp.from_string(line)
            items.setdefault(armor.object_id, armor)
            item_types.setdefault(armor.object_id, armor.get_item_type())

def parse_etc():
    with open('EtcItemgrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            etc = EtcItemgrp.from_string(line)
            items.setdefault(etc.object_id, etc)
            item_types.setdefault(etc.object_id, etc.get_item_type())

def parse_item_names():
    with open('ItemName_ClassicAden-eu.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            itemName = ItemName.from_string(line)
            item_names.setdefault(itemName.id, itemName)


use_skill_types = []

def get_default_action_by_ex_item_type(item_tag, ex_item_type):
    if item_tag == 'Weapon' or item_tag == 'Armor':
        return 'EQUIP'
    if ex_item_type == 'potion':
        pass
    return 'NONE'

def get_item_icon(item_id):
    if item_id in items:
        return items[item_id].get_icon()[1:-1].split(";")[0][1:-1] # ебать
    return 'Icon.etc_question_mark_i00'

def get_default_action(item_id):
    return 'EQUIP' if get_item_tag(item_id) == "Armor" or get_item_tag(item_id) == "Weapon" else 'NONE'

def get_item_name(item_id):
    if item_id in item_names:
        return item_names[item_id].name[1:-1]
    return 'Unknown'

def get_item_add_name(item_id):
    if item_id in item_names:
        return item_names[item_id].additionalname[1:-1]
    return 'Unknown'

def get_item_desc(item_id):
    return item_names[item_id].description

# armor, weapon, etc
def get_item_tag(item_id: str) -> str:
    return items.get(item_id).get_class_type()

# shield, helmet, etc
def get_item_type(item_id):
    if item_id in item_types:
        return items[item_id].get_item_type()
    return "NONE"

def is_tradable(item_id):
    if item_id in item_names:
        return str(item_names[item_id].is_trade == "1").lower()
    return "false"

def is_dropable(item_id):
    if item_id in item_names:
        return str(item_names[item_id].is_drop == "1").lower()

def is_sellable(item_id):
    if item_id in item_baseinfos:
        return str(item_baseinfos[item_id].default_price > 0).lower()
    return "false"

def is_destroyable(item_id):
    if item_id in item_names:
        return str(item_names[item_id].is_destruct == "1").lower()
    return "false"

def is_private_store(item_id):
    if item_id in item_names:
        return str(item_names[item_id].is_private_store == "1").lower()
    return "false"

def is_stackable(item_id):
    if item_id in items:
        return str(items[item_id].get_consume_type().lower().contains('stackable')).lower()
    return "false"

def get_auto_use_type(item_id):
    if item_id in item_names:
        return item_names[item_id].get_consume_type()
    return "normal"

def get_immediate_effect(item_id):
    if item_id in items:
        con_type = items[item_id].get_consume_type()
        if con_type == 'immediate' or con_type == 'stackable_immediate':
            return 'true'
    return 'false'

BASE_ITEM_DIR = 'D:/Projects/Essence/dist/game/data/stats/items/'
OUT_ITEM_DIR = './out'

def parse_datapack_items():
    for path in os.walk(BASE_ITEM_DIR):
        for file in path[2]:
            if '.xml' in file:
                try:
                    root = ET.parse(os.path.join(path[0], file))  # <list>
                    for item in root.iterfind('item'):
                        item_id = item.get('id')
                        item_name = item.get('name')
                        datapack_items[item_id] = item
                except Exception as e:
                    print(e)
                    pass

    print(f'Loaded {len(datapack_items)} items from datapack.')

def check_missing_items():
    for obj_id in items.keys():
        if obj_id not in datapack_items.keys():
            missing[obj_id] = items[obj_id]

    print(f'Missing {len(missing)} items.')

    with open('missing_items.txt', 'w', encoding='utf8') as out:
        for item_id in missing.keys():
            out.write(f' - Missing item [{item_id}][{get_item_name(item_id)}] from DataPack.\n')

def generate_file_name(skill_id):
    lower_bound = (int(skill_id) // 100) * 100
    upper_bound = lower_bound + 99
    return f"{lower_bound}-{upper_bound}.xml"

def get_itemtype_key(item_id):
    if get_item_tag(item_id) == 'EtcItem':
        return 'etcitem_type'
    elif get_item_tag(item_id) == 'Armor':
        return 'armor_type'
    elif get_item_tag(item_id) == 'Weapon':
        return 'weapon_type'

def get_material(item_id):
    if item_id in items:
        return items[item_id].get_material()
    return 'NONE'


def get_weight(item_id):
    if item_id in item_types:
        return items[item_id].get_weight()
    return 0

def handle_missing():
    changes = {}

    for item_id, item in missing.items():
        file_name = generate_file_name(item_id)
        try:
            if file_name not in changes:
                changes.setdefault(file_name, [])

            changes[file_name].append(item)
            # changes[file_name].append({
            #     'id': item_id,
            #     'name': get_item_name(item_id),
            #     'additional_name': get_item_add_name(item_id),
            #     'type': get_item_tag(item_id),
            #     'icon': get_item_icon(item_id),
            #     get_itemtype_key(item_id): get_item_type(item_id),
            #     'immediate_effect': get_immediate_effect(item_id),
            #     'default_action': get_default_action(item_id),
            #     'material': get_material(item_id),
            #     'weight': get_weight(item_id),
            #     'is_tradable': is_tradable(item_id),
            #     'is_dropable': is_dropable(item_id),
            #     'is_sellable': is_sellable(item_id),
            #     'is_stackable': is_stackable(item_id)
            # })

        except Exception as e:
            print(e)
            continue

    items_list: dict[str, AbstractItemInfo]
    for file_name, items_list in changes.items():
        filepath = os.path.join(BASE_ITEM_DIR, file_name)
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            root = ET.Element('list')
        else:
            el_tree = ET.parse(filepath)
            root = el_tree.getroot()

        existing_item_ids = {item.get('id') for item in root.findall('item')}

        for item in items_list.values():
            item_id = item.object_id
            if item.object_id not in existing_item_ids:
                new_sk_el = ET.SubElement(root, 'item', attrib={'id': item.object_id, 'name': get_item_name(item_id), 'additionalName': get_item_add_name(item_id), 'type': get_item_tag(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'icon', 'val': item.get_icon()})
                ET.SubElement(new_sk_el, 'set', {'name': 'default_action', 'val': get_default_action(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'immediate_effect', 'val': get_immediate_effect(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': get_itemtype_key(item_id), 'val': get_item_type(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'material', 'val': get_material(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'is_tradable', 'val': is_tradable(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'is_dropable', 'val': is_dropable(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'is_sellable', 'val': is_sellable(item_id)})
                ET.SubElement(new_sk_el, 'set', {'name': 'is_stackable', 'val': is_stackable(item_id)})
                if get_weight(item_id) > 0:
                    ET.SubElement(new_sk_el, 'set', {'name': 'weight', 'val': get_weight(item_id)})

        ET.indent(root, space="\t")
        print(ET.dump(root))
        with open(filepath, 'wb') as fh:
            fh.write(ET.tostring(root, encoding='utf-8', xml_declaration=True))

def compare_weapon_types_with_datapack():
    parse_datapack_items()
    check_missing_items()
    handle_missing()

parse_item_names()
parse_weapons()
parse_armor()
parse_etc()

compare_weapon_types_with_datapack()