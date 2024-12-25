import json
auto_use_types = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        data = line.split('\t')
        item_id = data[1].split('=')[1]
        auto_use_type = data[2].split('=')[1]
        auto_use_types[item_id] = auto_use_type.upper()
with open('autousetypes.json', 'w', encoding='utf8') as f:
    json.dump(auto_use_types, f, ensure_ascii=False, indent=4)
