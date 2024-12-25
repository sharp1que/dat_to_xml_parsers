begin = 'pet_skill_acquire_begin'
end = 'pet_skill_acquire_end'

item_names = {}
skill_names = {}

with open('SkillName_ClassicAden.txt', 'r', encoding='utf8') as ss:
    lines = ss.readlines()
    for line in lines:
        data = line.split('\t')
        data_type = data[0]
        if data_type == 'skill_begin':
            skill_name = data[1][9:]
            skill_id = data[4][6:-1]
            skill_add_name = data[5][6:-1]
            # print(skill_id, skill_name)
            skill_names[skill_id] = skill_name

with open('Itemdata.txt', 'r', encoding='utf-16-le') as it:
    lines = it.readlines()
    for line in lines:
        if len(line.split('\t')) == 0:
            continue

        data = line.split('\t')
        data_type = data[0]
        if data_type == 'item_begin':
            item_id = data[2]
            name = data[3][1:-1]
            item_names[name] = item_id
            # print(item_id, name)

with open('AcquirePetSkills.txt', 'r', encoding='utf-16-le') as f:
    pet_index = 0
    lines = f.readlines()
    with open('PetAcquireList.xml', 'w', encoding='utf-8') as w:
        w.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        w.write('<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="xsd/PetAcquireList.xsd">\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('//') or line.strip().__len__() == 0:
                continue
            line = line.strip()
            data = line.split(' ')
            data_type = str(data[0].strip())
            if data_type == begin:
                pet_index = 0
            if data_type == 'pet_index':
                pet_index = data[2]
                w.write(f'<pet type="{pet_index}" >\n')
            if data_type == 'pet_skill_begin':
                skill_data = data[1][10:]
                skill_id = skill_data[1:-1].split(',')[0]
                skill_lvl = skill_data[1:-1].split(",")[1]
                auto_get = data[2][13:]
                pet_lvl = data[3][7:]
                pet_evolve_lv = data[4][14:]
                pet_cost = data[5][9:]
                item_id = pet_cost[1:-1]
                if item_id != "":
                    item_data = item_id[1:-1].split(';')
                    item_id = item_data[0][1:-1]
                    item_count = item_data[1]
                    # print(item_id, item_count)
                    item_id_number = 57 if item_id == 'adena' else item_names[item_id]
                    w.write(
                        f'\t<skill id="{skill_id}" lvl="{skill_lvl}" isAutoGet="{auto_get}" reqLvl="{pet_lvl}" evolve="{pet_evolve_lv}" item="{item_id_number}" itemAmount="{item_count}" />\n')
                else:
                    w.write(
                        f'\t<skill id="{skill_id}" lvl="{skill_lvl}" isAutoGet="{auto_get}" reqLvl="{pet_lvl}" evolve="{pet_evolve_lv}" />\n')
                # print(skill_name, auto_get, pet_lvl, pet_evolve_lv, pet_cost)
            if data_type == end:
                w.write(f'</pet>\n')
        w.write('</list>')
