import os
import re
import shutil
from xml.etree import ElementTree as ET

from class_generator.base import AbstractItemInfo
from class_generator.generated_classes import Armorgrp, EtcItemgrp, ItemName, Weapongrp

items: dict[str, AbstractItemInfo] = dict()
names: dict[str, ItemName] = dict()
descs: dict[str, str] = dict()

def parse_items():
    parse_names()
    parse_weapons()
    parse_armor()
    parse_etc()

def get_item_type(item_id: str) -> str:
    if item_id in items:
        return items[item_id].get_item_type()
    return "NONE"

def get_name(item_id: str) -> str:
    if item_id in names:
        return names[item_id].name[1:-1]
    return None

def get_description(item_id: str) -> str:
    if item_id in descs:
        desc = descs[item_id]
        desc = desc.replace('--', '-')
        return desc
    return None

def get_item_tags(item_id: str) -> str:
    if item_id in items:
        return items[item_id].get_class_type()
    return "NONE"

def get_itemtype_key(item_id: str) -> str:
    if item_id in items:
        if items[item_id].get_class_type() == 'Armor':
            return 'armor_type'
        if items[item_id].get_class_type() == 'Weapon':
            return 'weapon_type'
    return "etcitem_type"

def parse_names():
    with open('ItemName_ClassicAden-eu.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('--', '-')
            desc = re.search(r'description=\[(.*?)\]\t', line)
            name = ItemName.from_string(line)
            names.setdefault(name.id, name)
            if desc:
                descs.setdefault(name.id, desc.group(1))

def parse_weapons():
    with open('Weapongrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            weapon = Weapongrp.from_string(line)
            items.setdefault(weapon.object_id, weapon)

def parse_armor():
    with open('Armorgrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            armor = Armorgrp.from_string(line)
            items.setdefault(armor.object_id, armor)

def parse_etc():
    with open('EtcItemgrp_ClassicAden.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            etc = EtcItemgrp.from_string(line)
            items.setdefault(etc.object_id, etc)

def generate_file_name(item_id: str) -> str:
    return f'{int(item_id) // 100 * 100 + 1}-{int(item_id) // 100 * 100 + 99}' + '.xml'


def fix_item_type():
    shutil.rmtree('./out/', ignore_errors=True)
    os.makedirs('./out/')
    for dir, _, files in os.walk('D:/Projects/Essence/dist/game/data/stats/items'):
        for filename in files:
            if filename.endswith('.xml'):
                print(f"Processing {filename}")
                file_path = os.path.join(dir, filename)
                tree = ET.parse(file_path)
                root = tree.getroot()
                ET.indent(root, space="\t")
                for item_element in root.findall('item'):
                    item_id = item_element.get('id')
                    item_desc = get_description(item_id)

                    # Remove existing <set> elements with specified names
                    for set_name in ['armor_type', 'weapon_type', 'etcitem_type']:
                        for set_element in item_element.findall(f'set[@name="{set_name}"]'):
                            item_element.remove(set_element)

                    # Add new <set> element based on the item type
                    item_type_key = get_itemtype_key(item_id)
                    item_type_value = get_item_type(item_id).upper()
                    new_set_element = ET.Element('set', name=item_type_key, val=item_type_value)
                    item_element.insert(2, new_set_element)

                    if item_desc:
                        comment = ET.Comment(f' {item_desc} ')
                        comment.tail = '\n\t\t'
                        item_element.insert(0, comment)
                ET.indent(root, space="\t")
                tree.write(f'./out/{filename}', encoding='utf-8', xml_declaration=True)

parse_items()
fix_item_type()