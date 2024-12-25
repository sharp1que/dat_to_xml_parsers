from encodings import utf_8


unavailable = 'Недоступно'
unavailable_item = 'Предмет недоступен.'
sealed = 'Запечатано'
not_used = 'Не используется'
can_not_use = 'использовать данный предмет больше нельзя'
list_start = '<list xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="xsd/ItemAuctionType.xsd">'

item_names = {}
item_types = {}
for x in ["WEAPON", "ETCEQUIPMENT", "ARMOR", "ACCESSARY", "ENCHANTSCROLL", "BLESSENCHANTSCROLL", "SKILLBOOK", "DYE", "SOULCRYSTAL", "VARIATIONSTONE", "ETC_BELT_ENCHANT", "ETCENCHANT", "POTIONANDETCSCROLL", "TICKET", "CRAFT", "ETCSUBTYPE"]:
    item_types[str(x)] = []

def get_enum_type_by_int(auction_type, sort_order):
    if auction_type == 1:
        return "WEAPON" # "WEAPON_SWORD"
    elif auction_type == 2:
        return "WEAPON" # "WEAPON_TWO_HAND_SWORD"
    elif auction_type == 3: 
        return "WEAPON" # "WEAPON_BLUNT"
    elif auction_type == 4: 
        return "WEAPON" # "WEAPON_ONE_HANDED_BLUNT"
    elif auction_type == 5: 
        return "WEAPON" # "WEAPON_MAGIC_BLUNT"
    elif auction_type == 6: 
        return "WEAPON" # "WEAPON_TWO_HANDED_MAGIC_BLUNT"
    elif auction_type == 7: 
        return "WEAPON" # "WEAPON_ETC_WEAPON" # (BOOK)
    elif auction_type == 8: 
        return "WEAPON" # "WEAPON_ANCIENT_SWORD"
    elif auction_type == 9: 
        return "WEAPON" # "WEAPON_DAGGER"
    elif auction_type == 10: 
        return ""
    elif auction_type == 11: 
        return "WEAPON" # "WEAPON_DUAL_SWORD"
    elif auction_type == 12: 
        return "WEAPON" # ""
    elif auction_type == 13: 
        return "WEAPON" # "WEAPON_BOW"
    elif auction_type == 14: 
        return "WEAPON" # "WEAPON_CROSSBOW"
    elif auction_type == 15: 
        return "SKILLBOOK" if sort_order == 31 else "WEAPON" # "WEAPON_SPELL_BOOK"# (sort_order=31) / RAPIER(sort_order=-2)
    elif auction_type == 16: 
        return "WEAPON" # "WEAPON_POLE"
    elif auction_type == 17: 
        return "WEAPON" # "WEAPON_DUALFIST"
    elif auction_type == 18: 
        return "WEAPON" # "WEAPON_SHIELD"
    elif auction_type == 19: 
        return "WEAPON" # "WEAPON_SYMBOL"
    elif auction_type == 20: 
        return "WEAPON" # "WEAPON_PISTOLS"
    elif auction_type == 21: 
        return "ETCEQUIPMENT" # "WEAPON_ARROW"
    elif auction_type == 22: 
        return "ETCEQUIPMENT" # "ARMOR_DOLL"
    elif auction_type == 23: 
        return "ARMOR" # "ARMOR_CHEST"
    elif auction_type == 24: 
        return "ARMOR" # "ARMOR_LEGS"
    elif auction_type == 25: 
        return "ARMOR" # "ARMOR_FULL_CHEST"
    elif auction_type == 26: 
        return "ARMOR" # "ARMOR_FEET"
    elif auction_type == 27: 
        return "ARMOR" # "ARMOR_HEAD"
    elif auction_type == 28: 
        return "ARMOR" # "ARMOR_GLOVES"
    elif auction_type == 29: 
        return "ACCESSARY" # "ACCESSORY_LR_EARRING"
    elif auction_type == 30: 
        return "ACCESSARY" # "ACCESSORY_LR_RING"
    elif auction_type == 31: 
        return "ACCESSARY" # "ACCESSORY_NECKLACE"
    elif auction_type == 32: 
        return "ACCESSARY" # "ACCESSORY_BACK"
    elif auction_type == 33: 
        return "ACCESSARY" # "ACCESSORY_PENDANT"
    elif auction_type == 34: 
        return "ETCEQUIPMENT" # "ACCESSORY_JEWEL"
    elif auction_type == 35: 
        return "ETCEQUIPMENT" # "ACCESSORY_AGHATION"
    elif auction_type == 36: 
        return "ETCEQUIPMENT" # "ACCESSORY_TALISMAN"
    elif auction_type == 37: 
        return "ACCESSARY" # "ACCESSORY_DHAIR"
    elif auction_type == 38: 
        return "ACCESSARY" # "ACCESSORY_BRACELET" # / ACCESSORY_BROOCH
    elif auction_type == 39: 
        return "ACCESSARY" # "ACCESSORY_BELT"
    elif auction_type == 40: 
        return "ENCHANTSCROLL" # "ETC_ENCHANT_SCROLL_WEAPON"
    elif auction_type == 41: 
        return "ENCHANTSCROLL" # "ETC_ENCHANT_SCROLL_ARMOR"
    elif auction_type == 42: 
        return "BLESSENCHANTSCROLL" # "ETC_BLESS_SCROLL"
    elif auction_type == 43: 
        return "SKILLBOOK" # "ETC_SPELL_BOOK"
    elif auction_type == 44: 
        return "DYE" # "ETC_DYE"
    elif auction_type == 45: 
        return "SOULCRYSTAL" # "ETC_SOUL_CRYSTALL"
    elif auction_type == 46: 
        return "VARIATIONSTONE" # "ETC_LIFE_STONE"
    elif auction_type == 47: 
        return "ETCENCHANT" # "ETC_BELT_ENCHANT" # (Заклепка ^)
    elif auction_type == 48: 
        return ""
    elif auction_type == 49: 
        return ""
    elif auction_type == 50: 
        return "ETCENCHANT" # "ETC_ATTRIBUTE_STONE"
    elif auction_type == 51: 
        return ""
    elif auction_type == 52: 
        return ""
    elif auction_type == 53: 
        return "ETCENCHANT" # "ETC_ENCHANT_SUPPORT"
    elif auction_type == 54: 
        return ""
    elif auction_type == 55: 
        return ""
    elif auction_type == 56: 
        return "POTIONANDETCSCROLL" # "ETC_POTION"
    elif auction_type == 57: 
        return "POTIONANDETCSCROLL" # "ETC_BUFF_SCROLL"
    elif auction_type == 58: 
        return "TICKET" # "ETC_COUPON"
    elif auction_type == 59: 
        return "TICKET" # "ETC_INSTANCE_TIME"
    elif auction_type == 60: 
        return "CRAFT" # "ETC_PET_FOOD"
    elif auction_type == 61: 
        return "CRAFT" # "ETC_RECEIPE"
    elif auction_type == 62: 
        return "CRAFT" # "ETC_GEMSTONE" #(sort_order=67) | ETC_L_COIN_BOX(sort_order=-55)
    elif auction_type == 63: 
        return "CRAFT" # "ETC_CRAFT_KEY"
    elif auction_type == 64: 
        return "CRAFT" # "ETC_GRADE_CRYSTALL"
    elif auction_type == 65: 
        return ""
    elif auction_type == 66: 
        return ""
    elif auction_type == 67: 
        return "CRAFT" # "ETC_PACKED_BOX"
    elif auction_type == 68: 
        return "ETCSUBTYPE" # "ETC_OTHER"

