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

items = dict()
# scan through current directory and read all .txt files
# for each file, read the lines and create a class with the name of the file
# Scan through the current directory and read all .txt files
for path in os.scandir('./'):
    if path.path.endswith('.txt') and path.is_file():
        print(f'Processing {path.name}')
        with open(path, 'r', encoding='utf8') as f:
            class_name, class_attrs = file_to_class(path.name)
            Instance = create_class(class_name, class_attrs)
            line =  f.readline()
            attrs = split_by_tabs(line)
            instance = Instance(**dict(attrs))
            if instance:
                items.setdefault(instance.object_id, instance)





