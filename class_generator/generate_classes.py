import re
import os

UNPACKED_DIR_FULL_PATH = 'D:/GameClients/502/system/eu/unpacked'

class_definitions = list()

base_imports = """
from class_generator.base import *
from class_generator.generated_classes import *
"""

grp_class_template = """
class {class_name}(AbstractItemInfo):

    def __init__(self, {init_params}):
        super().__init__(object_id)
        {init_body}
123
    @classmethod
    def from_string(cls, line) -> '{class_name}':
        split_params = line.split('\\t')[1:-1]
        attributes = [{attr}]
        data = {{attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}}
        return cls({from_dict_params})
    
    def __str__(self):
        return f"{class_name}({str_params})"
"""

class_template = """
class {class_name}(object):

    def __init__(self, {init_params}):
        {init_body}

    @classmethod
    def from_string(self, line) -> '{class_name}':
        split_params = line.split('\\t')[1:-1]
        attributes = [{attr}]
        data = {{attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}}
        return self({from_dict_params})
    
    def __str__(self):
        return f"{class_name}({str_params})"
"""

def fix_attr_name(attr_name):
    if attr_name == 'class':
        return 'clazz'
    return attr_name

def generate_class(class_name, attributes) -> str:
    class_name = class_name.replace('-eu', '')
    template = grp_class_template if class_name.lower().endswith("grp") else class_template
    init_params = ", ".join(fix_attr_name(attr) for attr in attributes)
    init_body = "\n        ".join([f"self.{fix_attr_name(attr)} = {fix_attr_name(attr)}" for attr in attributes])
    from_dict_params = ", ".join([f"data.get('{fix_attr_name(attr)}')" for attr in attributes])
    str_params = ", ".join(["%s={self.%s}" % (fix_attr_name(attr), fix_attr_name(attr)) for attr in attributes])
    attr = ", ".join([f"'{fix_attr_name(attr)}'" for attr in attributes])
    return template.format(class_name=class_name, init_params=init_params, init_body=init_body, from_dict_params=from_dict_params,  str_params=str_params, attr=attr)

def parse_data_types(data):
    pattern = re.compile(r'(\w+)=\{?([^\t]*)\}?')
    matches = pattern.findall(data)
    attributes = [key for key, value in matches]
    return attributes

def ucfirst(string):
    if len(string) == 0:
        return string
    return string[0].upper() + string[1:]

def generate_class_from_file(file_path, file_name) -> str:
    with open(file_path, 'r', encoding='utf8') as text_file:
        for line in text_file:
            result = re.search(r'(\w+)_begin', line)
            if result:
                class_name = ucfirst(file_name.replace('.txt', ''))
                attributes = parse_data_types(line)
                if len(attributes) == 0:
                    exception_message = f'No attributes found for class {class_name} in file {file_path}'
                    print(exception_message)
                    return generate_class(class_name, ['error'])
                return generate_class(class_name, attributes)
    return "Error"

def file_name_to_class_name(file_name) -> str:
    # replace all underscores with spaces
    all_words = file_name.split('_')
    all_except_last = all_words[:-1] if len(all_words) > 1 else all_words 
    # capitalize each word
    return "".join([ucfirst(word) for word in all_except_last])

# Example usage
with open('generated_classes.py', 'w', encoding='utf8') as f:
    f.write(base_imports + "\n")
    for root, dirs, files in os.walk(UNPACKED_DIR_FULL_PATH):
        for file in files:
            if file.endswith('txt') and file_name_to_class_name(file) not in class_definitions:
                file_path = os.path.join(root, file)
                class_name_from_file = file.replace('.txt', '')
                class_name_from_file = file_name_to_class_name(class_name_from_file)
                class_def:str = generate_class_from_file(file_path, class_name_from_file)
                class_definitions.append(class_name_from_file)
                print(f'Generated class {class_name_from_file} from file {file_path}')
                f.write(class_def)
                f.write('\n\n')

