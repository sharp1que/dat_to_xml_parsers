import os
from pathlib import Path
import xml.etree.ElementTree as ET
import shutil


skills = {}
skills_grps = {}
datapack_skills = {}

diff = []
missing = []


def parse_skill_name():
    with open('SkillName_ClassicAden-eu.txt', 'r', encoding='utf8') as input:
        for line in input.readlines():
            parts = line.split("\t")
            if parts[0] == 'skill_begin':
                id = parts[1].split('=')[1]
                level = parts[2].split('=')[1]
                name = parts[4].split('=')[1][1:-1]
                skills.setdefault(id, {})
                skills[id][level] = [name]
    print(f'Loaded {len(skills.keys())} skill names')


def parse_skill_grp():
    with open('Skillgrp_ClassicAden.txt', 'r', encoding='utf8') as input:
        for line in input.readlines():
            parts = line.split("\t")
            if parts[0] == 'skill_begin':
                skill_id = parts[1].split('=')[1]
                skill_level = parts[2].split('=')[1]
                skills_grps.setdefault(skill_id, {})
                skills_grps[skill_id][skill_level] = {}
                for attributes in [part.split('=') for part in parts[2:-1]]:
                    skills_grps[skill_id][skill_level][attributes[0]
                                                       ] = attributes[1]
    print(f'Loaded {len(skills_grps.values())} skill grps')


def parse_skills():
    parse_skill_name()
    parse_skill_grp()


def parse_datapack_skills():
    for path in os.walk('.'):
        for file in path[2]:
            if '.xml' in file:
                try:
                    root = ET.parse(file)  # <list>
                    for skill in root.iterfind('skill'):
                        skill_id = skill.get('id')
                        skill_name = skill.get('name')
                        skill_to_level = skill.get('toLevel')
                        datapack_skills.setdefault(
                            skill_id, [skill_name, skill_to_level]
                        )
                except Exception as e:
                    pass


def get_skill_name(skill_id, skill_lvl):
    return skills[skill_id][skill_lvl][0]


def get_skill_icon(skill_id, skill_lvl):
    return skills_grps[skill_id][skill_lvl]['icon'][1:-1]


def get_skill_operate_type(skill_id):
    return skills_grps[skill_id]['1']['operate_type']


def get_max_skill_lvl_grp(skill_id):
    return list(skills_grps[skill_id].keys())[-1]


def get_max_skill_lvl(skill_id):
    return datapack_skills[skill_id][1] if skill_id in datapack_skills else -1


def check_missing_skills():

    for skill_id in skills_grps.keys():
        max_grp_lvl = get_max_skill_lvl_grp(skill_id)
        max_skill_lvl = get_max_skill_lvl(skill_id)
        if max_skill_lvl == -1:
            missing.append(skill_id)
        elif max_skill_lvl != max_grp_lvl:
            diff.append(skill_id)

    print(f'Total {len(diff)} skills need update and {len(missing)} missing')

    with open('update_skills.txt', 'w', encoding='utf8') as out:
        for sk_id in diff:
            last_lvl = get_max_skill_lvl(sk_id)
            last_dat_lvl = get_max_skill_lvl_grp(sk_id)
            params = ['- Need Update', sk_id, skills[sk_id]['1'][0],
                      f'Max DP LVL = {last_lvl} MAX DAT LVL = {last_dat_lvl}\n']
            out.write(' '.join(params))

    with open('missing_skills.txt', 'w', encoding='utf8') as out:
        for sk_id in missing:
            sk_name = skills[sk_id]['1'][0]
            out.write(
                f' - Missing skill [{sk_id}][{sk_name}] from DataPack.\n')


def generate_file_name(skill_id):
    lower_bound = (int(skill_id) // 100) * 100
    upper_bound = lower_bound + 99
    return f"{lower_bound}-{upper_bound}.xml"


def handle_missing():
    for sk_id in missing:
        file_name = generate_file_name(sk_id)
        sk_grp_lvl = get_max_skill_lvl_grp(sk_id)
        sk_name = get_skill_name(sk_id, '1')
        try:
            el_tree = ET.parse(file_name)
            root = el_tree.getroot()
            skills = el_tree.findall('skill')
            skill_ids = [skill.get('id') for skill in skills]

            if sk_id not in skill_ids:
                print(f'Adding missing skill: {sk_id} {sk_name}')
                new_sk_el = ET.SubElement(root, 'skill')
                new_sk_el.set('id', sk_id)
                new_sk_el.set('toLevel', sk_grp_lvl)
                new_sk_el.set('name', sk_name)
                icon = ET.SubElement(new_sk_el, 'icon')
                icon.text = get_skill_icon(sk_id, sk_grp_lvl)
                operateType = ET.SubElement(new_sk_el, 'operateType')
                operateType.text = 'A1'
                ET.indent(root, space="\t")
                # Save the modified XML back to the file
                # ET.indent(root, space="\t")
                # ET.dump(root)
                fh = open('./out/{}'.format(file_name), 'wb')
                fh.write(ET.tostring(
                    root, encoding='utf-8', xml_declaration=True))
                root = ET.parse(file_name)
            else:
                print(f'Skill already exists in {file_name}: {sk_id}')

        except Exception as e:
            print(e)
            continue


def add_missing_skills_to_existing_files():
    try:
        shutil.rmtree('./out')
    except Exception as e:
        pass

    os.makedirs('./out')

    for ww in os.walk('.'):
        for file in ww[2]:
            path = Path(file)
            if '.xml' in str(file) and path.exists():
                print(f'{file} exists!')
            else:
                for skill_id in missing:
                    open(generate_file_name(skill_id),
                         'w', encoding='utf8').close()


parse_skills()
parse_datapack_skills()
check_missing_skills()
add_missing_skills_to_existing_files()
