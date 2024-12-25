parse_data = open("npc_string_localisation.txt", 'w+', encoding='utf8')

xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
list_element = "<list xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"../../xsd/localisations.xsd\">"
list_end_element = "</list>"

with open('NpcString_Classic-ru.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    parse_data.write(xml_header + "\n")
    parse_data.write(list_element + "\n")
    for line in lines:
        split = line.split('\t')
        string_id = split[1].split('=')[1]
        string_val = split[2][8:-1].replace("\"", "").replace("&", "&amp;")
        string_val = string_val.replace("<", "&lt;").replace(">", "&gt;")
        
        formatted_string = f"\t<localisation id=\"{string_id}\" translation=\"{string_val}\" />\n"
        parse_data.write(formatted_string)
    parse_data.write(list_end_element)
