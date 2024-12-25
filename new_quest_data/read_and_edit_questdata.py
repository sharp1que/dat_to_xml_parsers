import re
import lxml.etree as ET

def extract_quest_data(file_path):
    """Extracts quest data from the specified file."""
    quests = []
    with open(file_path, "r", encoding="utf-8") as openFile:
        for line in openFile:
            quest_data = {}
            for pair in line.strip().split("\t")[1:-1]:
                if "=" in pair:
                    key, value = pair.split("=", 1)
                    if len(value) > 2 and value.startswith("{") and value.endswith("}"):
                        value = re.findall(r"\{([^}]+)\}", value)[0].split(";")
                        if key == "quest_level":
                            value = tuple(map(int, value))
                    elif value.isdigit():
                        value = int(value)
                    quest_data[key] = value
            quests.append(quest_data)
    return quests


def update_quest_goals(root, goal_data):
    """Updates goal strings and counts in the XML tree."""
    for quest in root.iter("quest"):
        quest_id = int(quest.get("id"))
        if quest_id not in goal_data:
            continue

        goals_elem = quest.find("goals")
        if goals_elem is None:
            continue

        quest_nums_param = goals_elem.find("param[@name='goalCount']")
        quest_str_param = goals_elem.find("param[@name='goalString']")

        if quest_nums_param is not None and quest_str_param is not None:
            new_nums = goal_data[quest_id]["goal_num"]
            new_str = goal_data[quest_id]["goal_string"]

            if int(quest_nums_param.text) != new_nums:
                quest_nums_param.text = str(new_nums)
                print(
                    f"Editing quest[{quest_id}]({new_str}): "
                    f"goalNums set to {new_nums} (previously was {quest_nums_param.text})"
                )


# Example usage
quests = extract_quest_data("./NewQuestData_ClassicAden-eu.txt")
print(f"Loaded {len(quests)} client quests.")

# Create a dictionary indexed by quest_id for efficient lookup
goal_data = {
    quest["quest_id"]: {
        "goal_string": quest["goal_string"],
        "goal_num": quest["goal_num"],
    }
    for quest in quests
}

tree = ET.parse("../../dist/game/data/NewQuestData.xml")
root = tree.getroot()
print(f"Loaded {len(root.findall('quest'))} server quests.")

update_quest_goals(root, goal_data)

tree.write(
    "NewQuestData.xml.generated",
    pretty_print=True,
    encoding="utf-8",
    xml_declaration='<?xml version="1.0" encoding="UTF-8"?>',
)