with open('ItemName_ClassicAden-ru.txt', encoding='utf8') as f:
    lines = f.readlines()
    unique_types = []
    print(f'Parsing {len(lines)} lines!')
    with open('ItemAuctionType.xml', 'w+', encoding='utf8') as w:
        for line in lines:
            data = line.split("\t")
            item_type = data[0]
            if item_type == 'item_name_begin':
                item_id = int(data[1][3:])
                item_name = str(data[2][6:-1])
                item_additional_name = str(data[3][16:-1])
                item_desc = str(data[4])[13:-1]
                item_is_private_store = int(data[17][17:])
                item_keep_type = int(data[18][10:])
                item_commission_store = int(data[20][20:])
                item_sort_order = int(data[25][11:])
                item_auction_type = int(data[26][11:])

                # skip non-tradeable
                if item_name.lower().endswith(unavailable.lower()) or item_additional_name.lower().endswith(unavailable.lower()):
                    continue
                elif item_desc.lower().__contains__(can_not_use.lower()):
                    continue
                elif item_desc.lower().startswith(unavailable_item.lower()):
                    continue
                elif item_additional_name.lower().endswith(sealed.lower()):
                    continue
                elif item_is_private_store == 0:
                    continue
                elif item_auction_type == 0:
                    continue

                # if item_auction_type != 68: # 0 - not listed (1-68 currently)
                #     continue

                list = item_types[str(get_enum_type_by_int(item_auction_type, item_sort_order))]
                list.append(f'{item_id}|{item_name}')

                print(f'{item_name} [{item_additional_name}] item_is_private_store={item_is_private_store}, item_keep_type={item_keep_type}, item_commission_store={item_commission_store}, item_sort_order={item_sort_order}, item_auction_type={item_auction_type}')
        w.write(list_start + '\n')
        for key, val in item_types.items():
            if (len(val) == 0):
                continue

            # w.write(f'<group id="{key}" type="{key}" >\n')
            w.write(f'<group type="{key}" >\n')
            for id in val:
                item_id_data = id.split('|')[0]
                item_name_data = id.split('|')[1]

                w.write(f'\t<item id="{item_id_data}" /> <!-- {item_name_data} -->\n')
            w.write('</group>\n')
        w.write('</list>')
        w.close()


    # 1 -> WEAPON_SWORD
    # 2 -> WEAPON_TWO_HAND_SWORD
    # 3 -> WEAPON_BLUNT
    # 4 -> WEAPON_ONE_HANDED_BLUNT
    # 5 -> WEAPON_MAGIC_BLUNT
    # 6 -> WEAPON_TWO_HANDED_MAGIC_BLUNT
    # 7 -> WEAPON_ETC_WEAPON (BOOK)
    # 8 -> WEAPON_ANCIENT_SWORD
    # 9 -> WEAPON_DAGGER
    # 10 -> 
    # 11 -> WEAPON_DUAL_SWORD
    # 12 -> 
    # 13 -> WEAPON_BOW
    # 14 -> WEAPON_CROSSBOW
    # 15 -> WEAPON_SPELL_BOOK(sort_order=31) / RAPIER(sort_order=-2)
    # 16 -> WEAPON_POLE
    # 17 -> WEAPON_DUALFIST
    # 18 -> WEAPON_SHIELD
    # 19 -> WEAPON_SYMBOL
    # 20 -> WEAPON_PISTOLS
    # 21 -> WEAPON_)ARROW
    # 22 -> ARMOR_DOLL
    # 23 -> ARMOR_CHEST
    # 24 -> ARMOR_LEGS
    # 25 -> ARMOR_FULL_CHEST
    # 26 -> ARMOR_FEET
    # 27 -> ARMOR_HEAD
    # 28 -> ARMOR_GLOVES
    # 29 -> ACCESSORY_LR_EARRING
    # 30 -> ACCESSORY_LR_RING
    # 31 -> ACCESSORY_NECKLACE
    # 32 -> ACCESSORY_BACK
    # 33 -> ACCESSORY_PENDANT
    # 34 -> ACCESSORY_JEWEL
    # 35 -> ACCESSORY_AGHATION
    # 36 -> ACCESSORY_TALISMAN
    # 37 -> ACCESSORY_DHAIR
    # 38 -> ACCESSORY_BRACELET / ACCESSORY_BROOCH
    # 39 -> ACCESSORY_BELT
    # 40 -> ETC_ENCHANT_SCROLL_WEAPON
    # 41 -> ETC_ENCHANT_SCROLL_ARMOR
    # 42 -> ETC_BLESS_SCROLL
    # 43 -> ETC_SPELL_BOOK
    # 44 -> ETC_DYE
    # 45 -> ETC_SOUL_CRYSTALL
    # 46 -> ETC_LIFE_STONE
    # 47 -> ETC_BELT_ENCHANT (Заклепка ^)
    # 48 -> 
    # 49 -> 
    # 50 -> ETC_ATTRIBUTE_STONE
    # 51 -> 
    # 52 -> 
    # 53 -> ETC_ENCHANT_SUPPORT
    # 54 -> 
    # 55 -> 
    # 56 -> ETC_POTION
    # 57 -> ETC_BUFF_SCROLL
    # 58 -> ETC_COUPON
    # 59 -> ETC_INSTANCE_TIME
    # 60 -> ETC_PET_FOOD
    # 61 -> ETC_RECEIPE
    # 62 -> ETC_GEMSTONE(sort_order=67) | ETC_L_COIN_BOX(sort_order=-55)
    # 63 -> ETC_CRAFT_KEY
    # 64 -> ETC_GRADE_CRYSTALL
    # 65 -> 
    # 66 -> 
    # 67 -> ETC_PACKED_BOX
    # 68 -> ETC_OTHER