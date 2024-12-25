import re
from lxml import etree as ET
from lxml import objectify

ptrn = r"u?automatic_use=([0-9]+)"
auto_usable_actions = []
action_data = dict()

with open("actions.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        data = line.strip().split("\t")

        actionId = data[1].split("=")[1]
        options = data[4].split("=")[1][1:-1]
        command = data[5].split("=")[1][1:-1]
        autoUseType = int(re.search(ptrn, line).group(1))

        action_data.setdefault(actionId, [options, command, autoUseType])
        if autoUseType == 1:
            auto_usable_actions.append(
                actionId,
            )
            # print(actionId, autoUseType)

parser = ET.XMLParser(
    remove_comments=True, remove_blank_text=True, resolve_entities=False
)
tree = ET.parse("ActionData.xml", parser=parser)

root = tree.getroot()
objectify.deannotate(root, cleanup_namespaces=True)
# find all actions with id in auto_usable_actions
for action in root.findall("action"):
    if action.get("id") in auto_usable_actions:
        action.set("autoUse", "1")
    comment_text = (
        "Deleted"
        if action.get("id") not in action_data
        else action_data[action.get("id")][1]
    )
    action.tail = f" <!-- {comment_text} -->\n\t"

ET.indent(root, space="\t")


# write to file
tree.write(
    "ActionData.xml",
    encoding="utf8",
    xml_declaration=True,
)
