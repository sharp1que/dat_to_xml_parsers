import re
import xml.etree.ElementTree as ET

auto_use_pattern = r"u?automatic_use=([0-9]+)"
id_pattern = r"u?id=(\d+)"
category_pattern = r"u?category=(.*?)"
category_params = r"u?category2=(.*?)\t"
cmd_pattern = r"u?cmd=\[(.*?)\]"
icon_pattern = r"u?icon=(.*?)\t"
name_pattern = r"u?name=\[(.*?)\]"
toggle_group_id_pattern = r"u?toggle_group_id=(\d+)"
desc_pattern = r"u?desc=\[(.*?)\]"

actions = dict()

with open("ActionName_ClassicAden-e.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        data = line.strip().split("\t")
        actionId = data[1].split("=")[1]
        actionType = data[2].split("=")[1]
        actionCategory = data[3].split("=")[1].upper().replace(" ", "_")
        categoryParams = data[4].split("=")[1][1:-1]
        actionCmd = data[5].split("=")[1][1:-1]
        actionIcon = data[6].split("=")[1][1:-1]
        actionIconEx = data[7].split("=")[1][1:-1]
        actionDescription = " ".join(data[8].split("=")[1][1:-1].split("\\n\\n"))
        actionGroupId = data[9].split("=")[1]
        actionAutoUse = data[10].split("=")[1]
        actionHandler = data[11].split("=")[1][1:-1].upper()

        actions[actionId] = {
            "actionType": actionType,
            "actionCategory": actionCategory,
            "categoryParams": categoryParams,
            "actionCmd": actionCmd,
            "actionIcon": actionIcon,
            "actionDescription": actionDescription,
            "actionGroupId": actionGroupId,
            "actionAutoUse": actionAutoUse,
            "actionHandler": actionHandler,
        }

sorted_actions = {k: actions[k] for k in sorted(actions, key=int)}

# Print sorted actions
for actionId, actionData in sorted_actions.items():
    autoUse = " autoUse=\"1\"" if actionData["actionAutoUse"] == "1" else ""
    print(
        f"\t<!-- {actionData['actionCmd']} -->\n",
        f"\t<action id=\"{actionId}\" handler=\"{actionData['actionHandler']}\" options=\"{actionData["categoryParams"]}\"{autoUse} /> <!-- {actionData['actionDescription']} -->\n",
        # actionData["actionType"],
        # actionData["actionCategory"],
        # actionData["categoryParams"],
        # actionData["actionCmd"],
        # actionData["actionIcon"],
        # actionData["actionDescription"],
        # actionData["actionGroupId"],
        # f"autoUse={actionData["actionAutoUse"]}",
        # actionData["actionHandler"],
    )

    # Create the root element of the XML tree
    root = ET.Element("list")

    # Iterate over the actions and add them to the XML tree
    for actionId, actionData in sorted_actions.items():
        actionElement = ET.SubElement(root, "action", id=actionId, handler=actionData["actionHandler"], options=actionData["categoryParams"], autoUse=actionData["actionAutoUse"])
        actionElement.text = ET.Comment(text={actionData['actionCmd']})
        actionElement.tail = ET.Comment(text={actionData['actionDescription']})

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Write the XML tree to a file
    tree.write("ActionData2.xml", encoding="utf8", xml_declaration=True, short_empty_elements=False)
