import os
import re
from xml.etree import ElementTree as ET

# Define skill types
TYPES = [
    "NONE",
    "BUFF_SKILL",
    "SEQUENTIAL_SKILL",
    "PRIORITY_BUFF_SKILL",
    "NONE",
    "NONE",
    "NONE",
]

# Initialize dictionary to store skill auto use types
skill_auto_types = {}

# Read the text file and extract skill ID and auto_use_type
with open("Skillgrp_ClassicAden.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        skill_id = re.search(r"\bid=(\d+).", line).group(1)
        auto_use_type = re.search(r"\bauto_use_type=(\d+).", line).group(1)
        if skill_id and auto_use_type:
            auto_use_type = TYPES[int(auto_use_type)]
            skill_auto_types[skill_id] = auto_use_type

# Print loaded skill count
print("Loaded {} skills".format(len(skill_auto_types)))

# Check for specific skill
if "1040" in skill_auto_types.keys():
    print("Skill 1040 is {}".format(skill_auto_types["1040"]))

# Change to the desired directory
os.chdir("../../")
path = os.path.abspath("./dist/game/data/stats/skills")

# Iterate over XML files in the directory
for filename in os.listdir(path):
    if filename.endswith(".xml"):
        try:
            tree = ET.parse(
                os.path.join(path, filename),
                parser=ET.XMLParser(encoding="utf-8", target=ET.TreeBuilder(insert_comments=True))
            )
        except ET.ParseError as e:
            print(f"Error parsing {filename}: {e}")
            continue  # Skip this file and continue with the next one

        root = tree.getroot()

        # Process each skill in the XML
        for skill in root.findall("skill"):
            skill_id = skill.attrib["id"]  # Keep as string for consistency with skill_auto_types keys

            # Check if the skill ID is in the skill_auto_types dictionary and it's not "NONE"
            if skill_id in skill_auto_types.keys() and skill_auto_types[skill_id] != "NONE":
                auto_use_type = skill_auto_types[skill_id]

                # Find the 'operateType' element
                operate_type = skill.find("operateType")

                # Check if the skill already has an autoUseType element
                if skill.find("autoUseType") is None and operate_type is not None:
                    # Create and insert the new autoUseType element after operateType
                    new_auto_use = ET.Element("autoUseType")
                    new_auto_use.text = auto_use_type
                    new_auto_use.tail = "\n\t\t"

                    # Find the position of operateType and insert after it
                    index = list(skill).index(operate_type)
                    skill.insert(index + 1, new_auto_use) # галава ебать гптшная

        # Save the modified XML file
        print(f"Saving changes to {os.path.join(path, filename)}")
        tree.write(
            os.path.join(path, filename),
            encoding="utf-8",
            xml_declaration=True,
            method="xml",
        )
