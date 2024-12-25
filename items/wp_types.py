import os
from typing import Any, Dict, List, Tuple
import re
from xml.etree import ElementTree as ET

from weapons import generate_file_name

FILENAME_PATTERN = r'(.*?)(_Classic(Aden)?)?\.txt'
GENERATED_CLASSES = []

# Description: This script reads a file and creates a class with the named from filename and the attributes and methods from the file.
def create_class(name: str, attrs: Dict[str, Any]) -> type:
    def __init__(self, **kwargs: Any) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({", ".join([f"{k}={v}" for k, v in self.__dict__.items()])})'
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({", ".join([f"{k}={v}" for k, v in self.__dict__.items()])})'
    def get(self, key: str) -> Any:
        return getattr(self, key)
    def set(self, key: str, value: Any) -> None:
        setattr(self, key, value)
    def get_attrs(self) -> List[str]:
        return list(self.__dict__.keys())
    def get_methods(self) -> List[str]:
        return [m for m in dir(self) if callable(getattr(self, m)) and not m.startswith("__")]
    attrs.update({
        '__init__': __init__,
        '__str__': __str__,
        '__repr__': __repr__,
        'get': get,
        'set': set,
        'get_attrs': get_attrs,
        'get_methods': get_methods
    })
    return type(name, (object,), attrs)



# split a string by tabs and return a list of strings
# for each element in the list, split by '=' and return a tuple
def split_by_tabs(line):
    return [tuple(i.split('=', 1)) for i in line.split('\t') if '=' in i]


def file_to_class(filename: str) -> tuple[str, dict[Any, Any]]:
    class_name = re.search(FILENAME_PATTERN, filename)
    if class_name:
        return class_name.group(1), {}
    return 'Unknown', {}

weapongrps = dict()


# scan through current directory and read all .txt files
# for each file, read the lines and create a class with the name of the file
# Scan through the current directory and read all .txt files
for line in open('Weapongrp_ClassicAden.txt').readlines():
    class_name, class_attrs = file_to_class("Weapongrp")
    Grp = create_class(class_name, class_attrs)
    attrs = split_by_tabs(line)
    instance = Grp(**dict(attrs))
    if instance:
        weapongrps.setdefault(instance.object_id, instance)

# for each instance in the list of instances, print the instance
for obj_id, item_class in weapongrps.items():
    filename = generate_file_name(obj_id)
    tree = ET.parse(filename)
    root = tree.getroot()
    items = root.findall('item')
    if items:
        for item in items:
            breakpoint()
            instance = weapongrps.get(item.get('id'))
            itemtype = item.get('type')
            if itemtype and itemtype == 'Weapon' and item.get('id') == instance.object_id:
                item.set('weapon_type', str(instance.weapon_type).upper())
            elif itemtype and itemtype == 'Armor' and item.get('id') == instance.object_id:
                item.set('armor_type', str(instance.armor_type).upper())
    ET.indent(root, space="\t")
    ET.dump(root)
    # tree.write(file)
