parse_data = open("npc_name_localisation.txt", 'w+', encoding='utf8')

with open('npc_name.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        split = line.split('\t')
        npc_id = split[1].split('=')[1]
        npc_name = split[2].split('=')[1].replace('[', '').replace("]", "")
        npc_title = split[3].split('=')[1].replace('[', '').replace(']', '')
        
        formatted_string = f"<localisation id=\"{npc_id}\" name=\"{npc_name}\" title=\"{npc_title}\" />\n"
        parse_data.write(formatted_string)
        print(formatted_string)
    