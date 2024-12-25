import re
with open('ready_spawn.txt', 'a', encoding='utf8') as out:
    npc_names = dict()
    spawns = dict[str]()

    with open('npcdata.txt', 'r', encoding='utf-16-le') as n:
        n_lines = n.readlines()
        for line in n_lines:
            data = line.split('\t')
            if data[0] == 'npc_begin':
                n_npc_id = data[2]
                n_npc_name = data[3][1:-1]
                npc_names[n_npc_name.lower()] = n_npc_id
        print('Loaded {} npc names'.format(len(npc_names)))

    with open('fort_npcs.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            # Parse Territories
            data = line.split("\t")
            pos_type = data[0]
            if pos_type == 'territory_begin':
                territory_name = data[1][1:-1]
                spawns[territory_name] = list[str]()
                out.write(f'\n\t\t\t\t<!-- {territory_name} -->\n\n')
            elif pos_type == 'npc_ex_begin':
                monster_name = data[1][1:-1]
                pos = data[2][5:-1]
                if not pos.__contains__('ere'):
                    pos_list = pos.split(";")

                    x = pos_list[0]
                    y = pos_list[1]
                    z = pos_list[2]
                    heading = pos_list[3]

                    total = data[3][6:]
                    respawn = data[4][8:]
                    rand_respawn = data[5][13:]
                    has_random = rand_respawn.__contains__('sec')
                    ai_params = data[6][15:-1] if has_random else rand_respawn
                    params_dict = dict[str]()
                    for param in ai_params.split(";"):
                        match = re.match(r'\[(.*?)]=(\d+)', param)
                        if match:
                            param_name = match.group(1)
                            param_value = match.group(2)
                            params_dict[param_name] = param_value
                    if has_random:
                        out.write(f'\t\t\t\t<npc id="{npc_names[monster_name.lower()]}" x="{x}" y="{y}" z="{z}" heading="{heading}" count="{total}" respawnTime="{respawn}" respawnRandom="{rand_respawn}" >\n')
                    else:
                        out.write(f'\t\t\t\t<npc id="{npc_names[monster_name.lower()]}" x="{x}" y="{y}" z="{z}" heading="{heading}" count="{total}" respawnTime="{respawn}" >\n')

                    out.write('\t\t\t\t\t<parameters>\n')
                    for param in params_dict:
                        out.write(f'\t\t\t\t\t\t<param name="{param}" value="{params_dict[param]}" />\n')
                    out.write('\t\t\t\t\t</parameters>\n')
                    out.write('\t\t\t\t</npc>\n')
