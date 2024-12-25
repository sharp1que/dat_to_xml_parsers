import re
from xml.etree import ElementTree as ET
from typing import NamedTuple


class RewardType(tuple):
    BASE = 0
    KEY = 1
    SPECIAL = 2
    EXTRA = 3
    UNKNOWN = 4

    def __repr__(self) -> str:
        return self.get_name(self)

    @staticmethod
    def get_name(reward_type):
        if reward_type == RewardType.BASE:
            return "Base"
        elif reward_type == RewardType.KEY:
            return "Key"
        elif reward_type == RewardType.SPECIAL:
            return "Special"
        elif reward_type == RewardType.EXTRA:
            return "Extra"
        elif reward_type == RewardType.UNKNOWN:
            return "Unknown"
        else:
            return "Error"


class MissionLevelRewardHolder(NamedTuple):
    season_date: str
    item_id: str
    item_count: str
    reward_type: int
    at_level: int

    # Hash calculation
    def __hash__(self):
        return (
            hash(self.season_date)
            + hash(self.item_id)
            + hash(self.item_count)
            + hash(self.reward_type)
            + hash(self.at_level)
        )

    def __str__(self):
        return f"[{self.season_date}] Item ID: {self.item_id}, Item Count: {self.item_count}, Reward Type: {RewardType.get_name(self.reward_type)}, At Level: {self.at_level}"


mission_levels = dict()
mission_rewards_by_level = dict()
item_names = dict()
reward_pattern = r"u?\{(\d+);(\d+);(\d+)\}"


def parse_item_names():
    with open("./ItemName_ClassicAden-ru.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split("\t")
            item_names.setdefault(data[1].split("=")[1], data[2].split("=")[1][1:-1])
    print(f"Item names parsed: {len(item_names)}")


def parse_mission_levels():
    with open("./MissionLevel_ClassicAden.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split("\t")
            season_date = data[1].split("=")[1]
            limit_lvl = data[2].split("=")[1]
            base_reward = parse_reward(data[5].split("=")[1][1:-1])
            key_reward = parse_reward(data[6].split("=")[1][1:-1])
            # pprint(key_reward)
            special_reward = parse_reward(data[7].split("=")[1])
            extra_reward = parse_reward(data[8].split("=")[1])

            if season_date not in mission_rewards_by_level:
                mission_rewards_by_level[season_date] = dict()

            for base_level in base_reward:
                holder = MissionLevelRewardHolder(
                    season_date=season_date,
                    item_id=base_reward[base_level][0],
                    item_count=base_reward[base_level][1],
                    reward_type=RewardType.BASE,
                    at_level=base_level,
                )
                mission_rewards_by_level.get(season_date, dict())[
                    str(holder.__hash__())
                ] = holder

            print(f"Key reward: {key_reward}")
            for key_level in key_reward:
                holder = MissionLevelRewardHolder(
                    season_date=season_date,
                    item_id=key_reward[key_level][0],
                    item_count=key_reward[key_level][1],
                    reward_type=RewardType.KEY,
                    at_level=key_level,
                )
                mission_rewards_by_level.get(season_date, dict())[
                    str(holder.__hash__())
                ] = holder

            holder = MissionLevelRewardHolder(
                season_date=season_date,
                item_id=special_reward["0"][0],
                item_count=special_reward["0"][1],
                reward_type=RewardType.SPECIAL,
                at_level=limit_lvl,
            )
            mission_rewards_by_level.get(season_date, dict())[
                str(holder.__hash__())
            ] = holder

            holder = MissionLevelRewardHolder(
                season_date=season_date,
                item_id=extra_reward["0"][0],
                item_count=extra_reward["0"][1],
                reward_type=RewardType.EXTRA,
                at_level=limit_lvl,
            )
            mission_rewards_by_level.get(season_date, dict())[
                str(holder.__hash__())
            ] = holder

    # print(f"Mission levels parsed: {len(mission_levels)}")
    print(f"Mission rewards parsed: {len(mission_rewards_by_level)}")
    # pprint(mission_rewards_by_level)


def parse_reward(data):
    reward_list = dict()
    for match in re.finditer(reward_pattern, data):
        reward_list[match.group(1)] = [match.group(2), match.group(3)]
    return reward_list


def write_to_xml():
    list_elem = ET.Element("list")
    tree = ET.ElementTree(list_elem)
    root = tree.getroot()
    for season_date in mission_rewards_by_level.keys():
        mission_element = ET.SubElement(root, "missionLevel")
        mission_element.set("season", season_date)
        mission_element.set("maxLevel", "30")
        mission_element.set("skipCoinPrice", "1000")
        mission_element.set("bonusRewardIsAvailable", "true")
        mission_element.set("bonusRewardByLevelUP", "true")
        # Base rewards
        base_reward_element = ET.SubElement(mission_element, "rewardList")

        print(f"Processing rewards for season {season_date}")
        for i, hash_key in enumerate(
            sorted(
                mission_rewards_by_level[season_date].keys(),
                key=lambda x: int(mission_rewards_by_level[season_date][x].at_level),
            )
        ):
            mission_data = mission_rewards_by_level[season_date][hash_key]
            print(
                f"Processing rewards for mission_data {mission_data} ({mission_data.__hash__()})"
            )
            reward_element = ET.SubElement(base_reward_element, "reward")
            reward_element.set("forLevel", mission_data.at_level)
            reward_element.set(
                "rewardType", RewardType.get_name(mission_data.reward_type).upper()
            )
            reward_element.set("rewardId", mission_data.item_id)
            reward_element.set("rewardCnt", mission_data.item_count)
            tail_text = (
                "\n\t\t"
                if i == len(mission_rewards_by_level[season_date].keys()) - 1
                else "\n\t\t\t"
            )
            reward_element.tail = ET.Comment(
                text="\t<!-- %s -->%s" % (item_names[mission_data.item_id], tail_text)
            ).text

    ET.indent(root, space="\t")
    stri = ET.tostring(
        # encoding="UTF-8",
        xml_declaration=True,
        method="xml",
        encoding="UTF-8",
        element=root,
    )
    ff = open("MissionLevel.xml", mode="wb+")
    ff.write(stri)
    ff.close()
    # tree.write("MissionLevel.xml", encoding="UTF-8", xml_declaration=True)


if __name__ == "__main__":
    parse_item_names()
    parse_mission_levels()
    write_to_xml()
