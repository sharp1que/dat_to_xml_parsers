import os
from pathlib import Path
import xml.etree.ElementTree as ET
import shutil

from class_generator.generated_classes import SkillName, Skillgrp, SkillAcquire

class Info:
    def __init__(self, skill_id, skill_level, name):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.name = name[1:-1]


skills_grps: dict[str, dict[str, Skillgrp]] = {}
skill_names: dict[str, dict[str, SkillName]] = {}
datapack_skills: dict[str, dict[str, Info]] = {}

ignored_params = [
    'skill_begin', 'skill_end', 'class_type', 'object_id', 'sublevel', 'icon_type'
    ''              
                  ]

only_if_gtzero = ['mp_consume', 'hp_consume', 'cast_range', 'cool_time', 'skill_hit_time', 'skill_cool_time', 'skill_hit_cancel_time', 'skill_fly_time', 'skill_cool_time', 'skill_hit_time']

diff = []
missing = []
skill_filenames = {}

op_type_replacement = {
    "instant": "A1",
    "duration": "A2",
    "duration_level_up": "A3",
    "selfduration": "A4",
    "passive": "P",
    "toggle": "T",
    "channelling_instance": "CA1",
    "channelling_duration": "CA2",
    "channelling_duration_level_up": "CA3",
    "charge_instant": "DA1",
    "charge_duration": "DA2",
    "aura": "AU",
    "aura_activity": "AU1",
    "group_toggle": "TG",
    "back_step_instant": "",
    "back_step_duration": "",
    "aura_activity2": "AU2",
    "party_instant": "",
    "dual_pump1": "",
    "race_special_passive": "PR",
    "blink_instant": "DA3",
    "back_step_duration_with_target_knockback": "DA6",
    # Add other entries as needed...
}

def replace_operate_type(text):
    if text in op_type_replacement:
        return op_type_replacement[text]
    return text

def parse_skill_name():
    with open('SkillName_ClassicAden-eu.txt', 'r', encoding='utf8') as input:
        for line in input:
            parts = line.split("\t")
            if parts[0] == 'skill_begin':
                skillname = SkillName.from_string(line)
                if skillname:
                    skill_names.setdefault(skillname.skill_id, {})
                    skill_names[skillname.skill_id][skillname.skill_level] = skillname
    print(f'Loaded {len(skill_names.keys())} skill names')

def parse_skill_grp():
    with open('Skillgrp_ClassicAden.txt', 'r', encoding='utf8') as input:
        for line in input:
            parts = line.split("\t")
            if parts[0] == 'skill_begin':
                skillgrp = Skillgrp.from_string(line)
                if skillgrp:
                    skills_grps.setdefault(skillgrp.id, {})
                    skills_grps[skillgrp.id][skillgrp.level] = skillgrp

    print(f'Loaded {len(skills_grps.values())} skill grps')

def parse_skills():
    parse_skill_name()
    parse_skill_grp()

def add_new_set(root, name, value):
    set = ET.SubElement(root, 'set', {'name': name})
    set.text = value

def parse_datapack_skills():
    for root, _, files in os.walk('../../dist/game/data/stats/skills/'):
        for file in files:
            if file.endswith('.xml'):
                try:
                    tree = ET.parse(os.path.join(root, file))
                    for skill in tree.iterfind('skill'):
                        skill_id = skill.get('id', "0")
                        skill_to_level = int(skill.get('levels', "1"))
                        skill_name = skill.get('name')
                        for i in range(1, skill_to_level + 1):
                            datapack_skills.setdefault(skill_id, {})
                            datapack_skills[skill_id][str(i)] = Info(skill_id, str(i), skill_name)
                        
                        # datapack_skills.setdefault(skill_id, [skill_name, skill_to_level])
                except Exception:
                    pass

def get_skill_name(skill_id, skill_lvl):
    return skill_names[skill_id][skill_lvl].name[1:-1]

def get_skill_icon(skill_id, skill_lvl):
    return skills_grps[skill_id][skill_lvl].icon[1:-1]

def get_skill_operate_type(skill_id, skill_lvl):
    return skills_grps[skill_id][skill_lvl].operate_type

def get_max_skill_lvl_grp(skill_id):
    # last key is in skills_grps[skill_id].keys()[-1]
    return list(skills_grps[skill_id].keys())[-1]

def get_max_skill_lvl(skill_id):
    if skill_id in datapack_skills:
        return list(datapack_skills[skill_id].keys())[-1]
    return -1

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
            params = ['- Need Update', sk_id, skill_names[sk_id]['1'].name,  f'Max DP LVL = {last_lvl} MAX DAT LVL = {last_dat_lvl}\n']
            out.write(' '.join(params))

    with open('missing_skills.txt', 'w', encoding='utf8') as out:
        for sk_id in missing:
            sk_name = get_skill_name(sk_id, '1')
            out.write(f' - Missing skill [{sk_id}][{sk_name}] from DataPack.\n')

def generate_file_name(skill_id):
    lower_bound = (int(skill_id) // 100) * 100
    upper_bound = lower_bound + 99
    return f"{lower_bound}-{upper_bound}.xml"

def handle_missing():
    for sk_id in missing:
        file_name = generate_file_name(skill_id=sk_id)
        skill_filenames.setdefault(file_name, []).append(sk_id)

    for file_name, skill_ids in skill_filenames.items():
        file_path = os.path.join('./out', file_name)
        if not os.path.exists(file_path):
            root = ET.Element('list')
        else:
            tree = ET.parse(file_path)
            root = tree.getroot()

        existing_skill_ids = {skill.get('id') for skill in root.findall('skill')}

        for sk_id in skill_ids:
            if sk_id not in existing_skill_ids:
                skillgrp = skills_grps[sk_id]['1']
                skillname = skill_names[sk_id]['1']
                sk_name = skillname.name[1:-1]
                sk_max_lvl = get_max_skill_lvl_grp(sk_id)
                print(f'Adding missing skill: {sk_id} {sk_name} levels="{sk_max_lvl}"')
                new_sk_el = ET.SubElement(root, 'skill')
                new_sk_el.set('id', sk_id)
                new_sk_el.set('levels', sk_max_lvl)
                new_sk_el.set('name', sk_name)
                
                # for attribute in skillgrp.__dict__.keys():
                #     add_new_set(new_sk_el, attribute, getattr(skillgrp, attribute))
                add_new_set(new_sk_el, 'mp_consume1', skillgrp.mp_consume)
                add_new_set(new_sk_el, 'is_magic', skillgrp.is_magic.upper())
                add_new_set(new_sk_el, 'icon', skillgrp.icon[1:-1])
                add_if_gt_zero(new_sk_el, 'icon_hide', skillgrp.icon_hide)
                
                add_new_set(new_sk_el, 'operate_type', get_skill_operate_type(sk_id, sk_max_lvl))


        ET.indent(root, space="\t")
        if not os.path.exists('./out'):
            os.makedirs('./out')
        with open(file_path, 'wb') as fh:
            fh.write(ET.tostring(root, encoding='utf-8', xml_declaration=True))

parse_skills()
parse_datapack_skills()
check_missing_skills()
handle_missing()