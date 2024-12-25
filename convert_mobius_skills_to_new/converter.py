import re
from textwrap import indent
from lxml import etree as ET
import os

input_skills = dict()

def read_file(file_path):
    tree = ET.parse(source=file_path, parser=ET.XMLParser(recover=True, encoding='utf-8'))
    root = tree.getroot()
    skills = root.findall('skill')
    for skill in skills:
        skill_id = skill.get('id')
        input_skills[skill_id] = skill
    print('Read file successfully, loaded %d skills' % len(input_skills))
    return tree
    


def reformat_element(element: ET.Element):
    skill_name = element.get('name')
    skill_id = element.get('id')
    max_level = element.get('toLevel')
    key_values = dict()
    for child in element.getchildren():
        key_values[child.tag] = child.text
    
    new_skill = ET.Element('skill')
    new_skill.set('id', skill_id)
    new_skill.set('name', skill_name)
    new_skill.set('levels', max_level)
    
    for key, value in key_values.items():
        if skill_id in element_collections and key in element_collections[skill_id]:
            value = " ".join([f"{child.tag}={child.text}" for child in element_collections[skill_id][key]])
        ET.SubElement(new_skill, 'set', {'name':key, 'value':value.strip()})
    return new_skill

for skill_id, skill in input_skills.items():
    name = skill.get('name')
    data = {
        'name': name,
        'value': skill.get('value'),
        'description': skill.find('description').text
    }
    # print('Processing Skill ID: %s' % skill_id, name)
    # print(ET.tostring(reformat_element(skill), pretty_print=True, element_or_tree='skill').decode('utf-8'))


collect_tags = ['castRange', 'effectPoint', 'set', 'requirement']
element_collections = dict()

if not os.path.exists('./out'):
    os.makedirs('./out')
with os.scandir('.') as entries, open('./out/output.xml', 'wb') as output_file:
    for entry in entries:
        if entry.is_file() and not 'output.xml' in entry.name and entry.name.endswith('.xml'):
            element_tree = read_file(entry.path)
            root = element_tree.getroot()
            for skill in root.findall('skill'):
                skill_id = skill.get('id')
                name = skill.get('name')
                max_level = skill.get('toLevel')
                print('Processing Skill ID: %s' % skill_id, name)
                # iterate over each skills children elements
                elements = skill.getchildren()
                for element in elements:
                    print(element.tag, element.text)
                    # recursively iterate over each element's children
                    children = element.getchildren()
                    indent = 0
                    element_collections.setdefault(skill_id, dict().setdefault(element.tag, []))
                    while len(children) > 0:
                        for child in children:
                            if child.tag == 'effect':
                                effect_name = child.get('name')
                                effect_value = child.get('value')
                                print(f'\t{child.tag} {effect_name} {effect_value}')
                            else:
                                indent_str = "" if indent == 0 else "\t"*indent
                                print(f'{indent_str}', f"LV={child.get('level', None)}", child.tag, child.text)
                            children = child.getchildren()
                        indent += 1
                ET.dump(reformat_element(skill), pretty_print=True)

                    
