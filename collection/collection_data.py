xml_start = '<?xml version="1.0" encoding="UTF-8"?>'
list_start = '<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../xsd/CollectionData.xsd">'
list_end = '</list>'

item_names = dict()

with open('ItemName_ClassicAden-ru.txt', 'r', encoding='utf8') as i:
    i_lines = i.readlines()
    for i_line in i_lines:
        data = i_line.split('\t')
        item_type = data[0]
        if item_type == 'item_name_begin':
            item_id = data[1][3:]
            item_name = data[2][6:-1]
            item_names[item_id] = item_name

    print('Loaded {} item names'.format(len(item_names)))

pass

file_to_parse = 'collection_ClassicAden-ru.txt'

with open('CollectionData.xml', 'a', encoding='utf8') as w:
    w.write(xml_start + '\n')
    w.write(list_start + '\n')
    with open(file_to_parse, 'r', encoding='utf8') as f:
        lines = f.readlines()
    for line in lines:
        data = line.split('\t') # split by tabs
        data_type = data[0]
        # required line to parse
        if data_type == 'collection_begin':
            collection_id = data[1][14:]
            collection_name = data[2][17:-1].replace('Ⅰ', 'I').replace('Ⅱ', 'II').replace('Ⅲ', 'III').replace('Ⅳ', 'IV').replace('Ⅴ', 'V')
            main_category = data[3][14:]
            period = data[4][7:]
            option_id = data[5][10:]
            description = data[6][12:]
            items = data[7][6:]
            is_event = data[8][9:]
            unk5 = data[9][5:]
            complete_item_type = data[10][19:]
            complete_skill_type = data[11][20:]
            w.write(f'\t<!-- {collection_name} -->\n')
            w.write(f'\t<!-- Description: \n')
            # parse desc
            desc_items = description[1:-1].split("};{")
            for desc_item in desc_items:
                fixed_desc = desc_item.replace('{', '').replace('}', '')
                param_name = fixed_desc.split(';')[0]
                param_add_type = 'PER' if fixed_desc.split(';')[1] == '0' else 'ADD'
                param_val = fixed_desc.split(';')[2]
                w.write(f'\t{param_name} {param_add_type} {param_val}\n')
                # print(param_name, param_add_type, param_val)
            w.write(f'\t-->\n')
            if period == '0':
                w.write(f'\t<collection id="{collection_id}" optionId="{option_id}" category="{main_category}">\n')
            else:
                w.write(f'\t<collection id="{collection_id}" period="{period}" optionId="{option_id}" category="{main_category}">\n')
            # parse items
            item_list = items[1:-1].split('};{')
            for item_entry in item_list:
                fixed_item = item_entry.replace('{', '').replace('}', '').split(';')
                item_id = fixed_item[0]
                item_name = item_names[item_id]
                replacement_item_id = fixed_item[1]
                item_count = fixed_item[2]
                enchant_lvl = fixed_item[3]
                is_blessed = fixed_item[4]
                slot = fixed_item[5]
                bless_cond = fixed_item[6]
                w.write(f'\t\t<item id="{item_id}" count="{item_count}" enchant_level="{enchant_lvl}" /> <!-- {item_name} --> \n')
                # print(f'{item_name}[{item_id}]', replacement_item_id, item_count, enchant_lvl, bless_condition, rep_item_count, rep_enchant_lvl)
            w.write(f'\t</collection>\n\n')
            # print(collection_id, collection_name, main_category, period, option_id, description, items, is_event, unk5, complete_item_type, complete_skill_type)
    f.close()
    w.write(list_end + '\n')
    w.close()


