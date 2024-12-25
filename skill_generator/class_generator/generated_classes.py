
from class_generator.base import *
from class_generator.generated_classes import *


class AbnormalAgathion(object):

    def __init__(self, id, npc_id, offset_position, unknown_array):
        self.id = id
        self.npc_id = npc_id
        self.offset_position = offset_position
        self.unknown_array = unknown_array

    @classmethod
    def from_string(self, line) -> 'AbnormalAgathion':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'npc_id', 'offset_position', 'unknown_array']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('npc_id'), data.get('offset_position'), data.get('unknown_array'))
    
    def __str__(self):
        return f"AbnormalAgathion(id={self.id}, npc_id={self.npc_id}, offset_position={self.offset_position}, unknown_array={self.unknown_array})"



class AbnormalDefaultEffect(object):

    def __init__(self, id, effect_name, is_screen_effect, is_attach_to_ground, unk_502, attach_bone_name, attach_type, offset_position, offset_rotation, is_scaling_by_cylinder, effect_scale, posteffect_id, bodypart):
        self.id = id
        self.effect_name = effect_name
        self.is_screen_effect = is_screen_effect
        self.is_attach_to_ground = is_attach_to_ground
        self.unk_502 = unk_502
        self.attach_bone_name = attach_bone_name
        self.attach_type = attach_type
        self.offset_position = offset_position
        self.offset_rotation = offset_rotation
        self.is_scaling_by_cylinder = is_scaling_by_cylinder
        self.effect_scale = effect_scale
        self.posteffect_id = posteffect_id
        self.bodypart = bodypart

    @classmethod
    def from_string(self, line) -> 'AbnormalDefaultEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'effect_name', 'is_screen_effect', 'is_attach_to_ground', 'unk_502', 'attach_bone_name', 'attach_type', 'offset_position', 'offset_rotation', 'is_scaling_by_cylinder', 'effect_scale', 'posteffect_id', 'bodypart']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('effect_name'), data.get('is_screen_effect'), data.get('is_attach_to_ground'), data.get('unk_502'), data.get('attach_bone_name'), data.get('attach_type'), data.get('offset_position'), data.get('offset_rotation'), data.get('is_scaling_by_cylinder'), data.get('effect_scale'), data.get('posteffect_id'), data.get('bodypart'))
    
    def __str__(self):
        return f"AbnormalDefaultEffect(id={self.id}, effect_name={self.effect_name}, is_screen_effect={self.is_screen_effect}, is_attach_to_ground={self.is_attach_to_ground}, unk_502={self.unk_502}, attach_bone_name={self.attach_bone_name}, attach_type={self.attach_type}, offset_position={self.offset_position}, offset_rotation={self.offset_rotation}, is_scaling_by_cylinder={self.is_scaling_by_cylinder}, effect_scale={self.effect_scale}, posteffect_id={self.posteffect_id}, bodypart={self.bodypart})"



class AbnormalEdgeEffectData(object):

    def __init__(self, id, alpha_factor, gray_factor, unk1, unk2, unk3, extrude_scale, edge_peak, edge_sharp, noise_scale, noise_pan_speed, noise_rate, max_color, min_color, unk4, bodypart):
        self.id = id
        self.alpha_factor = alpha_factor
        self.gray_factor = gray_factor
        self.unk1 = unk1
        self.unk2 = unk2
        self.unk3 = unk3
        self.extrude_scale = extrude_scale
        self.edge_peak = edge_peak
        self.edge_sharp = edge_sharp
        self.noise_scale = noise_scale
        self.noise_pan_speed = noise_pan_speed
        self.noise_rate = noise_rate
        self.max_color = max_color
        self.min_color = min_color
        self.unk4 = unk4
        self.bodypart = bodypart

    @classmethod
    def from_string(self, line) -> 'AbnormalEdgeEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'alpha_factor', 'gray_factor', 'unk1', 'unk2', 'unk3', 'extrude_scale', 'edge_peak', 'edge_sharp', 'noise_scale', 'noise_pan_speed', 'noise_rate', 'max_color', 'min_color', 'unk4', 'bodypart']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('alpha_factor'), data.get('gray_factor'), data.get('unk1'), data.get('unk2'), data.get('unk3'), data.get('extrude_scale'), data.get('edge_peak'), data.get('edge_sharp'), data.get('noise_scale'), data.get('noise_pan_speed'), data.get('noise_rate'), data.get('max_color'), data.get('min_color'), data.get('unk4'), data.get('bodypart'))
    
    def __str__(self):
        return f"AbnormalEdgeEffectData(id={self.id}, alpha_factor={self.alpha_factor}, gray_factor={self.gray_factor}, unk1={self.unk1}, unk2={self.unk2}, unk3={self.unk3}, extrude_scale={self.extrude_scale}, edge_peak={self.edge_peak}, edge_sharp={self.edge_sharp}, noise_scale={self.noise_scale}, noise_pan_speed={self.noise_pan_speed}, noise_rate={self.noise_rate}, max_color={self.max_color}, min_color={self.min_color}, unk4={self.unk4}, bodypart={self.bodypart})"



class AbnormalRelationEffect(object):

    def __init__(self, id, default_id, enemy_abnormal_id, doppelgangger_abnormal_id):
        self.id = id
        self.default_id = default_id
        self.enemy_abnormal_id = enemy_abnormal_id
        self.doppelgangger_abnormal_id = doppelgangger_abnormal_id

    @classmethod
    def from_string(self, line) -> 'AbnormalRelationEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'default_id', 'enemy_abnormal_id', 'doppelgangger_abnormal_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('default_id'), data.get('enemy_abnormal_id'), data.get('doppelgangger_abnormal_id'))
    
    def __str__(self):
        return f"AbnormalRelationEffect(id={self.id}, default_id={self.default_id}, enemy_abnormal_id={self.enemy_abnormal_id}, doppelgangger_abnormal_id={self.doppelgangger_abnormal_id})"



class ActionName(object):

    def __init__(self, id, type, category, category2, cmd, icon, iconEx1, name, toggle_group_id, automatic_use, desc):
        self.id = id
        self.type = type
        self.category = category
        self.category2 = category2
        self.cmd = cmd
        self.icon = icon
        self.iconEx1 = iconEx1
        self.name = name
        self.toggle_group_id = toggle_group_id
        self.automatic_use = automatic_use
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'ActionName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'category', 'category2', 'cmd', 'icon', 'iconEx1', 'name', 'toggle_group_id', 'automatic_use', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('category'), data.get('category2'), data.get('cmd'), data.get('icon'), data.get('iconEx1'), data.get('name'), data.get('toggle_group_id'), data.get('automatic_use'), data.get('desc'))
    
    def __str__(self):
        return f"ActionName(id={self.id}, type={self.type}, category={self.category}, category2={self.category2}, cmd={self.cmd}, icon={self.icon}, iconEx1={self.iconEx1}, name={self.name}, toggle_group_id={self.toggle_group_id}, automatic_use={self.automatic_use}, desc={self.desc})"



class ActionName(object):

    def __init__(self, id, type, category, category2, cmd, icon, iconEx1, name, toggle_group_id, automatic_use, desc):
        self.id = id
        self.type = type
        self.category = category
        self.category2 = category2
        self.cmd = cmd
        self.icon = icon
        self.iconEx1 = iconEx1
        self.name = name
        self.toggle_group_id = toggle_group_id
        self.automatic_use = automatic_use
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'ActionName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'category', 'category2', 'cmd', 'icon', 'iconEx1', 'name', 'toggle_group_id', 'automatic_use', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('category'), data.get('category2'), data.get('cmd'), data.get('icon'), data.get('iconEx1'), data.get('name'), data.get('toggle_group_id'), data.get('automatic_use'), data.get('desc'))
    
    def __str__(self):
        return f"ActionName(id={self.id}, type={self.type}, category={self.category}, category2={self.category2}, cmd={self.cmd}, icon={self.icon}, iconEx1={self.iconEx1}, name={self.name}, toggle_group_id={self.toggle_group_id}, automatic_use={self.automatic_use}, desc={self.desc})"



class AdditionalEffect(object):

    def __init__(self, id, Attach_Bone_Name, EffectNames, MeshSocketNames, EffectScales, bUsePawnScale):
        self.id = id
        self.Attach_Bone_Name = Attach_Bone_Name
        self.EffectNames = EffectNames
        self.MeshSocketNames = MeshSocketNames
        self.EffectScales = EffectScales
        self.bUsePawnScale = bUsePawnScale

    @classmethod
    def from_string(self, line) -> 'AdditionalEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'Attach_Bone_Name', 'EffectNames', 'MeshSocketNames', 'EffectScales', 'bUsePawnScale']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('Attach_Bone_Name'), data.get('EffectNames'), data.get('MeshSocketNames'), data.get('EffectScales'), data.get('bUsePawnScale'))
    
    def __str__(self):
        return f"AdditionalEffect(id={self.id}, Attach_Bone_Name={self.Attach_Bone_Name}, EffectNames={self.EffectNames}, MeshSocketNames={self.MeshSocketNames}, EffectScales={self.EffectScales}, bUsePawnScale={self.bUsePawnScale})"



class AdditionalItemGrp(AbstractItemInfo):

    def __init__(self, id, has_ani, include_item, max_energy, lookchange, cloakhide, cloakmeshtype, armor_hide):
        super().__init__(object_id)
        self.id = id
        self.has_ani = has_ani
        self.include_item = include_item
        self.max_energy = max_energy
        self.lookchange = lookchange
        self.cloakhide = cloakhide
        self.cloakmeshtype = cloakmeshtype
        self.armor_hide = armor_hide

    @classmethod
    def from_string(cls, line) -> 'AdditionalItemGrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'has_ani', 'include_item', 'max_energy', 'lookchange', 'cloakhide', 'cloakmeshtype', 'armor_hide']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('id'), data.get('has_ani'), data.get('include_item'), data.get('max_energy'), data.get('lookchange'), data.get('cloakhide'), data.get('cloakmeshtype'), data.get('armor_hide'))
    
    def __str__(self):
        return f"AdditionalItemGrp(id={self.id}, has_ani={self.has_ani}, include_item={self.include_item}, max_energy={self.max_energy}, lookchange={self.lookchange}, cloakhide={self.cloakhide}, cloakmeshtype={self.cloakmeshtype}, armor_hide={self.armor_hide})"



class AdditionalJewelEquipEffect(object):

    def __init__(self, SkillID, SkillLevel, OnStick, OnBook):
        self.SkillID = SkillID
        self.SkillLevel = SkillLevel
        self.OnStick = OnStick
        self.OnBook = OnBook

    @classmethod
    def from_string(self, line) -> 'AdditionalJewelEquipEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['SkillID', 'SkillLevel', 'OnStick', 'OnBook']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('SkillID'), data.get('SkillLevel'), data.get('OnStick'), data.get('OnBook'))
    
    def __str__(self):
        return f"AdditionalJewelEquipEffect(SkillID={self.SkillID}, SkillLevel={self.SkillLevel}, OnStick={self.OnStick}, OnBook={self.OnBook})"



class AdditionalNpcGrpParts(object):

    def __init__(self, npc_id, clazz, chest, legs, gloves, feet, back, hairAcc, hairStyle, rhand, lhand, beast, weapon_enchant, armor_enchant, unk_447):
        self.npc_id = npc_id
        self.clazz = clazz
        self.chest = chest
        self.legs = legs
        self.gloves = gloves
        self.feet = feet
        self.back = back
        self.hairAcc = hairAcc
        self.hairStyle = hairStyle
        self.rhand = rhand
        self.lhand = lhand
        self.beast = beast
        self.weapon_enchant = weapon_enchant
        self.armor_enchant = armor_enchant
        self.unk_447 = unk_447

    @classmethod
    def from_string(self, line) -> 'AdditionalNpcGrpParts':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_id', 'clazz', 'chest', 'legs', 'gloves', 'feet', 'back', 'hairAcc', 'hairStyle', 'rhand', 'lhand', 'beast', 'weapon_enchant', 'armor_enchant', 'unk_447']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('npc_id'), data.get('clazz'), data.get('chest'), data.get('legs'), data.get('gloves'), data.get('feet'), data.get('back'), data.get('hairAcc'), data.get('hairStyle'), data.get('rhand'), data.get('lhand'), data.get('beast'), data.get('weapon_enchant'), data.get('armor_enchant'), data.get('unk_447'))
    
    def __str__(self):
        return f"AdditionalNpcGrpParts(npc_id={self.npc_id}, clazz={self.clazz}, chest={self.chest}, legs={self.legs}, gloves={self.gloves}, feet={self.feet}, back={self.back}, hairAcc={self.hairAcc}, hairStyle={self.hairStyle}, rhand={self.rhand}, lhand={self.lhand}, beast={self.beast}, weapon_enchant={self.weapon_enchant}, armor_enchant={self.armor_enchant}, unk_447={self.unk_447})"



class AdditionalSoulshotEffect(object):

    def __init__(self, ItemClassID, Level, AttackEffect, AttackCriticalEffect):
        self.ItemClassID = ItemClassID
        self.Level = Level
        self.AttackEffect = AttackEffect
        self.AttackCriticalEffect = AttackCriticalEffect

    @classmethod
    def from_string(self, line) -> 'AdditionalSoulshotEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['ItemClassID', 'Level', 'AttackEffect', 'AttackCriticalEffect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ItemClassID'), data.get('Level'), data.get('AttackEffect'), data.get('AttackCriticalEffect'))
    
    def __str__(self):
        return f"AdditionalSoulshotEffect(ItemClassID={self.ItemClassID}, Level={self.Level}, AttackEffect={self.AttackEffect}, AttackCriticalEffect={self.AttackCriticalEffect})"



class Agathiondata(object):

    def __init__(self, item_id, enchant, main_skill, sub_skill):
        self.item_id = item_id
        self.enchant = enchant
        self.main_skill = main_skill
        self.sub_skill = sub_skill

    @classmethod
    def from_string(self, line) -> 'Agathiondata':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'enchant', 'main_skill', 'sub_skill']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('enchant'), data.get('main_skill'), data.get('sub_skill'))
    
    def __str__(self):
        return f"Agathiondata(item_id={self.item_id}, enchant={self.enchant}, main_skill={self.main_skill}, sub_skill={self.sub_skill})"



class AlchemyData(object):

    def __init__(self, skill_id, skill_level, skill_max_level, grade_type, category_type, string_id, recipe_items, result_item, fail_result_item):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_max_level = skill_max_level
        self.grade_type = grade_type
        self.category_type = category_type
        self.string_id = string_id
        self.recipe_items = recipe_items
        self.result_item = result_item
        self.fail_result_item = fail_result_item

    @classmethod
    def from_string(self, line) -> 'AlchemyData':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_max_level', 'grade_type', 'category_type', 'string_id', 'recipe_items', 'result_item', 'fail_result_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('skill_max_level'), data.get('grade_type'), data.get('category_type'), data.get('string_id'), data.get('recipe_items'), data.get('result_item'), data.get('fail_result_item'))
    
    def __str__(self):
        return f"AlchemyData(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_max_level={self.skill_max_level}, grade_type={self.grade_type}, category_type={self.category_type}, string_id={self.string_id}, recipe_items={self.recipe_items}, result_item={self.result_item}, fail_result_item={self.fail_result_item})"



class AlterSkillData(object):

    def __init__(self, origin_skill_id, alter_skill_id):
        self.origin_skill_id = origin_skill_id
        self.alter_skill_id = alter_skill_id

    @classmethod
    def from_string(self, line) -> 'AlterSkillData':
        split_params = line.split('\t')[1:-1]
        attributes = ['origin_skill_id', 'alter_skill_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('origin_skill_id'), data.get('alter_skill_id'))
    
    def __str__(self):
        return f"AlterSkillData(origin_skill_id={self.origin_skill_id}, alter_skill_id={self.alter_skill_id})"



class AnimationCombo(object):

    def __init__(self, name, anim0, anim1, anim2, loop):
        self.name = name
        self.anim0 = anim0
        self.anim1 = anim1
        self.anim2 = anim2
        self.loop = loop

    @classmethod
    def from_string(self, line) -> 'AnimationCombo':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'anim0', 'anim1', 'anim2', 'loop']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('anim0'), data.get('anim1'), data.get('anim2'), data.get('loop'))
    
    def __str__(self):
        return f"AnimationCombo(name={self.name}, anim0={self.anim0}, anim1={self.anim1}, anim2={self.anim2}, loop={self.loop})"



class ArmorGradeEffectSet(object):

    def __init__(self, id, effect_name, attach_bone_name, attach_type, offset_position, offset_rotation, effect_scale, is_scaling_by_cylinder):
        self.id = id
        self.effect_name = effect_name
        self.attach_bone_name = attach_bone_name
        self.attach_type = attach_type
        self.offset_position = offset_position
        self.offset_rotation = offset_rotation
        self.effect_scale = effect_scale
        self.is_scaling_by_cylinder = is_scaling_by_cylinder

    @classmethod
    def from_string(self, line) -> 'ArmorGradeEffectSet':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'effect_name', 'attach_bone_name', 'attach_type', 'offset_position', 'offset_rotation', 'effect_scale', 'is_scaling_by_cylinder']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('effect_name'), data.get('attach_bone_name'), data.get('attach_type'), data.get('offset_position'), data.get('offset_rotation'), data.get('effect_scale'), data.get('is_scaling_by_cylinder'))
    
    def __str__(self):
        return f"ArmorGradeEffectSet(id={self.id}, effect_name={self.effect_name}, attach_bone_name={self.attach_bone_name}, attach_type={self.attach_type}, offset_position={self.offset_position}, offset_rotation={self.offset_rotation}, effect_scale={self.effect_scale}, is_scaling_by_cylinder={self.is_scaling_by_cylinder})"



class Armorgrp(AbstractItemInfo):

    def __init__(self, tag, object_id, drop_type, drop_anim_type, drop_radius, drop_height, drop_texture, icon, durability, weight, material_type, crystallizable, related_quest_id, color, is_attribution, icon_panel, complete_item_dropsound_type, inventory_type, body_part, m_HumnFigh, m_HumnFigh_add, f_HumnFigh, f_HumnFigh_add, m_DarkElf, m_DarkElf_add, f_DarkElf, f_DarkElf_add, m_Dorf, m_Dorf_add, f_Dorf, f_Dorf_add, m_Elf, m_Elf_add, f_Elf, f_Elf_add, m_HumnMyst, m_HumnMyst_add, f_HumnMyst, f_HumnMyst_add, m_OrcFigh, m_OrcFigh_add, f_OrcFigh, f_OrcFigh_add, m_OrcMage, m_OrcMage_add, f_OrcMage, f_OrcMage_add, m_Kamael, m_Kamael_add, f_Kamael, f_Kamael_add, m_Ertheia, m_Ertheia_add, f_Ertheia, f_Ertheia_add, m_Sylph, m_Sylph_add, f_Sylph, f_Sylph_add, m_HighElf, m_HighElf_add, f_HighElf, f_HighElf_add, NPC, NPC_add, attack_effect, item_sound, drop_sound, equip_sound, UNK_7, UNK_6, armor_type, crystal_type, mp_bonus, hide_mask, underwear_body_part1, underwear_body_part2, full_armor_enchant_effect_type, ensoul_slot_count):
        super().__init__(object_id)
        self.tag = tag
        self.object_id = object_id
        self.drop_type = drop_type
        self.drop_anim_type = drop_anim_type
        self.drop_radius = drop_radius
        self.drop_height = drop_height
        self.drop_texture = drop_texture
        self.icon = icon
        self.durability = durability
        self.weight = weight
        self.material_type = material_type
        self.crystallizable = crystallizable
        self.related_quest_id = related_quest_id
        self.color = color
        self.is_attribution = is_attribution
        self.icon_panel = icon_panel
        self.complete_item_dropsound_type = complete_item_dropsound_type
        self.inventory_type = inventory_type
        self.body_part = body_part
        self.m_HumnFigh = m_HumnFigh
        self.m_HumnFigh_add = m_HumnFigh_add
        self.f_HumnFigh = f_HumnFigh
        self.f_HumnFigh_add = f_HumnFigh_add
        self.m_DarkElf = m_DarkElf
        self.m_DarkElf_add = m_DarkElf_add
        self.f_DarkElf = f_DarkElf
        self.f_DarkElf_add = f_DarkElf_add
        self.m_Dorf = m_Dorf
        self.m_Dorf_add = m_Dorf_add
        self.f_Dorf = f_Dorf
        self.f_Dorf_add = f_Dorf_add
        self.m_Elf = m_Elf
        self.m_Elf_add = m_Elf_add
        self.f_Elf = f_Elf
        self.f_Elf_add = f_Elf_add
        self.m_HumnMyst = m_HumnMyst
        self.m_HumnMyst_add = m_HumnMyst_add
        self.f_HumnMyst = f_HumnMyst
        self.f_HumnMyst_add = f_HumnMyst_add
        self.m_OrcFigh = m_OrcFigh
        self.m_OrcFigh_add = m_OrcFigh_add
        self.f_OrcFigh = f_OrcFigh
        self.f_OrcFigh_add = f_OrcFigh_add
        self.m_OrcMage = m_OrcMage
        self.m_OrcMage_add = m_OrcMage_add
        self.f_OrcMage = f_OrcMage
        self.f_OrcMage_add = f_OrcMage_add
        self.m_Kamael = m_Kamael
        self.m_Kamael_add = m_Kamael_add
        self.f_Kamael = f_Kamael
        self.f_Kamael_add = f_Kamael_add
        self.m_Ertheia = m_Ertheia
        self.m_Ertheia_add = m_Ertheia_add
        self.f_Ertheia = f_Ertheia
        self.f_Ertheia_add = f_Ertheia_add
        self.m_Sylph = m_Sylph
        self.m_Sylph_add = m_Sylph_add
        self.f_Sylph = f_Sylph
        self.f_Sylph_add = f_Sylph_add
        self.m_HighElf = m_HighElf
        self.m_HighElf_add = m_HighElf_add
        self.f_HighElf = f_HighElf
        self.f_HighElf_add = f_HighElf_add
        self.NPC = NPC
        self.NPC_add = NPC_add
        self.attack_effect = attack_effect
        self.item_sound = item_sound
        self.drop_sound = drop_sound
        self.equip_sound = equip_sound
        self.UNK_7 = UNK_7
        self.UNK_6 = UNK_6
        self.armor_type = armor_type
        self.crystal_type = crystal_type
        self.mp_bonus = mp_bonus
        self.hide_mask = hide_mask
        self.underwear_body_part1 = underwear_body_part1
        self.underwear_body_part2 = underwear_body_part2
        self.full_armor_enchant_effect_type = full_armor_enchant_effect_type
        self.ensoul_slot_count = ensoul_slot_count

    @classmethod
    def from_string(cls, line) -> 'Armorgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['tag', 'object_id', 'drop_type', 'drop_anim_type', 'drop_radius', 'drop_height', 'drop_texture', 'icon', 'durability', 'weight', 'material_type', 'crystallizable', 'related_quest_id', 'color', 'is_attribution', 'icon_panel', 'complete_item_dropsound_type', 'inventory_type', 'body_part', 'm_HumnFigh', 'm_HumnFigh_add', 'f_HumnFigh', 'f_HumnFigh_add', 'm_DarkElf', 'm_DarkElf_add', 'f_DarkElf', 'f_DarkElf_add', 'm_Dorf', 'm_Dorf_add', 'f_Dorf', 'f_Dorf_add', 'm_Elf', 'm_Elf_add', 'f_Elf', 'f_Elf_add', 'm_HumnMyst', 'm_HumnMyst_add', 'f_HumnMyst', 'f_HumnMyst_add', 'm_OrcFigh', 'm_OrcFigh_add', 'f_OrcFigh', 'f_OrcFigh_add', 'm_OrcMage', 'm_OrcMage_add', 'f_OrcMage', 'f_OrcMage_add', 'm_Kamael', 'm_Kamael_add', 'f_Kamael', 'f_Kamael_add', 'm_Ertheia', 'm_Ertheia_add', 'f_Ertheia', 'f_Ertheia_add', 'm_Sylph', 'm_Sylph_add', 'f_Sylph', 'f_Sylph_add', 'm_HighElf', 'm_HighElf_add', 'f_HighElf', 'f_HighElf_add', 'NPC', 'NPC_add', 'attack_effect', 'item_sound', 'drop_sound', 'equip_sound', 'UNK_7', 'UNK_6', 'armor_type', 'crystal_type', 'mp_bonus', 'hide_mask', 'underwear_body_part1', 'underwear_body_part2', 'full_armor_enchant_effect_type', 'ensoul_slot_count']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('tag'), data.get('object_id'), data.get('drop_type'), data.get('drop_anim_type'), data.get('drop_radius'), data.get('drop_height'), data.get('drop_texture'), data.get('icon'), data.get('durability'), data.get('weight'), data.get('material_type'), data.get('crystallizable'), data.get('related_quest_id'), data.get('color'), data.get('is_attribution'), data.get('icon_panel'), data.get('complete_item_dropsound_type'), data.get('inventory_type'), data.get('body_part'), data.get('m_HumnFigh'), data.get('m_HumnFigh_add'), data.get('f_HumnFigh'), data.get('f_HumnFigh_add'), data.get('m_DarkElf'), data.get('m_DarkElf_add'), data.get('f_DarkElf'), data.get('f_DarkElf_add'), data.get('m_Dorf'), data.get('m_Dorf_add'), data.get('f_Dorf'), data.get('f_Dorf_add'), data.get('m_Elf'), data.get('m_Elf_add'), data.get('f_Elf'), data.get('f_Elf_add'), data.get('m_HumnMyst'), data.get('m_HumnMyst_add'), data.get('f_HumnMyst'), data.get('f_HumnMyst_add'), data.get('m_OrcFigh'), data.get('m_OrcFigh_add'), data.get('f_OrcFigh'), data.get('f_OrcFigh_add'), data.get('m_OrcMage'), data.get('m_OrcMage_add'), data.get('f_OrcMage'), data.get('f_OrcMage_add'), data.get('m_Kamael'), data.get('m_Kamael_add'), data.get('f_Kamael'), data.get('f_Kamael_add'), data.get('m_Ertheia'), data.get('m_Ertheia_add'), data.get('f_Ertheia'), data.get('f_Ertheia_add'), data.get('m_Sylph'), data.get('m_Sylph_add'), data.get('f_Sylph'), data.get('f_Sylph_add'), data.get('m_HighElf'), data.get('m_HighElf_add'), data.get('f_HighElf'), data.get('f_HighElf_add'), data.get('NPC'), data.get('NPC_add'), data.get('attack_effect'), data.get('item_sound'), data.get('drop_sound'), data.get('equip_sound'), data.get('UNK_7'), data.get('UNK_6'), data.get('armor_type'), data.get('crystal_type'), data.get('mp_bonus'), data.get('hide_mask'), data.get('underwear_body_part1'), data.get('underwear_body_part2'), data.get('full_armor_enchant_effect_type'), data.get('ensoul_slot_count'))
    
    def __str__(self):
        return f"Armorgrp(tag={self.tag}, object_id={self.object_id}, drop_type={self.drop_type}, drop_anim_type={self.drop_anim_type}, drop_radius={self.drop_radius}, drop_height={self.drop_height}, drop_texture={self.drop_texture}, icon={self.icon}, durability={self.durability}, weight={self.weight}, material_type={self.material_type}, crystallizable={self.crystallizable}, related_quest_id={self.related_quest_id}, color={self.color}, is_attribution={self.is_attribution}, icon_panel={self.icon_panel}, complete_item_dropsound_type={self.complete_item_dropsound_type}, inventory_type={self.inventory_type}, body_part={self.body_part}, m_HumnFigh={self.m_HumnFigh}, m_HumnFigh_add={self.m_HumnFigh_add}, f_HumnFigh={self.f_HumnFigh}, f_HumnFigh_add={self.f_HumnFigh_add}, m_DarkElf={self.m_DarkElf}, m_DarkElf_add={self.m_DarkElf_add}, f_DarkElf={self.f_DarkElf}, f_DarkElf_add={self.f_DarkElf_add}, m_Dorf={self.m_Dorf}, m_Dorf_add={self.m_Dorf_add}, f_Dorf={self.f_Dorf}, f_Dorf_add={self.f_Dorf_add}, m_Elf={self.m_Elf}, m_Elf_add={self.m_Elf_add}, f_Elf={self.f_Elf}, f_Elf_add={self.f_Elf_add}, m_HumnMyst={self.m_HumnMyst}, m_HumnMyst_add={self.m_HumnMyst_add}, f_HumnMyst={self.f_HumnMyst}, f_HumnMyst_add={self.f_HumnMyst_add}, m_OrcFigh={self.m_OrcFigh}, m_OrcFigh_add={self.m_OrcFigh_add}, f_OrcFigh={self.f_OrcFigh}, f_OrcFigh_add={self.f_OrcFigh_add}, m_OrcMage={self.m_OrcMage}, m_OrcMage_add={self.m_OrcMage_add}, f_OrcMage={self.f_OrcMage}, f_OrcMage_add={self.f_OrcMage_add}, m_Kamael={self.m_Kamael}, m_Kamael_add={self.m_Kamael_add}, f_Kamael={self.f_Kamael}, f_Kamael_add={self.f_Kamael_add}, m_Ertheia={self.m_Ertheia}, m_Ertheia_add={self.m_Ertheia_add}, f_Ertheia={self.f_Ertheia}, f_Ertheia_add={self.f_Ertheia_add}, m_Sylph={self.m_Sylph}, m_Sylph_add={self.m_Sylph_add}, f_Sylph={self.f_Sylph}, f_Sylph_add={self.f_Sylph_add}, m_HighElf={self.m_HighElf}, m_HighElf_add={self.m_HighElf_add}, f_HighElf={self.f_HighElf}, f_HighElf_add={self.f_HighElf_add}, NPC={self.NPC}, NPC_add={self.NPC_add}, attack_effect={self.attack_effect}, item_sound={self.item_sound}, drop_sound={self.drop_sound}, equip_sound={self.equip_sound}, UNK_7={self.UNK_7}, UNK_6={self.UNK_6}, armor_type={self.armor_type}, crystal_type={self.crystal_type}, mp_bonus={self.mp_bonus}, hide_mask={self.hide_mask}, underwear_body_part1={self.underwear_body_part1}, underwear_body_part2={self.underwear_body_part2}, full_armor_enchant_effect_type={self.full_armor_enchant_effect_type}, ensoul_slot_count={self.ensoul_slot_count})"
    
    def get_item_type(self):
        return self.armor_type

    def get_material(self):
        return self.material_type

    def get_weight(self):
        return self.weight

    def get_consume_type(self):
        return "EQUIP"

    def get_icon(self):
        return self.icon


class ArtifactData(object):

    def __init__(self, item_id, enchant_skill_id, max_skill_level):
        self.item_id = item_id
        self.enchant_skill_id = enchant_skill_id
        self.max_skill_level = max_skill_level

    @classmethod
    def from_string(self, line) -> 'ArtifactData':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'enchant_skill_id', 'max_skill_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('enchant_skill_id'), data.get('max_skill_level'))
    
    def __str__(self):
        return f"ArtifactData(item_id={self.item_id}, enchant_skill_id={self.enchant_skill_id}, max_skill_level={self.max_skill_level})"



class ArtifactEnchantSetting(object):

    def __init__(self, enchant, min_enchant_material):
        self.enchant = enchant
        self.min_enchant_material = min_enchant_material

    @classmethod
    def from_string(self, line) -> 'ArtifactEnchantSetting':
        split_params = line.split('\t')[1:-1]
        attributes = ['enchant', 'min_enchant_material']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('enchant'), data.get('min_enchant_material'))
    
    def __str__(self):
        return f"ArtifactEnchantSetting(enchant={self.enchant}, min_enchant_material={self.min_enchant_material})"



class ArtifactTypeSetting(object):

    def __init__(self, artifact_group_id, material_items):
        self.artifact_group_id = artifact_group_id
        self.material_items = material_items

    @classmethod
    def from_string(self, line) -> 'ArtifactTypeSetting':
        split_params = line.split('\t')[1:-1]
        attributes = ['artifact_group_id', 'material_items']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('artifact_group_id'), data.get('material_items'))
    
    def __str__(self):
        return f"ArtifactTypeSetting(artifact_group_id={self.artifact_group_id}, material_items={self.material_items})"



class ArtifactUpgrade(object):

    def __init__(self, artifact_item_id, artifact_level, artifact_group_id, count, result_prob):
        self.artifact_item_id = artifact_item_id
        self.artifact_level = artifact_level
        self.artifact_group_id = artifact_group_id
        self.count = count
        self.result_prob = result_prob

    @classmethod
    def from_string(self, line) -> 'ArtifactUpgrade':
        split_params = line.split('\t')[1:-1]
        attributes = ['artifact_item_id', 'artifact_level', 'artifact_group_id', 'count', 'result_prob']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('artifact_item_id'), data.get('artifact_level'), data.get('artifact_group_id'), data.get('count'), data.get('result_prob'))
    
    def __str__(self):
        return f"ArtifactUpgrade(artifact_item_id={self.artifact_item_id}, artifact_level={self.artifact_level}, artifact_group_id={self.artifact_group_id}, count={self.count}, result_prob={self.result_prob})"



class BlessOption(object):

    def __init__(self, group_id, type_group, enchant_effect):
        self.group_id = group_id
        self.type_group = type_group
        self.enchant_effect = enchant_effect

    @classmethod
    def from_string(self, line) -> 'BlessOption':
        split_params = line.split('\t')[1:-1]
        attributes = ['group_id', 'type_group', 'enchant_effect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('group_id'), data.get('type_group'), data.get('enchant_effect'))
    
    def __str__(self):
        return f"BlessOption(group_id={self.group_id}, type_group={self.type_group}, enchant_effect={self.enchant_effect})"



class CardCollectData(object):

    def __init__(self, event_id, collect_group_id, card_id, card_reward_Texture, sub_title):
        self.event_id = event_id
        self.collect_group_id = collect_group_id
        self.card_id = card_id
        self.card_reward_Texture = card_reward_Texture
        self.sub_title = sub_title

    @classmethod
    def from_string(self, line) -> 'CardCollectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_id', 'collect_group_id', 'card_id', 'card_reward_Texture', 'sub_title']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_id'), data.get('collect_group_id'), data.get('card_id'), data.get('card_reward_Texture'), data.get('sub_title'))
    
    def __str__(self):
        return f"CardCollectData(event_id={self.event_id}, collect_group_id={self.collect_group_id}, card_id={self.card_id}, card_reward_Texture={self.card_reward_Texture}, sub_title={self.sub_title})"



class CardCollectData(object):

    def __init__(self, event_id, collect_group_id, card_id, card_reward_Texture, sub_title):
        self.event_id = event_id
        self.collect_group_id = collect_group_id
        self.card_id = card_id
        self.card_reward_Texture = card_reward_Texture
        self.sub_title = sub_title

    @classmethod
    def from_string(self, line) -> 'CardCollectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_id', 'collect_group_id', 'card_id', 'card_reward_Texture', 'sub_title']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_id'), data.get('collect_group_id'), data.get('card_id'), data.get('card_reward_Texture'), data.get('sub_title'))
    
    def __str__(self):
        return f"CardCollectData(event_id={self.event_id}, collect_group_id={self.collect_group_id}, card_id={self.card_id}, card_reward_Texture={self.card_reward_Texture}, sub_title={self.sub_title})"



class Cardselect(object):

    def __init__(self, boss_id, fee_daily_count, stage, fee_normal, fee_special, transcend_effect, unk_474, fee_adena_normal, fee_adena_special):
        self.boss_id = boss_id
        self.fee_daily_count = fee_daily_count
        self.stage = stage
        self.fee_normal = fee_normal
        self.fee_special = fee_special
        self.transcend_effect = transcend_effect
        self.unk_474 = unk_474
        self.fee_adena_normal = fee_adena_normal
        self.fee_adena_special = fee_adena_special

    @classmethod
    def from_string(self, line) -> 'Cardselect':
        split_params = line.split('\t')[1:-1]
        attributes = ['boss_id', 'fee_daily_count', 'stage', 'fee_normal', 'fee_special', 'transcend_effect', 'unk_474', 'fee_adena_normal', 'fee_adena_special']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('boss_id'), data.get('fee_daily_count'), data.get('stage'), data.get('fee_normal'), data.get('fee_special'), data.get('transcend_effect'), data.get('unk_474'), data.get('fee_adena_normal'), data.get('fee_adena_special'))
    
    def __str__(self):
        return f"Cardselect(boss_id={self.boss_id}, fee_daily_count={self.fee_daily_count}, stage={self.stage}, fee_normal={self.fee_normal}, fee_special={self.fee_special}, transcend_effect={self.transcend_effect}, unk_474={self.unk_474}, fee_adena_normal={self.fee_adena_normal}, fee_adena_special={self.fee_adena_special})"



class CastleName(object):

    def __init__(self, namber, tag, id, name, loc, desc, mark, markgray, flagicon, mercname, regionid):
        self.namber = namber
        self.tag = tag
        self.id = id
        self.name = name
        self.loc = loc
        self.desc = desc
        self.mark = mark
        self.markgray = markgray
        self.flagicon = flagicon
        self.mercname = mercname
        self.regionid = regionid

    @classmethod
    def from_string(self, line) -> 'CastleName':
        split_params = line.split('\t')[1:-1]
        attributes = ['namber', 'tag', 'id', 'name', 'loc', 'desc', 'mark', 'markgray', 'flagicon', 'mercname', 'regionid']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('namber'), data.get('tag'), data.get('id'), data.get('name'), data.get('loc'), data.get('desc'), data.get('mark'), data.get('markgray'), data.get('flagicon'), data.get('mercname'), data.get('regionid'))
    
    def __str__(self):
        return f"CastleName(namber={self.namber}, tag={self.tag}, id={self.id}, name={self.name}, loc={self.loc}, desc={self.desc}, mark={self.mark}, markgray={self.markgray}, flagicon={self.flagicon}, mercname={self.mercname}, regionid={self.regionid})"



class CastleName(object):

    def __init__(self, namber, tag, id, name, loc, desc, mark, markgray, flagicon, mercname, regionid):
        self.namber = namber
        self.tag = tag
        self.id = id
        self.name = name
        self.loc = loc
        self.desc = desc
        self.mark = mark
        self.markgray = markgray
        self.flagicon = flagicon
        self.mercname = mercname
        self.regionid = regionid

    @classmethod
    def from_string(self, line) -> 'CastleName':
        split_params = line.split('\t')[1:-1]
        attributes = ['namber', 'tag', 'id', 'name', 'loc', 'desc', 'mark', 'markgray', 'flagicon', 'mercname', 'regionid']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('namber'), data.get('tag'), data.get('id'), data.get('name'), data.get('loc'), data.get('desc'), data.get('mark'), data.get('markgray'), data.get('flagicon'), data.get('mercname'), data.get('regionid'))
    
    def __str__(self):
        return f"CastleName(namber={self.namber}, tag={self.tag}, id={self.id}, name={self.name}, loc={self.loc}, desc={self.desc}, mark={self.mark}, markgray={self.markgray}, flagicon={self.flagicon}, mercname={self.mercname}, regionid={self.regionid})"



class CharacterAbility(object):

    def __init__(self, category, detail, tooltip, index, UNK_1, is_percent):
        self.category = category
        self.detail = detail
        self.tooltip = tooltip
        self.index = index
        self.UNK_1 = UNK_1
        self.is_percent = is_percent

    @classmethod
    def from_string(self, line) -> 'CharacterAbility':
        split_params = line.split('\t')[1:-1]
        attributes = ['category', 'detail', 'tooltip', 'index', 'UNK_1', 'is_percent']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('category'), data.get('detail'), data.get('tooltip'), data.get('index'), data.get('UNK_1'), data.get('is_percent'))
    
    def __str__(self):
        return f"CharacterAbility(category={self.category}, detail={self.detail}, tooltip={self.tooltip}, index={self.index}, UNK_1={self.UNK_1}, is_percent={self.is_percent})"



class CharacterAbility(object):

    def __init__(self, category, detail, tooltip, index, UNK_1, is_percent):
        self.category = category
        self.detail = detail
        self.tooltip = tooltip
        self.index = index
        self.UNK_1 = UNK_1
        self.is_percent = is_percent

    @classmethod
    def from_string(self, line) -> 'CharacterAbility':
        split_params = line.split('\t')[1:-1]
        attributes = ['category', 'detail', 'tooltip', 'index', 'UNK_1', 'is_percent']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('category'), data.get('detail'), data.get('tooltip'), data.get('index'), data.get('UNK_1'), data.get('is_percent'))
    
    def __str__(self):
        return f"CharacterAbility(category={self.category}, detail={self.detail}, tooltip={self.tooltip}, index={self.index}, UNK_1={self.UNK_1}, is_percent={self.is_percent})"



class CharacterInitialStatExData(object):

    def __init__(self, clazz, race, sex, str, dex, con, int, wit, men, luc, cha):
        self.clazz = clazz
        self.race = race
        self.sex = sex
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wit = wit
        self.men = men
        self.luc = luc
        self.cha = cha

    @classmethod
    def from_string(self, line) -> 'CharacterInitialStatExData':
        split_params = line.split('\t')[1:-1]
        attributes = ['clazz', 'race', 'sex', 'str', 'dex', 'con', 'int', 'wit', 'men', 'luc', 'cha']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('clazz'), data.get('race'), data.get('sex'), data.get('str'), data.get('dex'), data.get('con'), data.get('int'), data.get('wit'), data.get('men'), data.get('luc'), data.get('cha'))
    
    def __str__(self):
        return f"CharacterInitialStatExData(clazz={self.clazz}, race={self.race}, sex={self.sex}, str={self.str}, dex={self.dex}, con={self.con}, int={self.int}, wit={self.wit}, men={self.men}, luc={self.luc}, cha={self.cha})"



class CharCreategrp(AbstractItemInfo):

    def __init__(self, x, y, z, chest, legs, gloves, feet, rhand, lhand, back, npcid, IntroAnimName, IntroWaitAnimName, NPCIntroAnimName, NPCIntroWaitAnimName):
        super().__init__(object_id)
        self.x = x
        self.y = y
        self.z = z
        self.chest = chest
        self.legs = legs
        self.gloves = gloves
        self.feet = feet
        self.rhand = rhand
        self.lhand = lhand
        self.back = back
        self.npcid = npcid
        self.IntroAnimName = IntroAnimName
        self.IntroWaitAnimName = IntroWaitAnimName
        self.NPCIntroAnimName = NPCIntroAnimName
        self.NPCIntroWaitAnimName = NPCIntroWaitAnimName

    @classmethod
    def from_string(cls, line) -> 'CharCreategrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['x', 'y', 'z', 'chest', 'legs', 'gloves', 'feet', 'rhand', 'lhand', 'back', 'npcid', 'IntroAnimName', 'IntroWaitAnimName', 'NPCIntroAnimName', 'NPCIntroWaitAnimName']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('x'), data.get('y'), data.get('z'), data.get('chest'), data.get('legs'), data.get('gloves'), data.get('feet'), data.get('rhand'), data.get('lhand'), data.get('back'), data.get('npcid'), data.get('IntroAnimName'), data.get('IntroWaitAnimName'), data.get('NPCIntroAnimName'), data.get('NPCIntroWaitAnimName'))
    
    def __str__(self):
        return f"CharCreategrp(x={self.x}, y={self.y}, z={self.z}, chest={self.chest}, legs={self.legs}, gloves={self.gloves}, feet={self.feet}, rhand={self.rhand}, lhand={self.lhand}, back={self.back}, npcid={self.npcid}, IntroAnimName={self.IntroAnimName}, IntroWaitAnimName={self.IntroWaitAnimName}, NPCIntroAnimName={self.NPCIntroAnimName}, NPCIntroWaitAnimName={self.NPCIntroWaitAnimName})"



class Chargrp(AbstractItemInfo):

    def __init__(self, hair, face_mesh, face_texture, beard_mesh, beard_texture, test, attack_effect, walkanimframe, attack_sound, defense_sound, damage_sound, voice_sound_weapon, voice_sound_weapon02, unk3, class_name, race, class_id, class_type, unk4, unk5):
        super().__init__(object_id)
        self.hair = hair
        self.face_mesh = face_mesh
        self.face_texture = face_texture
        self.beard_mesh = beard_mesh
        self.beard_texture = beard_texture
        self.test = test
        self.attack_effect = attack_effect
        self.walkanimframe = walkanimframe
        self.attack_sound = attack_sound
        self.defense_sound = defense_sound
        self.damage_sound = damage_sound
        self.voice_sound_weapon = voice_sound_weapon
        self.voice_sound_weapon02 = voice_sound_weapon02
        self.unk3 = unk3
        self.class_name = class_name
        self.race = race
        self.class_id = class_id
        self.class_type = class_type
        self.unk4 = unk4
        self.unk5 = unk5

    @classmethod
    def from_string(cls, line) -> 'Chargrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['hair', 'face_mesh', 'face_texture', 'beard_mesh', 'beard_texture', 'test', 'attack_effect', 'walkanimframe', 'attack_sound', 'defense_sound', 'damage_sound', 'voice_sound_weapon', 'voice_sound_weapon02', 'unk3', 'class_name', 'race', 'class_id', 'class_type', 'unk4', 'unk5']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('hair'), data.get('face_mesh'), data.get('face_texture'), data.get('beard_mesh'), data.get('beard_texture'), data.get('test'), data.get('attack_effect'), data.get('walkanimframe'), data.get('attack_sound'), data.get('defense_sound'), data.get('damage_sound'), data.get('voice_sound_weapon'), data.get('voice_sound_weapon02'), data.get('unk3'), data.get('class_name'), data.get('race'), data.get('class_id'), data.get('class_type'), data.get('unk4'), data.get('unk5'))
    
    def __str__(self):
        return f"Chargrp(hair={self.hair}, face_mesh={self.face_mesh}, face_texture={self.face_texture}, beard_mesh={self.beard_mesh}, beard_texture={self.beard_texture}, test={self.test}, attack_effect={self.attack_effect}, walkanimframe={self.walkanimframe}, attack_sound={self.attack_sound}, defense_sound={self.defense_sound}, damage_sound={self.damage_sound}, voice_sound_weapon={self.voice_sound_weapon}, voice_sound_weapon02={self.voice_sound_weapon02}, unk3={self.unk3}, class_name={self.class_name}, race={self.race}, class_id={self.class_id}, class_type={self.class_type}, unk4={self.unk4}, unk5={self.unk5})"



class CharHeadExgrp(AbstractItemInfo):

    def __init__(self, class_name, hair, face_mesh, face_texture, beard_mesh, beard_texture):
        super().__init__(object_id)
        self.class_name = class_name
        self.hair = hair
        self.face_mesh = face_mesh
        self.face_texture = face_texture
        self.beard_mesh = beard_mesh
        self.beard_texture = beard_texture

    @classmethod
    def from_string(cls, line) -> 'CharHeadExgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['class_name', 'hair', 'face_mesh', 'face_texture', 'beard_mesh', 'beard_texture']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('class_name'), data.get('hair'), data.get('face_mesh'), data.get('face_texture'), data.get('beard_mesh'), data.get('beard_texture'))
    
    def __str__(self):
        return f"CharHeadExgrp(class_name={self.class_name}, hair={self.hair}, face_mesh={self.face_mesh}, face_texture={self.face_texture}, beard_mesh={self.beard_mesh}, beard_texture={self.beard_texture})"



class ClassInfo(object):

    def __init__(self, clazz, classrole, classrole_name, classtransfer_degree, str, dex, con, int, wit, men, luc, cha, description):
        self.clazz = clazz
        self.classrole = classrole
        self.classrole_name = classrole_name
        self.classtransfer_degree = classtransfer_degree
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wit = wit
        self.men = men
        self.luc = luc
        self.cha = cha
        self.description = description

    @classmethod
    def from_string(self, line) -> 'ClassInfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['clazz', 'classrole', 'classrole_name', 'classtransfer_degree', 'str', 'dex', 'con', 'int', 'wit', 'men', 'luc', 'cha', 'description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('clazz'), data.get('classrole'), data.get('classrole_name'), data.get('classtransfer_degree'), data.get('str'), data.get('dex'), data.get('con'), data.get('int'), data.get('wit'), data.get('men'), data.get('luc'), data.get('cha'), data.get('description'))
    
    def __str__(self):
        return f"ClassInfo(clazz={self.clazz}, classrole={self.classrole}, classrole_name={self.classrole_name}, classtransfer_degree={self.classtransfer_degree}, str={self.str}, dex={self.dex}, con={self.con}, int={self.int}, wit={self.wit}, men={self.men}, luc={self.luc}, cha={self.cha}, description={self.description})"



class ClassInfo(object):

    def __init__(self, clazz, classrole, classrole_name, classtransfer_degree, str, dex, con, int, wit, men, luc, cha, description):
        self.clazz = clazz
        self.classrole = classrole
        self.classrole_name = classrole_name
        self.classtransfer_degree = classtransfer_degree
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wit = wit
        self.men = men
        self.luc = luc
        self.cha = cha
        self.description = description

    @classmethod
    def from_string(self, line) -> 'ClassInfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['clazz', 'classrole', 'classrole_name', 'classtransfer_degree', 'str', 'dex', 'con', 'int', 'wit', 'men', 'luc', 'cha', 'description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('clazz'), data.get('classrole'), data.get('classrole_name'), data.get('classtransfer_degree'), data.get('str'), data.get('dex'), data.get('con'), data.get('int'), data.get('wit'), data.get('men'), data.get('luc'), data.get('cha'), data.get('description'))
    
    def __str__(self):
        return f"ClassInfo(clazz={self.clazz}, classrole={self.classrole}, classrole_name={self.classrole_name}, classtransfer_degree={self.classtransfer_degree}, str={self.str}, dex={self.dex}, con={self.con}, int={self.int}, wit={self.wit}, men={self.men}, luc={self.luc}, cha={self.cha}, description={self.description})"



class ClassTree(object):

    def __init__(self, id, class_list):
        self.id = id
        self.class_list = class_list

    @classmethod
    def from_string(self, line) -> 'ClassTree':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'class_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('class_list'))
    
    def __str__(self):
        return f"ClassTree(id={self.id}, class_list={self.class_list})"



class ClassTreeDesc(object):

    def __init__(self, classID, desc1, desc2):
        self.classID = classID
        self.desc1 = desc1
        self.desc2 = desc2

    @classmethod
    def from_string(self, line) -> 'ClassTreeDesc':
        split_params = line.split('\t')[1:-1]
        attributes = ['classID', 'desc1', 'desc2']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('classID'), data.get('desc1'), data.get('desc2'))
    
    def __str__(self):
        return f"ClassTreeDesc(classID={self.classID}, desc1={self.desc1}, desc2={self.desc2})"



class ClassTreeDesc(object):

    def __init__(self, classID, desc1, desc2):
        self.classID = classID
        self.desc1 = desc1
        self.desc2 = desc2

    @classmethod
    def from_string(self, line) -> 'ClassTreeDesc':
        split_params = line.split('\t')[1:-1]
        attributes = ['classID', 'desc1', 'desc2']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('classID'), data.get('desc1'), data.get('desc2'))
    
    def __str__(self):
        return f"ClassTreeDesc(classID={self.classID}, desc1={self.desc1}, desc2={self.desc2})"



class CloakLookChangeItem(object):

    def __init__(self, ItemClassID, LookItemClassID_list):
        self.ItemClassID = ItemClassID
        self.LookItemClassID_list = LookItemClassID_list

    @classmethod
    def from_string(self, line) -> 'CloakLookChangeItem':
        split_params = line.split('\t')[1:-1]
        attributes = ['ItemClassID', 'LookItemClassID_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ItemClassID'), data.get('LookItemClassID_list'))
    
    def __str__(self):
        return f"CloakLookChangeItem(ItemClassID={self.ItemClassID}, LookItemClassID_list={self.LookItemClassID_list})"



class Collection(object):

    def __init__(self, collection_ID, collection_name, main_category, period, option_id, description, items, complete_item_type, complete_skill_type, start_time, end_time, unk493):
        self.collection_ID = collection_ID
        self.collection_name = collection_name
        self.main_category = main_category
        self.period = period
        self.option_id = option_id
        self.description = description
        self.items = items
        self.complete_item_type = complete_item_type
        self.complete_skill_type = complete_skill_type
        self.start_time = start_time
        self.end_time = end_time
        self.unk493 = unk493

    @classmethod
    def from_string(self, line) -> 'Collection':
        split_params = line.split('\t')[1:-1]
        attributes = ['collection_ID', 'collection_name', 'main_category', 'period', 'option_id', 'description', 'items', 'complete_item_type', 'complete_skill_type', 'start_time', 'end_time', 'unk493']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('collection_ID'), data.get('collection_name'), data.get('main_category'), data.get('period'), data.get('option_id'), data.get('description'), data.get('items'), data.get('complete_item_type'), data.get('complete_skill_type'), data.get('start_time'), data.get('end_time'), data.get('unk493'))
    
    def __str__(self):
        return f"Collection(collection_ID={self.collection_ID}, collection_name={self.collection_name}, main_category={self.main_category}, period={self.period}, option_id={self.option_id}, description={self.description}, items={self.items}, complete_item_type={self.complete_item_type}, complete_skill_type={self.complete_skill_type}, start_time={self.start_time}, end_time={self.end_time}, unk493={self.unk493})"



class Collectionmain(object):

    def __init__(self, main_id, background_level, category, collection_id, key_item_id, key_effect):
        self.main_id = main_id
        self.background_level = background_level
        self.category = category
        self.collection_id = collection_id
        self.key_item_id = key_item_id
        self.key_effect = key_effect

    @classmethod
    def from_string(self, line) -> 'Collectionmain':
        split_params = line.split('\t')[1:-1]
        attributes = ['main_id', 'background_level', 'category', 'collection_id', 'key_item_id', 'key_effect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('main_id'), data.get('background_level'), data.get('category'), data.get('collection_id'), data.get('key_item_id'), data.get('key_effect'))
    
    def __str__(self):
        return f"Collectionmain(main_id={self.main_id}, background_level={self.background_level}, category={self.category}, collection_id={self.collection_id}, key_item_id={self.key_item_id}, key_effect={self.key_effect})"



class Collection(object):

    def __init__(self, collection_ID, collection_name, main_category, period, option_id, description, items, complete_item_type, complete_skill_type, start_time, end_time, unk493):
        self.collection_ID = collection_ID
        self.collection_name = collection_name
        self.main_category = main_category
        self.period = period
        self.option_id = option_id
        self.description = description
        self.items = items
        self.complete_item_type = complete_item_type
        self.complete_skill_type = complete_skill_type
        self.start_time = start_time
        self.end_time = end_time
        self.unk493 = unk493

    @classmethod
    def from_string(self, line) -> 'Collection':
        split_params = line.split('\t')[1:-1]
        attributes = ['collection_ID', 'collection_name', 'main_category', 'period', 'option_id', 'description', 'items', 'complete_item_type', 'complete_skill_type', 'start_time', 'end_time', 'unk493']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('collection_ID'), data.get('collection_name'), data.get('main_category'), data.get('period'), data.get('option_id'), data.get('description'), data.get('items'), data.get('complete_item_type'), data.get('complete_skill_type'), data.get('start_time'), data.get('end_time'), data.get('unk493'))
    
    def __str__(self):
        return f"Collection(collection_ID={self.collection_ID}, collection_name={self.collection_name}, main_category={self.main_category}, period={self.period}, option_id={self.option_id}, description={self.description}, items={self.items}, complete_item_type={self.complete_item_type}, complete_skill_type={self.complete_skill_type}, start_time={self.start_time}, end_time={self.end_time}, unk493={self.unk493})"



class ColorExgrp(AbstractItemInfo):

    def __init__(self, id, sorting_order, color, enable, is_event, limit, hair_id2, is_new, unk1, color_data):
        super().__init__(object_id)
        self.id = id
        self.sorting_order = sorting_order
        self.color = color
        self.enable = enable
        self.is_event = is_event
        self.limit = limit
        self.hair_id2 = hair_id2
        self.is_new = is_new
        self.unk1 = unk1
        self.color_data = color_data

    @classmethod
    def from_string(cls, line) -> 'ColorExgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'sorting_order', 'color', 'enable', 'is_event', 'limit', 'hair_id2', 'is_new', 'unk1', 'color_data']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('id'), data.get('sorting_order'), data.get('color'), data.get('enable'), data.get('is_event'), data.get('limit'), data.get('hair_id2'), data.get('is_new'), data.get('unk1'), data.get('color_data'))
    
    def __str__(self):
        return f"ColorExgrp(id={self.id}, sorting_order={self.sorting_order}, color={self.color}, enable={self.enable}, is_event={self.is_event}, limit={self.limit}, hair_id2={self.hair_id2}, is_new={self.is_new}, unk1={self.unk1}, color_data={self.color_data})"



class ColorExName(object):

    def __init__(self, hair_id, id, color_name, Description):
        self.hair_id = hair_id
        self.id = id
        self.color_name = color_name
        self.Description = Description

    @classmethod
    def from_string(self, line) -> 'ColorExName':
        split_params = line.split('\t')[1:-1]
        attributes = ['hair_id', 'id', 'color_name', 'Description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('hair_id'), data.get('id'), data.get('color_name'), data.get('Description'))
    
    def __str__(self):
        return f"ColorExName(hair_id={self.hair_id}, id={self.id}, color_name={self.color_name}, Description={self.Description})"



class CombinationItemData(object):

    def __init__(self, GroupID, AutomaticType, level, max_level, slotone, slottwo, resultitem, result_effecttype, commission):
        self.GroupID = GroupID
        self.AutomaticType = AutomaticType
        self.level = level
        self.max_level = max_level
        self.slotone = slotone
        self.slottwo = slottwo
        self.resultitem = resultitem
        self.result_effecttype = result_effecttype
        self.commission = commission

    @classmethod
    def from_string(self, line) -> 'CombinationItemData':
        split_params = line.split('\t')[1:-1]
        attributes = ['GroupID', 'AutomaticType', 'level', 'max_level', 'slotone', 'slottwo', 'resultitem', 'result_effecttype', 'commission']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('GroupID'), data.get('AutomaticType'), data.get('level'), data.get('max_level'), data.get('slotone'), data.get('slottwo'), data.get('resultitem'), data.get('result_effecttype'), data.get('commission'))
    
    def __str__(self):
        return f"CombinationItemData(GroupID={self.GroupID}, AutomaticType={self.AutomaticType}, level={self.level}, max_level={self.max_level}, slotone={self.slotone}, slottwo={self.slottwo}, resultitem={self.resultitem}, result_effecttype={self.result_effecttype}, commission={self.commission})"



class CommandName(object):

    def __init__(self, id, action, cmd):
        self.id = id
        self.action = action
        self.cmd = cmd

    @classmethod
    def from_string(self, line) -> 'CommandName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'action', 'cmd']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('action'), data.get('cmd'))
    
    def __str__(self):
        return f"CommandName(id={self.id}, action={self.action}, cmd={self.cmd})"



class CommandName(object):

    def __init__(self, id, action, cmd):
        self.id = id
        self.action = action
        self.cmd = cmd

    @classmethod
    def from_string(self, line) -> 'CommandName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'action', 'cmd']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('action'), data.get('cmd'))
    
    def __str__(self):
        return f"CommandName(id={self.id}, action={self.action}, cmd={self.cmd})"



class CommonLook(object):

    def __init__(self, item_type, item_id):
        self.item_type = item_type
        self.item_id = item_id

    @classmethod
    def from_string(self, line) -> 'CommonLook':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_type', 'item_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_type'), data.get('item_id'))
    
    def __str__(self):
        return f"CommonLook(item_type={self.item_type}, item_id={self.item_id})"



class Costume(object):

    def __init__(self, costume_id, collection_skill, costume_preview, extract_fee, costume_need_item, evolution_need_costume, origin_type, grade, applycountry):
        self.costume_id = costume_id
        self.collection_skill = collection_skill
        self.costume_preview = costume_preview
        self.extract_fee = extract_fee
        self.costume_need_item = costume_need_item
        self.evolution_need_costume = evolution_need_costume
        self.origin_type = origin_type
        self.grade = grade
        self.applycountry = applycountry

    @classmethod
    def from_string(self, line) -> 'Costume':
        split_params = line.split('\t')[1:-1]
        attributes = ['costume_id', 'collection_skill', 'costume_preview', 'extract_fee', 'costume_need_item', 'evolution_need_costume', 'origin_type', 'grade', 'applycountry']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('costume_id'), data.get('collection_skill'), data.get('costume_preview'), data.get('extract_fee'), data.get('costume_need_item'), data.get('evolution_need_costume'), data.get('origin_type'), data.get('grade'), data.get('applycountry'))
    
    def __str__(self):
        return f"Costume(costume_id={self.costume_id}, collection_skill={self.collection_skill}, costume_preview={self.costume_preview}, extract_fee={self.extract_fee}, costume_need_item={self.costume_need_item}, evolution_need_costume={self.evolution_need_costume}, origin_type={self.origin_type}, grade={self.grade}, applycountry={self.applycountry})"



class CostumeCollectionBonus(object):

    def __init__(self, need_collection_count, time, reuse, bonus1, bonus2):
        self.need_collection_count = need_collection_count
        self.time = time
        self.reuse = reuse
        self.bonus1 = bonus1
        self.bonus2 = bonus2

    @classmethod
    def from_string(self, line) -> 'CostumeCollectionBonus':
        split_params = line.split('\t')[1:-1]
        attributes = ['need_collection_count', 'time', 'reuse', 'bonus1', 'bonus2']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('need_collection_count'), data.get('time'), data.get('reuse'), data.get('bonus1'), data.get('bonus2'))
    
    def __str__(self):
        return f"CostumeCollectionBonus(need_collection_count={self.need_collection_count}, time={self.time}, reuse={self.reuse}, bonus1={self.bonus1}, bonus2={self.bonus2})"



class CostumeCollection(object):

    def __init__(self, costume_id, costume_list, collection_skill):
        self.costume_id = costume_id
        self.costume_list = costume_list
        self.collection_skill = collection_skill

    @classmethod
    def from_string(self, line) -> 'CostumeCollection':
        split_params = line.split('\t')[1:-1]
        attributes = ['costume_id', 'costume_list', 'collection_skill']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('costume_id'), data.get('costume_list'), data.get('collection_skill'))
    
    def __str__(self):
        return f"CostumeCollection(costume_id={self.costume_id}, costume_list={self.costume_list}, collection_skill={self.collection_skill})"



class Credit(object):

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

    @classmethod
    def from_string(self, line) -> 'Credit':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'comment']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('comment'))
    
    def __str__(self):
        return f"Credit(name={self.name}, comment={self.comment})"



class CubicEffectData(object):

    def __init__(self, id, effect):
        self.id = id
        self.effect = effect

    @classmethod
    def from_string(self, line) -> 'CubicEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'effect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('effect'))
    
    def __str__(self):
        return f"CubicEffectData(id={self.id}, effect={self.effect})"



class DecoNPCData(object):

    def __init__(self, id, npc_id, level, faction, type, type_desc, sub_type, sub_type_desc, cost_adena, cost_item, residence_grades, residence_domains, period, desc_id, desc_param):
        self.id = id
        self.npc_id = npc_id
        self.level = level
        self.faction = faction
        self.type = type
        self.type_desc = type_desc
        self.sub_type = sub_type
        self.sub_type_desc = sub_type_desc
        self.cost_adena = cost_adena
        self.cost_item = cost_item
        self.residence_grades = residence_grades
        self.residence_domains = residence_domains
        self.period = period
        self.desc_id = desc_id
        self.desc_param = desc_param

    @classmethod
    def from_string(self, line) -> 'DecoNPCData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'npc_id', 'level', 'faction', 'type', 'type_desc', 'sub_type', 'sub_type_desc', 'cost_adena', 'cost_item', 'residence_grades', 'residence_domains', 'period', 'desc_id', 'desc_param']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('npc_id'), data.get('level'), data.get('faction'), data.get('type'), data.get('type_desc'), data.get('sub_type'), data.get('sub_type_desc'), data.get('cost_adena'), data.get('cost_item'), data.get('residence_grades'), data.get('residence_domains'), data.get('period'), data.get('desc_id'), data.get('desc_param'))
    
    def __str__(self):
        return f"DecoNPCData(id={self.id}, npc_id={self.npc_id}, level={self.level}, faction={self.faction}, type={self.type}, type_desc={self.type_desc}, sub_type={self.sub_type}, sub_type_desc={self.sub_type_desc}, cost_adena={self.cost_adena}, cost_item={self.cost_item}, residence_grades={self.residence_grades}, residence_domains={self.residence_domains}, period={self.period}, desc_id={self.desc_id}, desc_param={self.desc_param})"



class DethroneDailyMission(object):

    def __init__(self, name, id, npc_kill_max_count, desc):
        self.name = name
        self.id = id
        self.npc_kill_max_count = npc_kill_max_count
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'DethroneDailyMission':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'id', 'npc_kill_max_count', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('id'), data.get('npc_kill_max_count'), data.get('desc'))
    
    def __str__(self):
        return f"DethroneDailyMission(name={self.name}, id={self.id}, npc_kill_max_count={self.npc_kill_max_count}, desc={self.desc})"



class DethroneDistrictName(object):

    def __init__(self, name, id, category):
        self.name = name
        self.id = id
        self.category = category

    @classmethod
    def from_string(self, line) -> 'DethroneDistrictName':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'id', 'category']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('id'), data.get('category'))
    
    def __str__(self):
        return f"DethroneDistrictName(name={self.name}, id={self.id}, category={self.category})"



class DethroneFireAbility(object):

    def __init__(self, subtype, daily_exp_up_count, daily_init_count, daily_init_cost, max_level):
        self.subtype = subtype
        self.daily_exp_up_count = daily_exp_up_count
        self.daily_init_count = daily_init_count
        self.daily_init_cost = daily_init_cost
        self.max_level = max_level

    @classmethod
    def from_string(self, line) -> 'DethroneFireAbility':
        split_params = line.split('\t')[1:-1]
        attributes = ['subtype', 'daily_exp_up_count', 'daily_init_count', 'daily_init_cost', 'max_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('subtype'), data.get('daily_exp_up_count'), data.get('daily_init_count'), data.get('daily_init_cost'), data.get('max_level'))
    
    def __str__(self):
        return f"DethroneFireAbility(subtype={self.subtype}, daily_exp_up_count={self.daily_exp_up_count}, daily_init_count={self.daily_init_count}, daily_init_cost={self.daily_init_cost}, max_level={self.max_level})"



class DethroneFireAbilityComboEffect(object):

    def __init__(self, combo_effect_level, combo_effect_title, combo_effect_list):
        self.combo_effect_level = combo_effect_level
        self.combo_effect_title = combo_effect_title
        self.combo_effect_list = combo_effect_list

    @classmethod
    def from_string(self, line) -> 'DethroneFireAbilityComboEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['combo_effect_level', 'combo_effect_title', 'combo_effect_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('combo_effect_level'), data.get('combo_effect_title'), data.get('combo_effect_list'))
    
    def __str__(self):
        return f"DethroneFireAbilityComboEffect(combo_effect_level={self.combo_effect_level}, combo_effect_title={self.combo_effect_title}, combo_effect_list={self.combo_effect_list})"



class DethroneFireAbilityLevelupInfo(object):

    def __init__(self, Subtype, Level, Exp, exp_up_cost_item, exp_up_success_rate, exp_up_amount, level_up_cost, exp_up_success_reward, SkillEffect):
        self.Subtype = Subtype
        self.Level = Level
        self.Exp = Exp
        self.exp_up_cost_item = exp_up_cost_item
        self.exp_up_success_rate = exp_up_success_rate
        self.exp_up_amount = exp_up_amount
        self.level_up_cost = level_up_cost
        self.exp_up_success_reward = exp_up_success_reward
        self.SkillEffect = SkillEffect

    @classmethod
    def from_string(self, line) -> 'DethroneFireAbilityLevelupInfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['Subtype', 'Level', 'Exp', 'exp_up_cost_item', 'exp_up_success_rate', 'exp_up_amount', 'level_up_cost', 'exp_up_success_reward', 'SkillEffect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('Subtype'), data.get('Level'), data.get('Exp'), data.get('exp_up_cost_item'), data.get('exp_up_success_rate'), data.get('exp_up_amount'), data.get('level_up_cost'), data.get('exp_up_success_reward'), data.get('SkillEffect'))
    
    def __str__(self):
        return f"DethroneFireAbilityLevelupInfo(Subtype={self.Subtype}, Level={self.Level}, Exp={self.Exp}, exp_up_cost_item={self.exp_up_cost_item}, exp_up_success_rate={self.exp_up_success_rate}, exp_up_amount={self.exp_up_amount}, level_up_cost={self.level_up_cost}, exp_up_success_reward={self.exp_up_success_reward}, SkillEffect={self.SkillEffect})"



class DethroneShop(object):

    def __init__(self, id, item_id, item_Amount, need_item_list):
        self.id = id
        self.item_id = item_id
        self.item_Amount = item_Amount
        self.need_item_list = need_item_list

    @classmethod
    def from_string(self, line) -> 'DethroneShop':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'item_id', 'item_Amount', 'need_item_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('item_id'), data.get('item_Amount'), data.get('need_item_list'))
    
    def __str__(self):
        return f"DethroneShop(id={self.id}, item_id={self.item_id}, item_Amount={self.item_Amount}, need_item_list={self.need_item_list})"



class DualCastTypeData(object):

    def __init__(self, Type, LeftAnimCombo, RightAnimCombo):
        self.Type = Type
        self.LeftAnimCombo = LeftAnimCombo
        self.RightAnimCombo = RightAnimCombo

    @classmethod
    def from_string(self, line) -> 'DualCastTypeData':
        split_params = line.split('\t')[1:-1]
        attributes = ['Type', 'LeftAnimCombo', 'RightAnimCombo']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('Type'), data.get('LeftAnimCombo'), data.get('RightAnimCombo'))
    
    def __str__(self):
        return f"DualCastTypeData(Type={self.Type}, LeftAnimCombo={self.LeftAnimCombo}, RightAnimCombo={self.RightAnimCombo})"



class Dyecombination(object):

    def __init__(self, slotone, slottwo, adena):
        self.slotone = slotone
        self.slottwo = slottwo
        self.adena = adena

    @classmethod
    def from_string(self, line) -> 'Dyecombination':
        split_params = line.split('\t')[1:-1]
        attributes = ['slotone', 'slottwo', 'adena']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('slotone'), data.get('slottwo'), data.get('adena'))
    
    def __str__(self):
        return f"Dyecombination(slotone={self.slotone}, slottwo={self.slottwo}, adena={self.adena})"



class Dyepotential(object):

    def __init__(self, dyepotential_id, dye_slot_id, max_skill_level, skill_id, effect_name):
        self.dyepotential_id = dyepotential_id
        self.dye_slot_id = dye_slot_id
        self.max_skill_level = max_skill_level
        self.skill_id = skill_id
        self.effect_name = effect_name

    @classmethod
    def from_string(self, line) -> 'Dyepotential':
        split_params = line.split('\t')[1:-1]
        attributes = ['dyepotential_id', 'dye_slot_id', 'max_skill_level', 'skill_id', 'effect_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('dyepotential_id'), data.get('dye_slot_id'), data.get('max_skill_level'), data.get('skill_id'), data.get('effect_name'))
    
    def __str__(self):
        return f"Dyepotential(dyepotential_id={self.dyepotential_id}, dye_slot_id={self.dye_slot_id}, max_skill_level={self.max_skill_level}, skill_id={self.skill_id}, effect_name={self.effect_name})"



class DyepotentialExp(object):

    def __init__(self, dyepotential_level, exp):
        self.dyepotential_level = dyepotential_level
        self.exp = exp

    @classmethod
    def from_string(self, line) -> 'DyepotentialExp':
        split_params = line.split('\t')[1:-1]
        attributes = ['dyepotential_level', 'exp']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('dyepotential_level'), data.get('exp'))
    
    def __str__(self):
        return f"DyepotentialExp(dyepotential_level={self.dyepotential_level}, exp={self.exp})"



class DyepotentialFee(object):

    def __init__(self, enchant_fee_step, daily_count, enchant_exp, upgrade_item, commission, unk493):
        self.enchant_fee_step = enchant_fee_step
        self.daily_count = daily_count
        self.enchant_exp = enchant_exp
        self.upgrade_item = upgrade_item
        self.commission = commission
        self.unk493 = unk493

    @classmethod
    def from_string(self, line) -> 'DyepotentialFee':
        split_params = line.split('\t')[1:-1]
        attributes = ['enchant_fee_step', 'daily_count', 'enchant_exp', 'upgrade_item', 'commission', 'unk493']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('enchant_fee_step'), data.get('daily_count'), data.get('enchant_exp'), data.get('upgrade_item'), data.get('commission'), data.get('unk493'))
    
    def __str__(self):
        return f"DyepotentialFee(enchant_fee_step={self.enchant_fee_step}, daily_count={self.daily_count}, enchant_exp={self.enchant_exp}, upgrade_item={self.upgrade_item}, commission={self.commission}, unk493={self.unk493})"



class DyepotentialSlotFee(object):

    def __init__(self, dye_slot, dye_level, slot_fee):
        self.dye_slot = dye_slot
        self.dye_level = dye_level
        self.slot_fee = slot_fee

    @classmethod
    def from_string(self, line) -> 'DyepotentialSlotFee':
        split_params = line.split('\t')[1:-1]
        attributes = ['dye_slot', 'dye_level', 'slot_fee']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('dye_slot'), data.get('dye_level'), data.get('slot_fee'))
    
    def __str__(self):
        return f"DyepotentialSlotFee(dye_slot={self.dye_slot}, dye_level={self.dye_level}, slot_fee={self.slot_fee})"



class DynamicContentsName(object):

    def __init__(self, ID, Title, step, Name, Tooltip, Goal_Count, UNK, GoalDescription, map):
        self.ID = ID
        self.Title = Title
        self.step = step
        self.Name = Name
        self.Tooltip = Tooltip
        self.Goal_Count = Goal_Count
        self.UNK = UNK
        self.GoalDescription = GoalDescription
        self.map = map

    @classmethod
    def from_string(self, line) -> 'DynamicContentsName':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'Title', 'step', 'Name', 'Tooltip', 'Goal_Count', 'UNK', 'GoalDescription', 'map']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('Title'), data.get('step'), data.get('Name'), data.get('Tooltip'), data.get('Goal_Count'), data.get('UNK'), data.get('GoalDescription'), data.get('map'))
    
    def __str__(self):
        return f"DynamicContentsName(ID={self.ID}, Title={self.Title}, step={self.step}, Name={self.Name}, Tooltip={self.Tooltip}, Goal_Count={self.Goal_Count}, UNK={self.UNK}, GoalDescription={self.GoalDescription}, map={self.map})"



class ElementalSpiritStat(object):

    def __init__(self, unk, evolution_id, type, level, attack, defence, crit_rate, crit_damage):
        self.unk = unk
        self.evolution_id = evolution_id
        self.type = type
        self.level = level
        self.attack = attack
        self.defence = defence
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage

    @classmethod
    def from_string(self, line) -> 'ElementalSpiritStat':
        split_params = line.split('\t')[1:-1]
        attributes = ['unk', 'evolution_id', 'type', 'level', 'attack', 'defence', 'crit_rate', 'crit_damage']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('unk'), data.get('evolution_id'), data.get('type'), data.get('level'), data.get('attack'), data.get('defence'), data.get('crit_rate'), data.get('crit_damage'))
    
    def __str__(self):
        return f"ElementalSpiritStat(unk={self.unk}, evolution_id={self.evolution_id}, type={self.type}, level={self.level}, attack={self.attack}, defence={self.defence}, crit_rate={self.crit_rate}, crit_damage={self.crit_damage})"



class ElementalSpirit(object):

    def __init__(self, level, id, npc_id, element_id, evolution_level, attack, defence, crit_rate, crit_attack, max_exp, npcstring_id):
        self.level = level
        self.id = id
        self.npc_id = npc_id
        self.element_id = element_id
        self.evolution_level = evolution_level
        self.attack = attack
        self.defence = defence
        self.crit_rate = crit_rate
        self.crit_attack = crit_attack
        self.max_exp = max_exp
        self.npcstring_id = npcstring_id

    @classmethod
    def from_string(self, line) -> 'ElementalSpirit':
        split_params = line.split('\t')[1:-1]
        attributes = ['level', 'id', 'npc_id', 'element_id', 'evolution_level', 'attack', 'defence', 'crit_rate', 'crit_attack', 'max_exp', 'npcstring_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('level'), data.get('id'), data.get('npc_id'), data.get('element_id'), data.get('evolution_level'), data.get('attack'), data.get('defence'), data.get('crit_rate'), data.get('crit_attack'), data.get('max_exp'), data.get('npcstring_id'))
    
    def __str__(self):
        return f"ElementalSpirit(level={self.level}, id={self.id}, npc_id={self.npc_id}, element_id={self.element_id}, evolution_level={self.evolution_level}, attack={self.attack}, defence={self.defence}, crit_rate={self.crit_rate}, crit_attack={self.crit_attack}, max_exp={self.max_exp}, npcstring_id={self.npcstring_id})"



class EnchantChallengePoint(object):

    def __init__(self, point_group_id, prob_inc1, prob_inc1_range, prob_inc2, prob_inc2_range, over_up, over_up_range, num_reset_prob, num_reset_range, num_down_prob, num_down_range, num_protect_prob, num_protect_range):
        self.point_group_id = point_group_id
        self.prob_inc1 = prob_inc1
        self.prob_inc1_range = prob_inc1_range
        self.prob_inc2 = prob_inc2
        self.prob_inc2_range = prob_inc2_range
        self.over_up = over_up
        self.over_up_range = over_up_range
        self.num_reset_prob = num_reset_prob
        self.num_reset_range = num_reset_range
        self.num_down_prob = num_down_prob
        self.num_down_range = num_down_range
        self.num_protect_prob = num_protect_prob
        self.num_protect_range = num_protect_range

    @classmethod
    def from_string(self, line) -> 'EnchantChallengePoint':
        split_params = line.split('\t')[1:-1]
        attributes = ['point_group_id', 'prob_inc1', 'prob_inc1_range', 'prob_inc2', 'prob_inc2_range', 'over_up', 'over_up_range', 'num_reset_prob', 'num_reset_range', 'num_down_prob', 'num_down_range', 'num_protect_prob', 'num_protect_range']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('point_group_id'), data.get('prob_inc1'), data.get('prob_inc1_range'), data.get('prob_inc2'), data.get('prob_inc2_range'), data.get('over_up'), data.get('over_up_range'), data.get('num_reset_prob'), data.get('num_reset_range'), data.get('num_down_prob'), data.get('num_down_range'), data.get('num_protect_prob'), data.get('num_protect_range'))
    
    def __str__(self):
        return f"EnchantChallengePoint(point_group_id={self.point_group_id}, prob_inc1={self.prob_inc1}, prob_inc1_range={self.prob_inc1_range}, prob_inc2={self.prob_inc2}, prob_inc2_range={self.prob_inc2_range}, over_up={self.over_up}, over_up_range={self.over_up_range}, num_reset_prob={self.num_reset_prob}, num_reset_range={self.num_reset_range}, num_down_prob={self.num_down_prob}, num_down_range={self.num_down_range}, num_protect_prob={self.num_protect_prob}, num_protect_range={self.num_protect_range})"



class EnchantChallengePointSetting(object):

    def __init__(self, max_point, max_ticket_charge, prob_inc1_fee, prob_inc2_fee, over_up_prob_fee, num_reset_prob_fee, num_down_prob_fee, num_protect_prob_fee):
        self.max_point = max_point
        self.max_ticket_charge = max_ticket_charge
        self.prob_inc1_fee = prob_inc1_fee
        self.prob_inc2_fee = prob_inc2_fee
        self.over_up_prob_fee = over_up_prob_fee
        self.num_reset_prob_fee = num_reset_prob_fee
        self.num_down_prob_fee = num_down_prob_fee
        self.num_protect_prob_fee = num_protect_prob_fee

    @classmethod
    def from_string(self, line) -> 'EnchantChallengePointSetting':
        split_params = line.split('\t')[1:-1]
        attributes = ['max_point', 'max_ticket_charge', 'prob_inc1_fee', 'prob_inc2_fee', 'over_up_prob_fee', 'num_reset_prob_fee', 'num_down_prob_fee', 'num_protect_prob_fee']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('max_point'), data.get('max_ticket_charge'), data.get('prob_inc1_fee'), data.get('prob_inc2_fee'), data.get('over_up_prob_fee'), data.get('num_reset_prob_fee'), data.get('num_down_prob_fee'), data.get('num_protect_prob_fee'))
    
    def __str__(self):
        return f"EnchantChallengePointSetting(max_point={self.max_point}, max_ticket_charge={self.max_ticket_charge}, prob_inc1_fee={self.prob_inc1_fee}, prob_inc2_fee={self.prob_inc2_fee}, over_up_prob_fee={self.over_up_prob_fee}, num_reset_prob_fee={self.num_reset_prob_fee}, num_down_prob_fee={self.num_down_prob_fee}, num_protect_prob_fee={self.num_protect_prob_fee})"



class EnchantedCloakEffectData(object):

    def __init__(self, ID, Effects):
        self.ID = ID
        self.Effects = Effects

    @classmethod
    def from_string(self, line) -> 'EnchantedCloakEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'Effects']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('Effects'))
    
    def __str__(self):
        return f"EnchantedCloakEffectData(ID={self.ID}, Effects={self.Effects})"



class EnchantedHairEffectData(object):

    def __init__(self, ID, Enchanted):
        self.ID = ID
        self.Enchanted = Enchanted

    @classmethod
    def from_string(self, line) -> 'EnchantedHairEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'Enchanted']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('Enchanted'))
    
    def __str__(self):
        return f"EnchantedHairEffectData(ID={self.ID}, Enchanted={self.Enchanted})"



class EnchantedItemSkills(object):

    def __init__(self, item_id):
        self.item_id = item_id

    @classmethod
    def from_string(self, line) -> 'EnchantedItemSkills':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'))
    
    def __str__(self):
        return f"EnchantedItemSkills(item_id={self.item_id})"



class EnchantedItemSkills(object):

    def __init__(self, item_id):
        self.item_id = item_id

    @classmethod
    def from_string(self, line) -> 'EnchantedItemSkills':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'))
    
    def __str__(self):
        return f"EnchantedItemSkills(item_id={self.item_id})"



class EnchantedWeaponFlowEffectData(object):

    def __init__(self, group_id, group_name, group):
        self.group_id = group_id
        self.group_name = group_name
        self.group = group

    @classmethod
    def from_string(self, line) -> 'EnchantedWeaponFlowEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['group_id', 'group_name', 'group']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('group_id'), data.get('group_name'), data.get('group'))
    
    def __str__(self):
        return f"EnchantedWeaponFlowEffectData(group_id={self.group_id}, group_name={self.group_name}, group={self.group})"



class EnchantScrollSet(object):

    def __init__(self, scroll_set_id, failure_base, failure_decrease, failure_maintain, failure_crush, inc_base_min, inc_base_max, great_success_effect, enchant_range_datas, enchant_group_id):
        self.scroll_set_id = scroll_set_id
        self.failure_base = failure_base
        self.failure_decrease = failure_decrease
        self.failure_maintain = failure_maintain
        self.failure_crush = failure_crush
        self.inc_base_min = inc_base_min
        self.inc_base_max = inc_base_max
        self.great_success_effect = great_success_effect
        self.enchant_range_datas = enchant_range_datas
        self.enchant_group_id = enchant_group_id

    @classmethod
    def from_string(self, line) -> 'EnchantScrollSet':
        split_params = line.split('\t')[1:-1]
        attributes = ['scroll_set_id', 'failure_base', 'failure_decrease', 'failure_maintain', 'failure_crush', 'inc_base_min', 'inc_base_max', 'great_success_effect', 'enchant_range_datas', 'enchant_group_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('scroll_set_id'), data.get('failure_base'), data.get('failure_decrease'), data.get('failure_maintain'), data.get('failure_crush'), data.get('inc_base_min'), data.get('inc_base_max'), data.get('great_success_effect'), data.get('enchant_range_datas'), data.get('enchant_group_id'))
    
    def __str__(self):
        return f"EnchantScrollSet(scroll_set_id={self.scroll_set_id}, failure_base={self.failure_base}, failure_decrease={self.failure_decrease}, failure_maintain={self.failure_maintain}, failure_crush={self.failure_crush}, inc_base_min={self.inc_base_min}, inc_base_max={self.inc_base_max}, great_success_effect={self.great_success_effect}, enchant_range_datas={self.enchant_range_datas}, enchant_group_id={self.enchant_group_id})"



class EnchantStatBonus(object):

    def __init__(self, weapon_grade, magic_weapon, unk, weapon_type, soulshotpower, spiritshotpower):
        self.weapon_grade = weapon_grade
        self.magic_weapon = magic_weapon
        self.unk = unk
        self.weapon_type = weapon_type
        self.soulshotpower = soulshotpower
        self.spiritshotpower = spiritshotpower

    @classmethod
    def from_string(self, line) -> 'EnchantStatBonus':
        split_params = line.split('\t')[1:-1]
        attributes = ['weapon_grade', 'magic_weapon', 'unk', 'weapon_type', 'soulshotpower', 'spiritshotpower']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('weapon_grade'), data.get('magic_weapon'), data.get('unk'), data.get('weapon_type'), data.get('soulshotpower'), data.get('spiritshotpower'))
    
    def __str__(self):
        return f"EnchantStatBonus(weapon_grade={self.weapon_grade}, magic_weapon={self.magic_weapon}, unk={self.unk}, weapon_type={self.weapon_type}, soulshotpower={self.soulshotpower}, spiritshotpower={self.spiritshotpower})"



class EnchantValidate(object):

    def __init__(self, enchant_add):
        self.enchant_add = enchant_add

    @classmethod
    def from_string(self, line) -> 'EnchantValidate':
        split_params = line.split('\t')[1:-1]
        attributes = ['enchant_add']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('enchant_add'))
    
    def __str__(self):
        return f"EnchantValidate(enchant_add={self.enchant_add})"



class EnchantValidateExItem(object):

    def __init__(self, enchant_add):
        self.enchant_add = enchant_add

    @classmethod
    def from_string(self, line) -> 'EnchantValidateExItem':
        split_params = line.split('\t')[1:-1]
        attributes = ['enchant_add']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('enchant_add'))
    
    def __str__(self):
        return f"EnchantValidateExItem(enchant_add={self.enchant_add})"



class EnsoulOption(object):

    def __init__(self, option_type, step, id, name, desc, extraction_itemid, icon, icon_panel):
        self.option_type = option_type
        self.step = step
        self.id = id
        self.name = name
        self.desc = desc
        self.extraction_itemid = extraction_itemid
        self.icon = icon
        self.icon_panel = icon_panel

    @classmethod
    def from_string(self, line) -> 'EnsoulOption':
        split_params = line.split('\t')[1:-1]
        attributes = ['option_type', 'step', 'id', 'name', 'desc', 'extraction_itemid', 'icon', 'icon_panel']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('option_type'), data.get('step'), data.get('id'), data.get('name'), data.get('desc'), data.get('extraction_itemid'), data.get('icon'), data.get('icon_panel'))
    
    def __str__(self):
        return f"EnsoulOption(option_type={self.option_type}, step={self.step}, id={self.id}, name={self.name}, desc={self.desc}, extraction_itemid={self.extraction_itemid}, icon={self.icon}, icon_panel={self.icon_panel})"



class EnsoulOptionClient(object):

    def __init__(self, option_type, step, id, name, desc, extraction_itemid, icon, icon_panel):
        self.option_type = option_type
        self.step = step
        self.id = id
        self.name = name
        self.desc = desc
        self.extraction_itemid = extraction_itemid
        self.icon = icon
        self.icon_panel = icon_panel

    @classmethod
    def from_string(self, line) -> 'EnsoulOptionClient':
        split_params = line.split('\t')[1:-1]
        attributes = ['option_type', 'step', 'id', 'name', 'desc', 'extraction_itemid', 'icon', 'icon_panel']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('option_type'), data.get('step'), data.get('id'), data.get('name'), data.get('desc'), data.get('extraction_itemid'), data.get('icon'), data.get('icon_panel'))
    
    def __str__(self):
        return f"EnsoulOptionClient(option_type={self.option_type}, step={self.step}, id={self.id}, name={self.name}, desc={self.desc}, extraction_itemid={self.extraction_itemid}, icon={self.icon}, icon_panel={self.icon_panel})"



class EnsoulStone(object):

    def __init__(self, id, slot_type, ensoul_fee, ensoul_refee, ensoul_extraction, ensoul_option_list_legs, ensoul_option_list_feet, ensoul_option_list_head, ensoul_option_list_gloves, ensoul_option_list_onepiece, ensoul_option_list_chest, ensoul_option_list_finger, ensoul_option_list_ear, ensoul_option_list_neck, ensoul_option_list_shield, ensoul_option_list_sigil, ensoul_option_list_weapon):
        self.id = id
        self.slot_type = slot_type
        self.ensoul_fee = ensoul_fee
        self.ensoul_refee = ensoul_refee
        self.ensoul_extraction = ensoul_extraction
        self.ensoul_option_list_legs = ensoul_option_list_legs
        self.ensoul_option_list_feet = ensoul_option_list_feet
        self.ensoul_option_list_head = ensoul_option_list_head
        self.ensoul_option_list_gloves = ensoul_option_list_gloves
        self.ensoul_option_list_onepiece = ensoul_option_list_onepiece
        self.ensoul_option_list_chest = ensoul_option_list_chest
        self.ensoul_option_list_finger = ensoul_option_list_finger
        self.ensoul_option_list_ear = ensoul_option_list_ear
        self.ensoul_option_list_neck = ensoul_option_list_neck
        self.ensoul_option_list_shield = ensoul_option_list_shield
        self.ensoul_option_list_sigil = ensoul_option_list_sigil
        self.ensoul_option_list_weapon = ensoul_option_list_weapon

    @classmethod
    def from_string(self, line) -> 'EnsoulStone':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'slot_type', 'ensoul_fee', 'ensoul_refee', 'ensoul_extraction', 'ensoul_option_list_legs', 'ensoul_option_list_feet', 'ensoul_option_list_head', 'ensoul_option_list_gloves', 'ensoul_option_list_onepiece', 'ensoul_option_list_chest', 'ensoul_option_list_finger', 'ensoul_option_list_ear', 'ensoul_option_list_neck', 'ensoul_option_list_shield', 'ensoul_option_list_sigil', 'ensoul_option_list_weapon']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('slot_type'), data.get('ensoul_fee'), data.get('ensoul_refee'), data.get('ensoul_extraction'), data.get('ensoul_option_list_legs'), data.get('ensoul_option_list_feet'), data.get('ensoul_option_list_head'), data.get('ensoul_option_list_gloves'), data.get('ensoul_option_list_onepiece'), data.get('ensoul_option_list_chest'), data.get('ensoul_option_list_finger'), data.get('ensoul_option_list_ear'), data.get('ensoul_option_list_neck'), data.get('ensoul_option_list_shield'), data.get('ensoul_option_list_sigil'), data.get('ensoul_option_list_weapon'))
    
    def __str__(self):
        return f"EnsoulStone(id={self.id}, slot_type={self.slot_type}, ensoul_fee={self.ensoul_fee}, ensoul_refee={self.ensoul_refee}, ensoul_extraction={self.ensoul_extraction}, ensoul_option_list_legs={self.ensoul_option_list_legs}, ensoul_option_list_feet={self.ensoul_option_list_feet}, ensoul_option_list_head={self.ensoul_option_list_head}, ensoul_option_list_gloves={self.ensoul_option_list_gloves}, ensoul_option_list_onepiece={self.ensoul_option_list_onepiece}, ensoul_option_list_chest={self.ensoul_option_list_chest}, ensoul_option_list_finger={self.ensoul_option_list_finger}, ensoul_option_list_ear={self.ensoul_option_list_ear}, ensoul_option_list_neck={self.ensoul_option_list_neck}, ensoul_option_list_shield={self.ensoul_option_list_shield}, ensoul_option_list_sigil={self.ensoul_option_list_sigil}, ensoul_option_list_weapon={self.ensoul_option_list_weapon})"



class EnsoulStoneClient(object):

    def __init__(self, id, slot_type, ensoul_fee, ensoul_refee, ensoul_extraction, ensoul_option_list_legs, ensoul_option_list_feet, ensoul_option_list_head, ensoul_option_list_gloves, ensoul_option_list_onepiece, ensoul_option_list_chest, ensoul_option_list_finger, ensoul_option_list_ear, ensoul_option_list_neck, ensoul_option_list_shield, ensoul_option_list_sigil, ensoul_option_list_weapon):
        self.id = id
        self.slot_type = slot_type
        self.ensoul_fee = ensoul_fee
        self.ensoul_refee = ensoul_refee
        self.ensoul_extraction = ensoul_extraction
        self.ensoul_option_list_legs = ensoul_option_list_legs
        self.ensoul_option_list_feet = ensoul_option_list_feet
        self.ensoul_option_list_head = ensoul_option_list_head
        self.ensoul_option_list_gloves = ensoul_option_list_gloves
        self.ensoul_option_list_onepiece = ensoul_option_list_onepiece
        self.ensoul_option_list_chest = ensoul_option_list_chest
        self.ensoul_option_list_finger = ensoul_option_list_finger
        self.ensoul_option_list_ear = ensoul_option_list_ear
        self.ensoul_option_list_neck = ensoul_option_list_neck
        self.ensoul_option_list_shield = ensoul_option_list_shield
        self.ensoul_option_list_sigil = ensoul_option_list_sigil
        self.ensoul_option_list_weapon = ensoul_option_list_weapon

    @classmethod
    def from_string(self, line) -> 'EnsoulStoneClient':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'slot_type', 'ensoul_fee', 'ensoul_refee', 'ensoul_extraction', 'ensoul_option_list_legs', 'ensoul_option_list_feet', 'ensoul_option_list_head', 'ensoul_option_list_gloves', 'ensoul_option_list_onepiece', 'ensoul_option_list_chest', 'ensoul_option_list_finger', 'ensoul_option_list_ear', 'ensoul_option_list_neck', 'ensoul_option_list_shield', 'ensoul_option_list_sigil', 'ensoul_option_list_weapon']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('slot_type'), data.get('ensoul_fee'), data.get('ensoul_refee'), data.get('ensoul_extraction'), data.get('ensoul_option_list_legs'), data.get('ensoul_option_list_feet'), data.get('ensoul_option_list_head'), data.get('ensoul_option_list_gloves'), data.get('ensoul_option_list_onepiece'), data.get('ensoul_option_list_chest'), data.get('ensoul_option_list_finger'), data.get('ensoul_option_list_ear'), data.get('ensoul_option_list_neck'), data.get('ensoul_option_list_shield'), data.get('ensoul_option_list_sigil'), data.get('ensoul_option_list_weapon'))
    
    def __str__(self):
        return f"EnsoulStoneClient(id={self.id}, slot_type={self.slot_type}, ensoul_fee={self.ensoul_fee}, ensoul_refee={self.ensoul_refee}, ensoul_extraction={self.ensoul_extraction}, ensoul_option_list_legs={self.ensoul_option_list_legs}, ensoul_option_list_feet={self.ensoul_option_list_feet}, ensoul_option_list_head={self.ensoul_option_list_head}, ensoul_option_list_gloves={self.ensoul_option_list_gloves}, ensoul_option_list_onepiece={self.ensoul_option_list_onepiece}, ensoul_option_list_chest={self.ensoul_option_list_chest}, ensoul_option_list_finger={self.ensoul_option_list_finger}, ensoul_option_list_ear={self.ensoul_option_list_ear}, ensoul_option_list_neck={self.ensoul_option_list_neck}, ensoul_option_list_shield={self.ensoul_option_list_shield}, ensoul_option_list_sigil={self.ensoul_option_list_sigil}, ensoul_option_list_weapon={self.ensoul_option_list_weapon})"



class EnterEventgrp(AbstractItemInfo):

    def __init__(self, id, sound_name, sound_vol, sound_rad, isrise, spawn_type, unk493_1, unk493_2, unk493_3, effect_name, anim_name):
        super().__init__(object_id)
        self.id = id
        self.sound_name = sound_name
        self.sound_vol = sound_vol
        self.sound_rad = sound_rad
        self.isrise = isrise
        self.spawn_type = spawn_type
        self.unk493_1 = unk493_1
        self.unk493_2 = unk493_2
        self.unk493_3 = unk493_3
        self.effect_name = effect_name
        self.anim_name = anim_name

    @classmethod
    def from_string(cls, line) -> 'EnterEventgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'sound_name', 'sound_vol', 'sound_rad', 'isrise', 'spawn_type', 'unk493_1', 'unk493_2', 'unk493_3', 'effect_name', 'anim_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('id'), data.get('sound_name'), data.get('sound_vol'), data.get('sound_rad'), data.get('isrise'), data.get('spawn_type'), data.get('unk493_1'), data.get('unk493_2'), data.get('unk493_3'), data.get('effect_name'), data.get('anim_name'))
    
    def __str__(self):
        return f"EnterEventgrp(id={self.id}, sound_name={self.sound_name}, sound_vol={self.sound_vol}, sound_rad={self.sound_rad}, isrise={self.isrise}, spawn_type={self.spawn_type}, unk493_1={self.unk493_1}, unk493_2={self.unk493_2}, unk493_3={self.unk493_3}, effect_name={self.effect_name}, anim_name={self.anim_name})"



class Equipaddoption(object):

    def __init__(self, item_id, id, type, required_enchant, add_option):
        self.item_id = item_id
        self.id = id
        self.type = type
        self.required_enchant = required_enchant
        self.add_option = add_option

    @classmethod
    def from_string(self, line) -> 'Equipaddoption':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'id', 'type', 'required_enchant', 'add_option']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('id'), data.get('type'), data.get('required_enchant'), data.get('add_option'))
    
    def __str__(self):
        return f"Equipaddoption(item_id={self.item_id}, id={self.id}, type={self.type}, required_enchant={self.required_enchant}, add_option={self.add_option})"



class EtcItemgrp(AbstractItemInfo):

    def __init__(self, tag, object_id, drop_type, drop_anim_type, drop_radius, drop_height, drop_texture, icon, durability, weight, material_type, crystallizable, related_quest_id, color, is_attribution, icon_panel, complete_item_dropsound_type, inventory_type, mesh, texture, drop_sound, equip_sound, consume_type, etcitem_type, crystal_type, scroll_set_id):
        super().__init__(object_id)
        self.tag = tag
        self.object_id = object_id
        self.drop_type = drop_type
        self.drop_anim_type = drop_anim_type
        self.drop_radius = drop_radius
        self.drop_height = drop_height
        self.drop_texture = drop_texture
        self.icon = icon
        self.durability = durability
        self.weight = weight
        self.material_type = material_type
        self.crystallizable = crystallizable
        self.related_quest_id = related_quest_id
        self.color = color
        self.is_attribution = is_attribution
        self.icon_panel = icon_panel
        self.complete_item_dropsound_type = complete_item_dropsound_type
        self.inventory_type = inventory_type
        self.mesh = mesh
        self.texture = texture
        self.drop_sound = drop_sound
        self.equip_sound = equip_sound
        self.consume_type = consume_type
        self.etcitem_type = etcitem_type
        self.crystal_type = crystal_type
        self.scroll_set_id = scroll_set_id

    @classmethod
    def from_string(cls, line) -> 'EtcItemgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['tag', 'object_id', 'drop_type', 'drop_anim_type', 'drop_radius', 'drop_height', 'drop_texture', 'icon', 'durability', 'weight', 'material_type', 'crystallizable', 'related_quest_id', 'color', 'is_attribution', 'icon_panel', 'complete_item_dropsound_type', 'inventory_type', 'mesh', 'texture', 'drop_sound', 'equip_sound', 'consume_type', 'etcitem_type', 'crystal_type', 'scroll_set_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('tag'), data.get('object_id'), data.get('drop_type'), data.get('drop_anim_type'), data.get('drop_radius'), data.get('drop_height'), data.get('drop_texture'), data.get('icon'), data.get('durability'), data.get('weight'), data.get('material_type'), data.get('crystallizable'), data.get('related_quest_id'), data.get('color'), data.get('is_attribution'), data.get('icon_panel'), data.get('complete_item_dropsound_type'), data.get('inventory_type'), data.get('mesh'), data.get('texture'), data.get('drop_sound'), data.get('equip_sound'), data.get('consume_type'), data.get('etcitem_type'), data.get('crystal_type'), data.get('scroll_set_id'))
    
    def __str__(self):
        return f"EtcItemgrp(tag={self.tag}, object_id={self.object_id}, drop_type={self.drop_type}, drop_anim_type={self.drop_anim_type}, drop_radius={self.drop_radius}, drop_height={self.drop_height}, drop_texture={self.drop_texture}, icon={self.icon}, durability={self.durability}, weight={self.weight}, material_type={self.material_type}, crystallizable={self.crystallizable}, related_quest_id={self.related_quest_id}, color={self.color}, is_attribution={self.is_attribution}, icon_panel={self.icon_panel}, complete_item_dropsound_type={self.complete_item_dropsound_type}, inventory_type={self.inventory_type}, mesh={self.mesh}, texture={self.texture}, drop_sound={self.drop_sound}, equip_sound={self.equip_sound}, consume_type={self.consume_type}, etcitem_type={self.etcitem_type}, crystal_type={self.crystal_type}, scroll_set_id={self.scroll_set_id})"

    def get_item_type(self):
        return self.etcitem_type

    def get_material(self):
        return self.material_type

    def get_weight(self):
        return self.weight

    def get_consume_type(self):
        return self.consume_type

    def get_icon(self):
        return self.icon

class EtcStatusData(object):

    def __init__(self, skill_id, fixed_level):
        self.skill_id = skill_id
        self.fixed_level = fixed_level

    @classmethod
    def from_string(self, line) -> 'EtcStatusData':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'fixed_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('fixed_level'))
    
    def __str__(self):
        return f"EtcStatusData(skill_id={self.skill_id}, fixed_level={self.fixed_level})"



class EULA(object):

    def __init__(self, eula, eulaRGB_TESTserver, eulachinaspecialmessage, eulachinapkagreement):
        self.eula = eula
        self.eulaRGB_TESTserver = eulaRGB_TESTserver
        self.eulachinaspecialmessage = eulachinaspecialmessage
        self.eulachinapkagreement = eulachinapkagreement

    @classmethod
    def from_string(self, line) -> 'EULA':
        split_params = line.split('\t')[1:-1]
        attributes = ['eula', 'eulaRGB_TESTserver', 'eulachinaspecialmessage', 'eulachinapkagreement']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('eula'), data.get('eulaRGB_TESTserver'), data.get('eulachinaspecialmessage'), data.get('eulachinapkagreement'))
    
    def __str__(self):
        return f"EULA(eula={self.eula}, eulaRGB_TESTserver={self.eulaRGB_TESTserver}, eulachinaspecialmessage={self.eulachinaspecialmessage}, eulachinapkagreement={self.eulachinapkagreement})"



class EventAlarmList(object):

    def __init__(self, event_id, event_type, event_icon, event_title, start_date, start_time, end_date, end_time, activate_time, deactivate_time, event_day, event_desc):
        self.event_id = event_id
        self.event_type = event_type
        self.event_icon = event_icon
        self.event_title = event_title
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.activate_time = activate_time
        self.deactivate_time = deactivate_time
        self.event_day = event_day
        self.event_desc = event_desc

    @classmethod
    def from_string(self, line) -> 'EventAlarmList':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_id', 'event_type', 'event_icon', 'event_title', 'start_date', 'start_time', 'end_date', 'end_time', 'activate_time', 'deactivate_time', 'event_day', 'event_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_id'), data.get('event_type'), data.get('event_icon'), data.get('event_title'), data.get('start_date'), data.get('start_time'), data.get('end_date'), data.get('end_time'), data.get('activate_time'), data.get('deactivate_time'), data.get('event_day'), data.get('event_desc'))
    
    def __str__(self):
        return f"EventAlarmList(event_id={self.event_id}, event_type={self.event_type}, event_icon={self.event_icon}, event_title={self.event_title}, start_date={self.start_date}, start_time={self.start_time}, end_date={self.end_date}, end_time={self.end_time}, activate_time={self.activate_time}, deactivate_time={self.deactivate_time}, event_day={self.event_day}, event_desc={self.event_desc})"



class EventAlarmList(object):

    def __init__(self, event_id, event_type, event_icon, event_title, start_date, start_time, end_date, end_time, activate_time, deactivate_time, event_day, event_desc):
        self.event_id = event_id
        self.event_type = event_type
        self.event_icon = event_icon
        self.event_title = event_title
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.activate_time = activate_time
        self.deactivate_time = deactivate_time
        self.event_day = event_day
        self.event_desc = event_desc

    @classmethod
    def from_string(self, line) -> 'EventAlarmList':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_id', 'event_type', 'event_icon', 'event_title', 'start_date', 'start_time', 'end_date', 'end_time', 'activate_time', 'deactivate_time', 'event_day', 'event_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_id'), data.get('event_type'), data.get('event_icon'), data.get('event_title'), data.get('start_date'), data.get('start_time'), data.get('end_date'), data.get('end_time'), data.get('activate_time'), data.get('deactivate_time'), data.get('event_day'), data.get('event_desc'))
    
    def __str__(self):
        return f"EventAlarmList(event_id={self.event_id}, event_type={self.event_type}, event_icon={self.event_icon}, event_title={self.event_title}, start_date={self.start_date}, start_time={self.start_time}, end_date={self.end_date}, end_time={self.end_time}, activate_time={self.activate_time}, deactivate_time={self.deactivate_time}, event_day={self.event_day}, event_desc={self.event_desc})"



class EventContentsGoalName(object):

    def __init__(self, ID, Name, Tooltip, Goal_Count, UNK, GoalDescription, map):
        self.ID = ID
        self.Name = Name
        self.Tooltip = Tooltip
        self.Goal_Count = Goal_Count
        self.UNK = UNK
        self.GoalDescription = GoalDescription
        self.map = map

    @classmethod
    def from_string(self, line) -> 'EventContentsGoalName':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'Name', 'Tooltip', 'Goal_Count', 'UNK', 'GoalDescription', 'map']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('Name'), data.get('Tooltip'), data.get('Goal_Count'), data.get('UNK'), data.get('GoalDescription'), data.get('map'))
    
    def __str__(self):
        return f"EventContentsGoalName(ID={self.ID}, Name={self.Name}, Tooltip={self.Tooltip}, Goal_Count={self.Goal_Count}, UNK={self.UNK}, GoalDescription={self.GoalDescription}, map={self.map})"



class EventContentsName(object):

    def __init__(self, ID, Title, step, GroupIDs):
        self.ID = ID
        self.Title = Title
        self.step = step
        self.GroupIDs = GroupIDs

    @classmethod
    def from_string(self, line) -> 'EventContentsName':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'Title', 'step', 'GroupIDs']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('Title'), data.get('step'), data.get('GroupIDs'))
    
    def __str__(self):
        return f"EventContentsName(ID={self.ID}, Title={self.Title}, step={self.step}, GroupIDs={self.GroupIDs})"



class EventHtml(object):

    def __init__(self, id, title, desc):
        self.id = id
        self.title = title
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'EventHtml':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'title', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('title'), data.get('desc'))
    
    def __str__(self):
        return f"EventHtml(id={self.id}, title={self.title}, desc={self.desc})"



class EventHtml(object):

    def __init__(self, id, title, desc):
        self.id = id
        self.title = title
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'EventHtml':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'title', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('title'), data.get('desc'))
    
    def __str__(self):
        return f"EventHtml(id={self.id}, title={self.title}, desc={self.desc})"



class EventLookChange(object):

    def __init__(self, event_ave_id, priority, change_weapon, unk_388_1, attackitem_enchant, change_back, change_armor, standard_item_slot, need_equipped, change_accessory, ignore_beautyshop, none, sword, blunt, dagger, pole, fist, bow, etc, dual, dualfist, fishingrod, rapier, crossbow, ancientsword, flag, dualdagger, ownthing, twohandcrossbow, dualblunt, twohandsword, twohandblunt, mage_sword, mage_blunt, mage_twohandsword, mage_twohandblunt, unk, shooter, shield, sigil, armor1, armor2, armor3, armor4, back, hair, accessory, exceptionItem):
        self.event_ave_id = event_ave_id
        self.priority = priority
        self.change_weapon = change_weapon
        self.unk_388_1 = unk_388_1
        self.attackitem_enchant = attackitem_enchant
        self.change_back = change_back
        self.change_armor = change_armor
        self.standard_item_slot = standard_item_slot
        self.need_equipped = need_equipped
        self.change_accessory = change_accessory
        self.ignore_beautyshop = ignore_beautyshop
        self.none = none
        self.sword = sword
        self.blunt = blunt
        self.dagger = dagger
        self.pole = pole
        self.fist = fist
        self.bow = bow
        self.etc = etc
        self.dual = dual
        self.dualfist = dualfist
        self.fishingrod = fishingrod
        self.rapier = rapier
        self.crossbow = crossbow
        self.ancientsword = ancientsword
        self.flag = flag
        self.dualdagger = dualdagger
        self.ownthing = ownthing
        self.twohandcrossbow = twohandcrossbow
        self.dualblunt = dualblunt
        self.twohandsword = twohandsword
        self.twohandblunt = twohandblunt
        self.mage_sword = mage_sword
        self.mage_blunt = mage_blunt
        self.mage_twohandsword = mage_twohandsword
        self.mage_twohandblunt = mage_twohandblunt
        self.unk = unk
        self.shooter = shooter
        self.shield = shield
        self.sigil = sigil
        self.armor1 = armor1
        self.armor2 = armor2
        self.armor3 = armor3
        self.armor4 = armor4
        self.back = back
        self.hair = hair
        self.accessory = accessory
        self.exceptionItem = exceptionItem

    @classmethod
    def from_string(self, line) -> 'EventLookChange':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_ave_id', 'priority', 'change_weapon', 'unk_388_1', 'attackitem_enchant', 'change_back', 'change_armor', 'standard_item_slot', 'need_equipped', 'change_accessory', 'ignore_beautyshop', 'none', 'sword', 'blunt', 'dagger', 'pole', 'fist', 'bow', 'etc', 'dual', 'dualfist', 'fishingrod', 'rapier', 'crossbow', 'ancientsword', 'flag', 'dualdagger', 'ownthing', 'twohandcrossbow', 'dualblunt', 'twohandsword', 'twohandblunt', 'mage_sword', 'mage_blunt', 'mage_twohandsword', 'mage_twohandblunt', 'unk', 'shooter', 'shield', 'sigil', 'armor1', 'armor2', 'armor3', 'armor4', 'back', 'hair', 'accessory', 'exceptionItem']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_ave_id'), data.get('priority'), data.get('change_weapon'), data.get('unk_388_1'), data.get('attackitem_enchant'), data.get('change_back'), data.get('change_armor'), data.get('standard_item_slot'), data.get('need_equipped'), data.get('change_accessory'), data.get('ignore_beautyshop'), data.get('none'), data.get('sword'), data.get('blunt'), data.get('dagger'), data.get('pole'), data.get('fist'), data.get('bow'), data.get('etc'), data.get('dual'), data.get('dualfist'), data.get('fishingrod'), data.get('rapier'), data.get('crossbow'), data.get('ancientsword'), data.get('flag'), data.get('dualdagger'), data.get('ownthing'), data.get('twohandcrossbow'), data.get('dualblunt'), data.get('twohandsword'), data.get('twohandblunt'), data.get('mage_sword'), data.get('mage_blunt'), data.get('mage_twohandsword'), data.get('mage_twohandblunt'), data.get('unk'), data.get('shooter'), data.get('shield'), data.get('sigil'), data.get('armor1'), data.get('armor2'), data.get('armor3'), data.get('armor4'), data.get('back'), data.get('hair'), data.get('accessory'), data.get('exceptionItem'))
    
    def __str__(self):
        return f"EventLookChange(event_ave_id={self.event_ave_id}, priority={self.priority}, change_weapon={self.change_weapon}, unk_388_1={self.unk_388_1}, attackitem_enchant={self.attackitem_enchant}, change_back={self.change_back}, change_armor={self.change_armor}, standard_item_slot={self.standard_item_slot}, need_equipped={self.need_equipped}, change_accessory={self.change_accessory}, ignore_beautyshop={self.ignore_beautyshop}, none={self.none}, sword={self.sword}, blunt={self.blunt}, dagger={self.dagger}, pole={self.pole}, fist={self.fist}, bow={self.bow}, etc={self.etc}, dual={self.dual}, dualfist={self.dualfist}, fishingrod={self.fishingrod}, rapier={self.rapier}, crossbow={self.crossbow}, ancientsword={self.ancientsword}, flag={self.flag}, dualdagger={self.dualdagger}, ownthing={self.ownthing}, twohandcrossbow={self.twohandcrossbow}, dualblunt={self.dualblunt}, twohandsword={self.twohandsword}, twohandblunt={self.twohandblunt}, mage_sword={self.mage_sword}, mage_blunt={self.mage_blunt}, mage_twohandsword={self.mage_twohandsword}, mage_twohandblunt={self.mage_twohandblunt}, unk={self.unk}, shooter={self.shooter}, shield={self.shield}, sigil={self.sigil}, armor1={self.armor1}, armor2={self.armor2}, armor3={self.armor3}, armor4={self.armor4}, back={self.back}, hair={self.hair}, accessory={self.accessory}, exceptionItem={self.exceptionItem})"



class ExceptionMinimapData(object):

    def __init__(self, location_id, location_name, max_x, min_x, max_y, min_y, max_z, min_z, seen_x, seen_y, continent):
        self.location_id = location_id
        self.location_name = location_name
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y
        self.max_z = max_z
        self.min_z = min_z
        self.seen_x = seen_x
        self.seen_y = seen_y
        self.continent = continent

    @classmethod
    def from_string(self, line) -> 'ExceptionMinimapData':
        split_params = line.split('\t')[1:-1]
        attributes = ['location_id', 'location_name', 'max_x', 'min_x', 'max_y', 'min_y', 'max_z', 'min_z', 'seen_x', 'seen_y', 'continent']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('location_id'), data.get('location_name'), data.get('max_x'), data.get('min_x'), data.get('max_y'), data.get('min_y'), data.get('max_z'), data.get('min_z'), data.get('seen_x'), data.get('seen_y'), data.get('continent'))
    
    def __str__(self):
        return f"ExceptionMinimapData(location_id={self.location_id}, location_name={self.location_name}, max_x={self.max_x}, min_x={self.min_x}, max_y={self.max_y}, min_y={self.min_y}, max_z={self.max_z}, min_z={self.min_z}, seen_x={self.seen_x}, seen_y={self.seen_y}, continent={self.continent})"



class Exoptiondata(object):

    def __init__(self, last_option):
        self.last_option = last_option

    @classmethod
    def from_string(self, line) -> 'Exoptiondata':
        split_params = line.split('\t')[1:-1]
        attributes = ['last_option']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('last_option'))
    
    def __str__(self):
        return f"Exoptiondata(last_option={self.last_option})"



class Faceexgrp(AbstractItemInfo):

    def __init__(self, error):
        super().__init__()
        self.error = error

    @classmethod
    def from_string(cls, line) -> 'Faceexgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['error']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('error'))
    
    def __str__(self):
        return f"Faceexgrp(error={self.error})"



class FaceExName(object):

    def __init__(self, id, class_name, face_name, Description):
        self.id = id
        self.class_name = class_name
        self.face_name = face_name
        self.Description = Description

    @classmethod
    def from_string(self, line) -> 'FaceExName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'class_name', 'face_name', 'Description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('class_name'), data.get('face_name'), data.get('Description'))
    
    def __str__(self):
        return f"FaceExName(id={self.id}, class_name={self.class_name}, face_name={self.face_name}, Description={self.Description})"



class FactionName(object):

    def __init__(self, faction_id, faction_name, emblem_texture, emblem_big_texture, faction_desc, faction_npc, faction_area, regionid, monsterbook_use, level_count):
        self.faction_id = faction_id
        self.faction_name = faction_name
        self.emblem_texture = emblem_texture
        self.emblem_big_texture = emblem_big_texture
        self.faction_desc = faction_desc
        self.faction_npc = faction_npc
        self.faction_area = faction_area
        self.regionid = regionid
        self.monsterbook_use = monsterbook_use
        self.level_count = level_count

    @classmethod
    def from_string(self, line) -> 'FactionName':
        split_params = line.split('\t')[1:-1]
        attributes = ['faction_id', 'faction_name', 'emblem_texture', 'emblem_big_texture', 'faction_desc', 'faction_npc', 'faction_area', 'regionid', 'monsterbook_use', 'level_count']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('faction_id'), data.get('faction_name'), data.get('emblem_texture'), data.get('emblem_big_texture'), data.get('faction_desc'), data.get('faction_npc'), data.get('faction_area'), data.get('regionid'), data.get('monsterbook_use'), data.get('level_count'))
    
    def __str__(self):
        return f"FactionName(faction_id={self.faction_id}, faction_name={self.faction_name}, emblem_texture={self.emblem_texture}, emblem_big_texture={self.emblem_big_texture}, faction_desc={self.faction_desc}, faction_npc={self.faction_npc}, faction_area={self.faction_area}, regionid={self.regionid}, monsterbook_use={self.monsterbook_use}, level_count={self.level_count})"



class FlyMoveName(object):

    def __init__(self, path, node, name):
        self.path = path
        self.node = node
        self.name = name

    @classmethod
    def from_string(self, line) -> 'FlyMoveName':
        split_params = line.split('\t')[1:-1]
        attributes = ['path', 'node', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('path'), data.get('node'), data.get('name'))
    
    def __str__(self):
        return f"FlyMoveName(path={self.path}, node={self.node}, name={self.name})"



class FlyMoveName(object):

    def __init__(self, path, node, name):
        self.path = path
        self.node = node
        self.name = name

    @classmethod
    def from_string(self, line) -> 'FlyMoveName':
        split_params = line.split('\t')[1:-1]
        attributes = ['path', 'node', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('path'), data.get('node'), data.get('name'))
    
    def __str__(self):
        return f"FlyMoveName(path={self.path}, node={self.node}, name={self.name})"



class FullArmorEnchantEffectData(object):

    def __init__(self, effect_type, unk, min_enchant_num, noise_scale, noise_pan_speed, noise_rate, extrude_scale, edge_peak, edge_sharp, min_color, max_color, show_type):
        self.effect_type = effect_type
        self.unk = unk
        self.min_enchant_num = min_enchant_num
        self.noise_scale = noise_scale
        self.noise_pan_speed = noise_pan_speed
        self.noise_rate = noise_rate
        self.extrude_scale = extrude_scale
        self.edge_peak = edge_peak
        self.edge_sharp = edge_sharp
        self.min_color = min_color
        self.max_color = max_color
        self.show_type = show_type

    @classmethod
    def from_string(self, line) -> 'FullArmorEnchantEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['effect_type', 'unk', 'min_enchant_num', 'noise_scale', 'noise_pan_speed', 'noise_rate', 'extrude_scale', 'edge_peak', 'edge_sharp', 'min_color', 'max_color', 'show_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('effect_type'), data.get('unk'), data.get('min_enchant_num'), data.get('noise_scale'), data.get('noise_pan_speed'), data.get('noise_rate'), data.get('extrude_scale'), data.get('edge_peak'), data.get('edge_sharp'), data.get('min_color'), data.get('max_color'), data.get('show_type'))
    
    def __str__(self):
        return f"FullArmorEnchantEffectData(effect_type={self.effect_type}, unk={self.unk}, min_enchant_num={self.min_enchant_num}, noise_scale={self.noise_scale}, noise_pan_speed={self.noise_pan_speed}, noise_rate={self.noise_rate}, extrude_scale={self.extrude_scale}, edge_peak={self.edge_peak}, edge_sharp={self.edge_sharp}, min_color={self.min_color}, max_color={self.max_color}, show_type={self.show_type})"



class GameDataBase(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @classmethod
    def from_string(self, line) -> 'GameDataBase':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('type'))
    
    def __str__(self):
        return f"GameDataBase(name={self.name}, type={self.type})"



class GameDataBase(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    @classmethod
    def from_string(self, line) -> 'GameDataBase':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('type'))
    
    def __str__(self):
        return f"GameDataBase(name={self.name}, type={self.type})"



class GamePlayData(object):

    def __init__(self, error):
        self.error = error

    @classmethod
    def from_string(self, line) -> 'GamePlayData':
        split_params = line.split('\t')[1:-1]
        attributes = ['error']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('error'))
    
    def __str__(self):
        return f"GamePlayData(error={self.error})"



class GameTip(object):

    def __init__(self, id, priority, target_lv, validity, tip_msg, tip_img):
        self.id = id
        self.priority = priority
        self.target_lv = target_lv
        self.validity = validity
        self.tip_msg = tip_msg
        self.tip_img = tip_img

    @classmethod
    def from_string(self, line) -> 'GameTip':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'priority', 'target_lv', 'validity', 'tip_msg', 'tip_img']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('priority'), data.get('target_lv'), data.get('validity'), data.get('tip_msg'), data.get('tip_img'))
    
    def __str__(self):
        return f"GameTip(id={self.id}, priority={self.priority}, target_lv={self.target_lv}, validity={self.validity}, tip_msg={self.tip_msg}, tip_img={self.tip_img})"



class GameTip(object):

    def __init__(self, id, priority, target_lv, validity, tip_msg, tip_img):
        self.id = id
        self.priority = priority
        self.target_lv = target_lv
        self.validity = validity
        self.tip_msg = tip_msg
        self.tip_img = tip_img

    @classmethod
    def from_string(self, line) -> 'GameTip':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'priority', 'target_lv', 'validity', 'tip_msg', 'tip_img']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('priority'), data.get('target_lv'), data.get('validity'), data.get('tip_msg'), data.get('tip_img'))
    
    def __str__(self):
        return f"GameTip(id={self.id}, priority={self.priority}, target_lv={self.target_lv}, validity={self.validity}, tip_msg={self.tip_msg}, tip_img={self.tip_img})"



class GCShop(object):

    def __init__(self, shop_id, group_id, group_prob, roll_cost, pick_cost, item_list):
        self.shop_id = shop_id
        self.group_id = group_id
        self.group_prob = group_prob
        self.roll_cost = roll_cost
        self.pick_cost = pick_cost
        self.item_list = item_list

    @classmethod
    def from_string(self, line) -> 'GCShop':
        split_params = line.split('\t')[1:-1]
        attributes = ['shop_id', 'group_id', 'group_prob', 'roll_cost', 'pick_cost', 'item_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('shop_id'), data.get('group_id'), data.get('group_prob'), data.get('roll_cost'), data.get('pick_cost'), data.get('item_list'))
    
    def __str__(self):
        return f"GCShop(shop_id={self.shop_id}, group_id={self.group_id}, group_prob={self.group_prob}, roll_cost={self.roll_cost}, pick_cost={self.pick_cost}, item_list={self.item_list})"



class GeneralEffectName(object):

    def __init__(self, name_key, effect_name):
        self.name_key = name_key
        self.effect_name = effect_name

    @classmethod
    def from_string(self, line) -> 'GeneralEffectName':
        split_params = line.split('\t')[1:-1]
        attributes = ['name_key', 'effect_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name_key'), data.get('effect_name'))
    
    def __str__(self):
        return f"GeneralEffectName(name_key={self.name_key}, effect_name={self.effect_name})"



class GoodsIcon(object):

    def __init__(self, id, icon):
        self.id = id
        self.icon = icon

    @classmethod
    def from_string(self, line) -> 'GoodsIcon':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'icon']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('icon'))
    
    def __str__(self):
        return f"GoodsIcon(id={self.id}, icon={self.icon})"



class Hairaccessorylocgrp(AbstractItemInfo):

    def __init__(self, mesh_name, X0, Y0, Z0, Pitch0, Yaw0, Roll0, X1, Y1, Z1, Pitch1, Yaw1, Roll1, X2, Y2, Z2, Pitch2, Yaw2, Roll2, X3, Y3, Z3, Pitch3, Yaw3, Roll3, X4, Y4, Z4, Pitch4, Yaw4, Roll4, X5, Y5, Z5, Pitch5, Yaw5, Roll5, X6, Y6, Z6, Pitch6, Yaw6, Roll6, X7, Y7, Z7, Pitch7, Yaw7, Roll7, X8, Y8, Z8, Pitch8, Yaw8, Roll8, X9, Y9, Z9, Pitch9, Yaw9, Roll9, X10, Y10, Z10, Pitch10, Yaw10, Roll10, X11, Y11, Z11, Pitch11, Yaw11, Roll11, X12, Y12, Z12, Pitch12, Yaw12, Roll12, X13, Y13, Z13, Pitch13, Yaw13, Roll13, X14, Y14, Z14, Pitch14, Yaw14, Roll14):
        super().__init__(object_id)
        self.mesh_name = mesh_name
        self.X0 = X0
        self.Y0 = Y0
        self.Z0 = Z0
        self.Pitch0 = Pitch0
        self.Yaw0 = Yaw0
        self.Roll0 = Roll0
        self.X1 = X1
        self.Y1 = Y1
        self.Z1 = Z1
        self.Pitch1 = Pitch1
        self.Yaw1 = Yaw1
        self.Roll1 = Roll1
        self.X2 = X2
        self.Y2 = Y2
        self.Z2 = Z2
        self.Pitch2 = Pitch2
        self.Yaw2 = Yaw2
        self.Roll2 = Roll2
        self.X3 = X3
        self.Y3 = Y3
        self.Z3 = Z3
        self.Pitch3 = Pitch3
        self.Yaw3 = Yaw3
        self.Roll3 = Roll3
        self.X4 = X4
        self.Y4 = Y4
        self.Z4 = Z4
        self.Pitch4 = Pitch4
        self.Yaw4 = Yaw4
        self.Roll4 = Roll4
        self.X5 = X5
        self.Y5 = Y5
        self.Z5 = Z5
        self.Pitch5 = Pitch5
        self.Yaw5 = Yaw5
        self.Roll5 = Roll5
        self.X6 = X6
        self.Y6 = Y6
        self.Z6 = Z6
        self.Pitch6 = Pitch6
        self.Yaw6 = Yaw6
        self.Roll6 = Roll6
        self.X7 = X7
        self.Y7 = Y7
        self.Z7 = Z7
        self.Pitch7 = Pitch7
        self.Yaw7 = Yaw7
        self.Roll7 = Roll7
        self.X8 = X8
        self.Y8 = Y8
        self.Z8 = Z8
        self.Pitch8 = Pitch8
        self.Yaw8 = Yaw8
        self.Roll8 = Roll8
        self.X9 = X9
        self.Y9 = Y9
        self.Z9 = Z9
        self.Pitch9 = Pitch9
        self.Yaw9 = Yaw9
        self.Roll9 = Roll9
        self.X10 = X10
        self.Y10 = Y10
        self.Z10 = Z10
        self.Pitch10 = Pitch10
        self.Yaw10 = Yaw10
        self.Roll10 = Roll10
        self.X11 = X11
        self.Y11 = Y11
        self.Z11 = Z11
        self.Pitch11 = Pitch11
        self.Yaw11 = Yaw11
        self.Roll11 = Roll11
        self.X12 = X12
        self.Y12 = Y12
        self.Z12 = Z12
        self.Pitch12 = Pitch12
        self.Yaw12 = Yaw12
        self.Roll12 = Roll12
        self.X13 = X13
        self.Y13 = Y13
        self.Z13 = Z13
        self.Pitch13 = Pitch13
        self.Yaw13 = Yaw13
        self.Roll13 = Roll13
        self.X14 = X14
        self.Y14 = Y14
        self.Z14 = Z14
        self.Pitch14 = Pitch14
        self.Yaw14 = Yaw14
        self.Roll14 = Roll14

    @classmethod
    def from_string(cls, line) -> 'Hairaccessorylocgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['mesh_name', 'X0', 'Y0', 'Z0', 'Pitch0', 'Yaw0', 'Roll0', 'X1', 'Y1', 'Z1', 'Pitch1', 'Yaw1', 'Roll1', 'X2', 'Y2', 'Z2', 'Pitch2', 'Yaw2', 'Roll2', 'X3', 'Y3', 'Z3', 'Pitch3', 'Yaw3', 'Roll3', 'X4', 'Y4', 'Z4', 'Pitch4', 'Yaw4', 'Roll4', 'X5', 'Y5', 'Z5', 'Pitch5', 'Yaw5', 'Roll5', 'X6', 'Y6', 'Z6', 'Pitch6', 'Yaw6', 'Roll6', 'X7', 'Y7', 'Z7', 'Pitch7', 'Yaw7', 'Roll7', 'X8', 'Y8', 'Z8', 'Pitch8', 'Yaw8', 'Roll8', 'X9', 'Y9', 'Z9', 'Pitch9', 'Yaw9', 'Roll9', 'X10', 'Y10', 'Z10', 'Pitch10', 'Yaw10', 'Roll10', 'X11', 'Y11', 'Z11', 'Pitch11', 'Yaw11', 'Roll11', 'X12', 'Y12', 'Z12', 'Pitch12', 'Yaw12', 'Roll12', 'X13', 'Y13', 'Z13', 'Pitch13', 'Yaw13', 'Roll13', 'X14', 'Y14', 'Z14', 'Pitch14', 'Yaw14', 'Roll14']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('mesh_name'), data.get('X0'), data.get('Y0'), data.get('Z0'), data.get('Pitch0'), data.get('Yaw0'), data.get('Roll0'), data.get('X1'), data.get('Y1'), data.get('Z1'), data.get('Pitch1'), data.get('Yaw1'), data.get('Roll1'), data.get('X2'), data.get('Y2'), data.get('Z2'), data.get('Pitch2'), data.get('Yaw2'), data.get('Roll2'), data.get('X3'), data.get('Y3'), data.get('Z3'), data.get('Pitch3'), data.get('Yaw3'), data.get('Roll3'), data.get('X4'), data.get('Y4'), data.get('Z4'), data.get('Pitch4'), data.get('Yaw4'), data.get('Roll4'), data.get('X5'), data.get('Y5'), data.get('Z5'), data.get('Pitch5'), data.get('Yaw5'), data.get('Roll5'), data.get('X6'), data.get('Y6'), data.get('Z6'), data.get('Pitch6'), data.get('Yaw6'), data.get('Roll6'), data.get('X7'), data.get('Y7'), data.get('Z7'), data.get('Pitch7'), data.get('Yaw7'), data.get('Roll7'), data.get('X8'), data.get('Y8'), data.get('Z8'), data.get('Pitch8'), data.get('Yaw8'), data.get('Roll8'), data.get('X9'), data.get('Y9'), data.get('Z9'), data.get('Pitch9'), data.get('Yaw9'), data.get('Roll9'), data.get('X10'), data.get('Y10'), data.get('Z10'), data.get('Pitch10'), data.get('Yaw10'), data.get('Roll10'), data.get('X11'), data.get('Y11'), data.get('Z11'), data.get('Pitch11'), data.get('Yaw11'), data.get('Roll11'), data.get('X12'), data.get('Y12'), data.get('Z12'), data.get('Pitch12'), data.get('Yaw12'), data.get('Roll12'), data.get('X13'), data.get('Y13'), data.get('Z13'), data.get('Pitch13'), data.get('Yaw13'), data.get('Roll13'), data.get('X14'), data.get('Y14'), data.get('Z14'), data.get('Pitch14'), data.get('Yaw14'), data.get('Roll14'))
    
    def __str__(self):
        return f"Hairaccessorylocgrp(mesh_name={self.mesh_name}, X0={self.X0}, Y0={self.Y0}, Z0={self.Z0}, Pitch0={self.Pitch0}, Yaw0={self.Yaw0}, Roll0={self.Roll0}, X1={self.X1}, Y1={self.Y1}, Z1={self.Z1}, Pitch1={self.Pitch1}, Yaw1={self.Yaw1}, Roll1={self.Roll1}, X2={self.X2}, Y2={self.Y2}, Z2={self.Z2}, Pitch2={self.Pitch2}, Yaw2={self.Yaw2}, Roll2={self.Roll2}, X3={self.X3}, Y3={self.Y3}, Z3={self.Z3}, Pitch3={self.Pitch3}, Yaw3={self.Yaw3}, Roll3={self.Roll3}, X4={self.X4}, Y4={self.Y4}, Z4={self.Z4}, Pitch4={self.Pitch4}, Yaw4={self.Yaw4}, Roll4={self.Roll4}, X5={self.X5}, Y5={self.Y5}, Z5={self.Z5}, Pitch5={self.Pitch5}, Yaw5={self.Yaw5}, Roll5={self.Roll5}, X6={self.X6}, Y6={self.Y6}, Z6={self.Z6}, Pitch6={self.Pitch6}, Yaw6={self.Yaw6}, Roll6={self.Roll6}, X7={self.X7}, Y7={self.Y7}, Z7={self.Z7}, Pitch7={self.Pitch7}, Yaw7={self.Yaw7}, Roll7={self.Roll7}, X8={self.X8}, Y8={self.Y8}, Z8={self.Z8}, Pitch8={self.Pitch8}, Yaw8={self.Yaw8}, Roll8={self.Roll8}, X9={self.X9}, Y9={self.Y9}, Z9={self.Z9}, Pitch9={self.Pitch9}, Yaw9={self.Yaw9}, Roll9={self.Roll9}, X10={self.X10}, Y10={self.Y10}, Z10={self.Z10}, Pitch10={self.Pitch10}, Yaw10={self.Yaw10}, Roll10={self.Roll10}, X11={self.X11}, Y11={self.Y11}, Z11={self.Z11}, Pitch11={self.Pitch11}, Yaw11={self.Yaw11}, Roll11={self.Roll11}, X12={self.X12}, Y12={self.Y12}, Z12={self.Z12}, Pitch12={self.Pitch12}, Yaw12={self.Yaw12}, Roll12={self.Roll12}, X13={self.X13}, Y13={self.Y13}, Z13={self.Z13}, Pitch13={self.Pitch13}, Yaw13={self.Yaw13}, Roll13={self.Roll13}, X14={self.X14}, Y14={self.Y14}, Z14={self.Z14}, Pitch14={self.Pitch14}, Yaw14={self.Yaw14}, Roll14={self.Roll14})"



class Hairexgrp(AbstractItemInfo):

    def __init__(self, error):
        super().__init__(object_id)
        self.error = error

    @classmethod
    def from_string(cls, line) -> 'Hairexgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['error']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('error'))
    
    def __str__(self):
        return f"Hairexgrp(error={self.error})"



class HairExName(object):

    def __init__(self, id, class_name, hair_name, Description):
        self.id = id
        self.class_name = class_name
        self.hair_name = hair_name
        self.Description = Description

    @classmethod
    def from_string(self, line) -> 'HairExName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'class_name', 'hair_name', 'Description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('class_name'), data.get('hair_name'), data.get('Description'))
    
    def __str__(self):
        return f"HairExName(id={self.id}, class_name={self.class_name}, hair_name={self.hair_name}, Description={self.Description})"



class Hennagrp(AbstractItemInfo):

    def __init__(self, symbol_id, dye_item_id, symbol_name, symbol_icon, symbol_epic_icon, symbol_add_name, symbol_description, need_count, cancel_count, level, draw_items, remove_items):
        super().__init__(object_id)
        self.symbol_id = symbol_id
        self.dye_item_id = dye_item_id
        self.symbol_name = symbol_name
        self.symbol_icon = symbol_icon
        self.symbol_epic_icon = symbol_epic_icon
        self.symbol_add_name = symbol_add_name
        self.symbol_description = symbol_description
        self.need_count = need_count
        self.cancel_count = cancel_count
        self.level = level
        self.draw_items = draw_items
        self.remove_items = remove_items

    @classmethod
    def from_string(cls, line) -> 'Hennagrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['symbol_id', 'dye_item_id', 'symbol_name', 'symbol_icon', 'symbol_epic_icon', 'symbol_add_name', 'symbol_description', 'need_count', 'cancel_count', 'level', 'draw_items', 'remove_items']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('symbol_id'), data.get('dye_item_id'), data.get('symbol_name'), data.get('symbol_icon'), data.get('symbol_epic_icon'), data.get('symbol_add_name'), data.get('symbol_description'), data.get('need_count'), data.get('cancel_count'), data.get('level'), data.get('draw_items'), data.get('remove_items'))
    
    def __str__(self):
        return f"Hennagrp(symbol_id={self.symbol_id}, dye_item_id={self.dye_item_id}, symbol_name={self.symbol_name}, symbol_icon={self.symbol_icon}, symbol_epic_icon={self.symbol_epic_icon}, symbol_add_name={self.symbol_add_name}, symbol_description={self.symbol_description}, need_count={self.need_count}, cancel_count={self.cancel_count}, level={self.level}, draw_items={self.draw_items}, remove_items={self.remove_items})"



class Hennagrp(AbstractItemInfo):

    def __init__(self, symbol_id, dye_item_id, symbol_name, symbol_icon, symbol_epic_icon, symbol_add_name, symbol_description, need_count, cancel_count, level, draw_items, remove_items):
        super().__init__(object_id)
        self.symbol_id = symbol_id
        self.dye_item_id = dye_item_id
        self.symbol_name = symbol_name
        self.symbol_icon = symbol_icon
        self.symbol_epic_icon = symbol_epic_icon
        self.symbol_add_name = symbol_add_name
        self.symbol_description = symbol_description
        self.need_count = need_count
        self.cancel_count = cancel_count
        self.level = level
        self.draw_items = draw_items
        self.remove_items = remove_items

    @classmethod
    def from_string(cls, line) -> 'Hennagrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['symbol_id', 'dye_item_id', 'symbol_name', 'symbol_icon', 'symbol_epic_icon', 'symbol_add_name', 'symbol_description', 'need_count', 'cancel_count', 'level', 'draw_items', 'remove_items']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('symbol_id'), data.get('dye_item_id'), data.get('symbol_name'), data.get('symbol_icon'), data.get('symbol_epic_icon'), data.get('symbol_add_name'), data.get('symbol_description'), data.get('need_count'), data.get('cancel_count'), data.get('level'), data.get('draw_items'), data.get('remove_items'))
    
    def __str__(self):
        return f"Hennagrp(symbol_id={self.symbol_id}, dye_item_id={self.dye_item_id}, symbol_name={self.symbol_name}, symbol_icon={self.symbol_icon}, symbol_epic_icon={self.symbol_epic_icon}, symbol_add_name={self.symbol_add_name}, symbol_description={self.symbol_description}, need_count={self.need_count}, cancel_count={self.cancel_count}, level={self.level}, draw_items={self.draw_items}, remove_items={self.remove_items})"



class Hero(object):

    def __init__(self, id, book_skill, success_item, success_skill, commission):
        self.id = id
        self.book_skill = book_skill
        self.success_item = success_item
        self.success_skill = success_skill
        self.commission = commission

    @classmethod
    def from_string(self, line) -> 'Hero':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'book_skill', 'success_item', 'success_skill', 'commission']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('book_skill'), data.get('success_item'), data.get('success_skill'), data.get('commission'))
    
    def __str__(self):
        return f"Hero(id={self.id}, book_skill={self.book_skill}, success_item={self.success_item}, success_skill={self.success_skill}, commission={self.commission})"



class HomunCreate(object):

    def __init__(self, cost_base, hp_count, hp_volume, sp_count, sp_volume, vp_count, vp_volume, cost_time, gain_evolution_point):
        self.cost_base = cost_base
        self.hp_count = hp_count
        self.hp_volume = hp_volume
        self.sp_count = sp_count
        self.sp_volume = sp_volume
        self.vp_count = vp_count
        self.vp_volume = vp_volume
        self.cost_time = cost_time
        self.gain_evolution_point = gain_evolution_point

    @classmethod
    def from_string(self, line) -> 'HomunCreate':
        split_params = line.split('\t')[1:-1]
        attributes = ['cost_base', 'hp_count', 'hp_volume', 'sp_count', 'sp_volume', 'vp_count', 'vp_volume', 'cost_time', 'gain_evolution_point']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('cost_base'), data.get('hp_count'), data.get('hp_volume'), data.get('sp_count'), data.get('sp_volume'), data.get('vp_count'), data.get('vp_volume'), data.get('cost_time'), data.get('gain_evolution_point'))
    
    def __str__(self):
        return f"HomunCreate(cost_base={self.cost_base}, hp_count={self.hp_count}, hp_volume={self.hp_volume}, sp_count={self.sp_count}, sp_volume={self.sp_volume}, vp_count={self.vp_count}, vp_volume={self.vp_volume}, cost_time={self.cost_time}, gain_evolution_point={self.gain_evolution_point})"



class HomunEnchant(object):

    def __init__(self, day_count, mobs_count, extends_count, points_cost, vp_count, vpCost, vp_extend_times, vp_points_cost, unk3, game_points_cost, game_sp_cost, item_id_for_reset_mobs, item_count_for_reset_mobs, item_id_for_reset_vp_count, item_count_for_reset_vp_count):
        self.day_count = day_count
        self.mobs_count = mobs_count
        self.extends_count = extends_count
        self.points_cost = points_cost
        self.vp_count = vp_count
        self.vpCost = vpCost
        self.vp_extend_times = vp_extend_times
        self.vp_points_cost = vp_points_cost
        self.unk3 = unk3
        self.game_points_cost = game_points_cost
        self.game_sp_cost = game_sp_cost
        self.item_id_for_reset_mobs = item_id_for_reset_mobs
        self.item_count_for_reset_mobs = item_count_for_reset_mobs
        self.item_id_for_reset_vp_count = item_id_for_reset_vp_count
        self.item_count_for_reset_vp_count = item_count_for_reset_vp_count

    @classmethod
    def from_string(self, line) -> 'HomunEnchant':
        split_params = line.split('\t')[1:-1]
        attributes = ['day_count', 'mobs_count', 'extends_count', 'points_cost', 'vp_count', 'vpCost', 'vp_extend_times', 'vp_points_cost', 'unk3', 'game_points_cost', 'game_sp_cost', 'item_id_for_reset_mobs', 'item_count_for_reset_mobs', 'item_id_for_reset_vp_count', 'item_count_for_reset_vp_count']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('day_count'), data.get('mobs_count'), data.get('extends_count'), data.get('points_cost'), data.get('vp_count'), data.get('vpCost'), data.get('vp_extend_times'), data.get('vp_points_cost'), data.get('unk3'), data.get('game_points_cost'), data.get('game_sp_cost'), data.get('item_id_for_reset_mobs'), data.get('item_count_for_reset_mobs'), data.get('item_id_for_reset_vp_count'), data.get('item_count_for_reset_vp_count'))
    
    def __str__(self):
        return f"HomunEnchant(day_count={self.day_count}, mobs_count={self.mobs_count}, extends_count={self.extends_count}, points_cost={self.points_cost}, vp_count={self.vp_count}, vpCost={self.vpCost}, vp_extend_times={self.vp_extend_times}, vp_points_cost={self.vp_points_cost}, unk3={self.unk3}, game_points_cost={self.game_points_cost}, game_sp_cost={self.game_sp_cost}, item_id_for_reset_mobs={self.item_id_for_reset_mobs}, item_count_for_reset_mobs={self.item_count_for_reset_mobs}, item_id_for_reset_vp_count={self.item_id_for_reset_vp_count}, item_count_for_reset_vp_count={self.item_count_for_reset_vp_count})"



class HomunList(object):

    def __init__(self, itemid, amount, fee, grade, event, unk):
        self.itemid = itemid
        self.amount = amount
        self.fee = fee
        self.grade = grade
        self.event = event
        self.unk = unk

    @classmethod
    def from_string(self, line) -> 'HomunList':
        split_params = line.split('\t')[1:-1]
        attributes = ['itemid', 'amount', 'fee', 'grade', 'event', 'unk']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('itemid'), data.get('amount'), data.get('fee'), data.get('grade'), data.get('event'), data.get('unk'))
    
    def __str__(self):
        return f"HomunList(itemid={self.itemid}, amount={self.amount}, fee={self.fee}, grade={self.grade}, event={self.event}, unk={self.unk})"



class HomunNpc(object):

    def __init__(self, index, type, npc_id, base_skill, img_name, evolution_cost_point, evolution_cost_item):
        self.index = index
        self.type = type
        self.npc_id = npc_id
        self.base_skill = base_skill
        self.img_name = img_name
        self.evolution_cost_point = evolution_cost_point
        self.evolution_cost_item = evolution_cost_item

    @classmethod
    def from_string(self, line) -> 'HomunNpc':
        split_params = line.split('\t')[1:-1]
        attributes = ['index', 'type', 'npc_id', 'base_skill', 'img_name', 'evolution_cost_point', 'evolution_cost_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('index'), data.get('type'), data.get('npc_id'), data.get('base_skill'), data.get('img_name'), data.get('evolution_cost_point'), data.get('evolution_cost_item'))
    
    def __str__(self):
        return f"HomunNpc(index={self.index}, type={self.type}, npc_id={self.npc_id}, base_skill={self.base_skill}, img_name={self.img_name}, evolution_cost_point={self.evolution_cost_point}, evolution_cost_item={self.evolution_cost_item})"



class HomunNpcLevel(object):

    def __init__(self, id, level, exp_to_level, exp_per_point_grade1, exp_per_point_grade2, exp_per_point_grade3, unk, skill_id_win1, skill_level_win1, skill_id_win2, skill_level_win2, skill_id_win3, skill_level_win3):
        self.id = id
        self.level = level
        self.exp_to_level = exp_to_level
        self.exp_per_point_grade1 = exp_per_point_grade1
        self.exp_per_point_grade2 = exp_per_point_grade2
        self.exp_per_point_grade3 = exp_per_point_grade3
        self.unk = unk
        self.skill_id_win1 = skill_id_win1
        self.skill_level_win1 = skill_level_win1
        self.skill_id_win2 = skill_id_win2
        self.skill_level_win2 = skill_level_win2
        self.skill_id_win3 = skill_id_win3
        self.skill_level_win3 = skill_level_win3

    @classmethod
    def from_string(self, line) -> 'HomunNpcLevel':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'level', 'exp_to_level', 'exp_per_point_grade1', 'exp_per_point_grade2', 'exp_per_point_grade3', 'unk', 'skill_id_win1', 'skill_level_win1', 'skill_id_win2', 'skill_level_win2', 'skill_id_win3', 'skill_level_win3']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('level'), data.get('exp_to_level'), data.get('exp_per_point_grade1'), data.get('exp_per_point_grade2'), data.get('exp_per_point_grade3'), data.get('unk'), data.get('skill_id_win1'), data.get('skill_level_win1'), data.get('skill_id_win2'), data.get('skill_level_win2'), data.get('skill_id_win3'), data.get('skill_level_win3'))
    
    def __str__(self):
        return f"HomunNpcLevel(id={self.id}, level={self.level}, exp_to_level={self.exp_to_level}, exp_per_point_grade1={self.exp_per_point_grade1}, exp_per_point_grade2={self.exp_per_point_grade2}, exp_per_point_grade3={self.exp_per_point_grade3}, unk={self.unk}, skill_id_win1={self.skill_id_win1}, skill_level_win1={self.skill_level_win1}, skill_id_win2={self.skill_id_win2}, skill_level_win2={self.skill_level_win2}, skill_id_win3={self.skill_id_win3}, skill_level_win3={self.skill_level_win3})"



class HomunSlot(object):

    def __init__(self, slotid, costitems):
        self.slotid = slotid
        self.costitems = costitems

    @classmethod
    def from_string(self, line) -> 'HomunSlot':
        split_params = line.split('\t')[1:-1]
        attributes = ['slotid', 'costitems']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('slotid'), data.get('costitems'))
    
    def __str__(self):
        return f"HomunSlot(slotid={self.slotid}, costitems={self.costitems})"



class HuntingZone(object):

    def __init__(self, id, type, rc_level, loc, desc, search_zoneid, name, regionid, npc_id, quest_id, instantzone_id):
        self.id = id
        self.type = type
        self.rc_level = rc_level
        self.loc = loc
        self.desc = desc
        self.search_zoneid = search_zoneid
        self.name = name
        self.regionid = regionid
        self.npc_id = npc_id
        self.quest_id = quest_id
        self.instantzone_id = instantzone_id

    @classmethod
    def from_string(self, line) -> 'HuntingZone':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'rc_level', 'loc', 'desc', 'search_zoneid', 'name', 'regionid', 'npc_id', 'quest_id', 'instantzone_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('rc_level'), data.get('loc'), data.get('desc'), data.get('search_zoneid'), data.get('name'), data.get('regionid'), data.get('npc_id'), data.get('quest_id'), data.get('instantzone_id'))
    
    def __str__(self):
        return f"HuntingZone(id={self.id}, type={self.type}, rc_level={self.rc_level}, loc={self.loc}, desc={self.desc}, search_zoneid={self.search_zoneid}, name={self.name}, regionid={self.regionid}, npc_id={self.npc_id}, quest_id={self.quest_id}, instantzone_id={self.instantzone_id})"



class HuntingZone(object):

    def __init__(self, id, type, rc_level, loc, desc, search_zoneid, name, regionid, npc_id, quest_id, instantzone_id):
        self.id = id
        self.type = type
        self.rc_level = rc_level
        self.loc = loc
        self.desc = desc
        self.search_zoneid = search_zoneid
        self.name = name
        self.regionid = regionid
        self.npc_id = npc_id
        self.quest_id = quest_id
        self.instantzone_id = instantzone_id

    @classmethod
    def from_string(self, line) -> 'HuntingZone':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'rc_level', 'loc', 'desc', 'search_zoneid', 'name', 'regionid', 'npc_id', 'quest_id', 'instantzone_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('rc_level'), data.get('loc'), data.get('desc'), data.get('search_zoneid'), data.get('name'), data.get('regionid'), data.get('npc_id'), data.get('quest_id'), data.get('instantzone_id'))
    
    def __str__(self):
        return f"HuntingZone(id={self.id}, type={self.type}, rc_level={self.rc_level}, loc={self.loc}, desc={self.desc}, search_zoneid={self.search_zoneid}, name={self.name}, regionid={self.regionid}, npc_id={self.npc_id}, quest_id={self.quest_id}, instantzone_id={self.instantzone_id})"



class InstantZoneData(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_string(self, line) -> 'InstantZoneData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'))
    
    def __str__(self):
        return f"InstantZoneData(id={self.id}, name={self.name})"



class InstantZoneData(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_string(self, line) -> 'InstantZoneData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'))
    
    def __str__(self):
        return f"InstantZoneData(id={self.id}, name={self.name})"



class InventoryEffect(object):

    def __init__(self, item_id, min_enchant, max_enchant, effect):
        self.item_id = item_id
        self.min_enchant = min_enchant
        self.max_enchant = max_enchant
        self.effect = effect

    @classmethod
    def from_string(self, line) -> 'InventoryEffect':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'min_enchant', 'max_enchant', 'effect']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('min_enchant'), data.get('max_enchant'), data.get('effect'))
    
    def __str__(self):
        return f"InventoryEffect(item_id={self.item_id}, min_enchant={self.min_enchant}, max_enchant={self.max_enchant}, effect={self.effect})"



class ItemMultisell(object):

    def __init__(self, itemClassID, multisell_id_list, multisell_name, unk):
        self.itemClassID = itemClassID
        self.multisell_id_list = multisell_id_list
        self.multisell_name = multisell_name
        self.unk = unk

    @classmethod
    def from_string(self, line) -> 'ItemMultisell':
        split_params = line.split('\t')[1:-1]
        attributes = ['itemClassID', 'multisell_id_list', 'multisell_name', 'unk']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('itemClassID'), data.get('multisell_id_list'), data.get('multisell_name'), data.get('unk'))
    
    def __str__(self):
        return f"ItemMultisell(itemClassID={self.itemClassID}, multisell_id_list={self.multisell_id_list}, multisell_name={self.multisell_name}, unk={self.unk})"



class ItemMultisell(object):

    def __init__(self, itemClassID, multisell_id_list, multisell_name, unk):
        self.itemClassID = itemClassID
        self.multisell_id_list = multisell_id_list
        self.multisell_name = multisell_name
        self.unk = unk

    @classmethod
    def from_string(self, line) -> 'ItemMultisell':
        split_params = line.split('\t')[1:-1]
        attributes = ['itemClassID', 'multisell_id_list', 'multisell_name', 'unk']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('itemClassID'), data.get('multisell_id_list'), data.get('multisell_name'), data.get('unk'))
    
    def __str__(self):
        return f"ItemMultisell(itemClassID={self.itemClassID}, multisell_id_list={self.multisell_id_list}, multisell_name={self.multisell_name}, unk={self.unk})"



class ItemName(object):

    def __init__(self, id, name, additionalname, description, popup, default_action, use_order, name_class, color, Tooltip_Texture, Tooltip_BG_Texture, Tooltip_BG_Texture_Compare, Tooltip_BG_Deco_Texture, is_trade, is_drop, is_destruct, is_private_store, keep_type, is_npctrade, is_commission_store, enchant_bless, show_create_items, sort_order, auction_category, autouse_type, keep_type_selection, keep_type_enchant):
        self.id = id
        self.name = name
        self.additionalname = additionalname
        self.description = description
        self.popup = popup
        self.default_action = default_action
        self.use_order = use_order
        self.name_class = name_class
        self.color = color
        self.Tooltip_Texture = Tooltip_Texture
        self.Tooltip_BG_Texture = Tooltip_BG_Texture
        self.Tooltip_BG_Texture_Compare = Tooltip_BG_Texture_Compare
        self.Tooltip_BG_Deco_Texture = Tooltip_BG_Deco_Texture
        self.is_trade = is_trade
        self.is_drop = is_drop
        self.is_destruct = is_destruct
        self.is_private_store = is_private_store
        self.keep_type = keep_type
        self.is_npctrade = is_npctrade
        self.is_commission_store = is_commission_store
        self.enchant_bless = enchant_bless
        self.show_create_items = show_create_items
        self.sort_order = sort_order
        self.auction_category = auction_category
        self.autouse_type = autouse_type
        self.keep_type_selection = keep_type_selection
        self.keep_type_enchant = keep_type_enchant

    @classmethod
    def from_string(self, line) -> 'ItemName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'additionalname', 'description', 'popup', 'default_action', 'use_order', 'name_class', 'color', 'Tooltip_Texture', 'Tooltip_BG_Texture', 'Tooltip_BG_Texture_Compare', 'Tooltip_BG_Deco_Texture', 'is_trade', 'is_drop', 'is_destruct', 'is_private_store', 'keep_type', 'is_npctrade', 'is_commission_store', 'enchant_bless', 'show_create_items', 'sort_order', 'auction_category', 'autouse_type', 'keep_type_selection', 'keep_type_enchant']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('additionalname'), data.get('description'), data.get('popup'), data.get('default_action'), data.get('use_order'), data.get('name_class'), data.get('color'), data.get('Tooltip_Texture'), data.get('Tooltip_BG_Texture'), data.get('Tooltip_BG_Texture_Compare'), data.get('Tooltip_BG_Deco_Texture'), data.get('is_trade'), data.get('is_drop'), data.get('is_destruct'), data.get('is_private_store'), data.get('keep_type'), data.get('is_npctrade'), data.get('is_commission_store'), data.get('enchant_bless'), data.get('show_create_items'), data.get('sort_order'), data.get('auction_category'), data.get('autouse_type'), data.get('keep_type_selection'), data.get('keep_type_enchant'))
    
    def __str__(self):
        return f"ItemName(id={self.id}, name={self.name}, additionalname={self.additionalname}, description={self.description}, popup={self.popup}, default_action={self.default_action}, use_order={self.use_order}, name_class={self.name_class}, color={self.color}, Tooltip_Texture={self.Tooltip_Texture}, Tooltip_BG_Texture={self.Tooltip_BG_Texture}, Tooltip_BG_Texture_Compare={self.Tooltip_BG_Texture_Compare}, Tooltip_BG_Deco_Texture={self.Tooltip_BG_Deco_Texture}, is_trade={self.is_trade}, is_drop={self.is_drop}, is_destruct={self.is_destruct}, is_private_store={self.is_private_store}, keep_type={self.keep_type}, is_npctrade={self.is_npctrade}, is_commission_store={self.is_commission_store}, enchant_bless={self.enchant_bless}, show_create_items={self.show_create_items}, sort_order={self.sort_order}, auction_category={self.auction_category}, autouse_type={self.autouse_type}, keep_type_selection={self.keep_type_selection}, keep_type_enchant={self.keep_type_enchant})"



class ItemName(object):

    def __init__(self, id, name, additionalname, description, popup, default_action, use_order, name_class, color, Tooltip_Texture, Tooltip_BG_Texture, Tooltip_BG_Texture_Compare, Tooltip_BG_Deco_Texture, is_trade, is_drop, is_destruct, is_private_store, keep_type, is_npctrade, is_commission_store, enchant_bless, show_create_items, sort_order, auction_category, autouse_type, keep_type_selection, keep_type_enchant):
        self.id = id
        self.name = name
        self.additionalname = additionalname
        self.description = description
        self.popup = popup
        self.default_action = default_action
        self.use_order = use_order
        self.name_class = name_class
        self.color = color
        self.Tooltip_Texture = Tooltip_Texture
        self.Tooltip_BG_Texture = Tooltip_BG_Texture
        self.Tooltip_BG_Texture_Compare = Tooltip_BG_Texture_Compare
        self.Tooltip_BG_Deco_Texture = Tooltip_BG_Deco_Texture
        self.is_trade = is_trade
        self.is_drop = is_drop
        self.is_destruct = is_destruct
        self.is_private_store = is_private_store
        self.keep_type = keep_type
        self.is_npctrade = is_npctrade
        self.is_commission_store = is_commission_store
        self.enchant_bless = enchant_bless
        self.show_create_items = show_create_items
        self.sort_order = sort_order
        self.auction_category = auction_category
        self.autouse_type = autouse_type
        self.keep_type_selection = keep_type_selection
        self.keep_type_enchant = keep_type_enchant

    @classmethod
    def from_string(self, line) -> 'ItemName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'additionalname', 'description', 'popup', 'default_action', 'use_order', 'name_class', 'color', 'Tooltip_Texture', 'Tooltip_BG_Texture', 'Tooltip_BG_Texture_Compare', 'Tooltip_BG_Deco_Texture', 'is_trade', 'is_drop', 'is_destruct', 'is_private_store', 'keep_type', 'is_npctrade', 'is_commission_store', 'enchant_bless', 'show_create_items', 'sort_order', 'auction_category', 'autouse_type', 'keep_type_selection', 'keep_type_enchant']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('additionalname'), data.get('description'), data.get('popup'), data.get('default_action'), data.get('use_order'), data.get('name_class'), data.get('color'), data.get('Tooltip_Texture'), data.get('Tooltip_BG_Texture'), data.get('Tooltip_BG_Texture_Compare'), data.get('Tooltip_BG_Deco_Texture'), data.get('is_trade'), data.get('is_drop'), data.get('is_destruct'), data.get('is_private_store'), data.get('keep_type'), data.get('is_npctrade'), data.get('is_commission_store'), data.get('enchant_bless'), data.get('show_create_items'), data.get('sort_order'), data.get('auction_category'), data.get('autouse_type'), data.get('keep_type_selection'), data.get('keep_type_enchant'))
    
    def __str__(self):
        return f"ItemName(id={self.id}, name={self.name}, additionalname={self.additionalname}, description={self.description}, popup={self.popup}, default_action={self.default_action}, use_order={self.use_order}, name_class={self.name_class}, color={self.color}, Tooltip_Texture={self.Tooltip_Texture}, Tooltip_BG_Texture={self.Tooltip_BG_Texture}, Tooltip_BG_Texture_Compare={self.Tooltip_BG_Texture_Compare}, Tooltip_BG_Deco_Texture={self.Tooltip_BG_Deco_Texture}, is_trade={self.is_trade}, is_drop={self.is_drop}, is_destruct={self.is_destruct}, is_private_store={self.is_private_store}, keep_type={self.keep_type}, is_npctrade={self.is_npctrade}, is_commission_store={self.is_commission_store}, enchant_bless={self.enchant_bless}, show_create_items={self.show_create_items}, sort_order={self.sort_order}, auction_category={self.auction_category}, autouse_type={self.autouse_type}, keep_type_selection={self.keep_type_selection}, keep_type_enchant={self.keep_type_enchant})"



class ItemScore(object):

    def __init__(self, id, grade, unk3, unk4):
        self.id = id
        self.grade = grade
        self.unk3 = unk3
        self.unk4 = unk4

    @classmethod
    def from_string(self, line) -> 'ItemScore':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'grade', 'unk3', 'unk4']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('grade'), data.get('unk3'), data.get('unk4'))
    
    def __str__(self):
        return f"ItemScore(id={self.id}, grade={self.grade}, unk3={self.unk3}, unk4={self.unk4})"



class ItemStatData(object):

    def __init__(self, object_id, pDefense, mDefense, pAttack, mAttack, pAttackSpeed, pHit, mHit, pCritical, mCritical, speed, ShieldDefense, ShieldDefenseRate, pavoid, mavoid):
        self.object_id = object_id
        self.pDefense = pDefense
        self.mDefense = mDefense
        self.pAttack = pAttack
        self.mAttack = mAttack
        self.pAttackSpeed = pAttackSpeed
        self.pHit = pHit
        self.mHit = mHit
        self.pCritical = pCritical
        self.mCritical = mCritical
        self.speed = speed
        self.ShieldDefense = ShieldDefense
        self.ShieldDefenseRate = ShieldDefenseRate
        self.pavoid = pavoid
        self.mavoid = mavoid

    @classmethod
    def from_string(self, line) -> 'ItemStatData':
        split_params = line.split('\t')[1:-1]
        attributes = ['object_id', 'pDefense', 'mDefense', 'pAttack', 'mAttack', 'pAttackSpeed', 'pHit', 'mHit', 'pCritical', 'mCritical', 'speed', 'ShieldDefense', 'ShieldDefenseRate', 'pavoid', 'mavoid']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('object_id'), data.get('pDefense'), data.get('mDefense'), data.get('pAttack'), data.get('mAttack'), data.get('pAttackSpeed'), data.get('pHit'), data.get('mHit'), data.get('pCritical'), data.get('mCritical'), data.get('speed'), data.get('ShieldDefense'), data.get('ShieldDefenseRate'), data.get('pavoid'), data.get('mavoid'))
    
    def __str__(self):
        return f"ItemStatData(object_id={self.object_id}, pDefense={self.pDefense}, mDefense={self.mDefense}, pAttack={self.pAttack}, mAttack={self.mAttack}, pAttackSpeed={self.pAttackSpeed}, pHit={self.pHit}, mHit={self.mHit}, pCritical={self.pCritical}, mCritical={self.mCritical}, speed={self.speed}, ShieldDefense={self.ShieldDefense}, ShieldDefenseRate={self.ShieldDefenseRate}, pavoid={self.pavoid}, mavoid={self.mavoid})"



class ItemUseFilter(object):

    def __init__(self, id, enchanted_item, blessed_item, ensoul_item, variation_item, lookchange_item, attribute_item, locked_item, equipped_item):
        self.id = id
        self.enchanted_item = enchanted_item
        self.blessed_item = blessed_item
        self.ensoul_item = ensoul_item
        self.variation_item = variation_item
        self.lookchange_item = lookchange_item
        self.attribute_item = attribute_item
        self.locked_item = locked_item
        self.equipped_item = equipped_item

    @classmethod
    def from_string(self, line) -> 'ItemUseFilter':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'enchanted_item', 'blessed_item', 'ensoul_item', 'variation_item', 'lookchange_item', 'attribute_item', 'locked_item', 'equipped_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('enchanted_item'), data.get('blessed_item'), data.get('ensoul_item'), data.get('variation_item'), data.get('lookchange_item'), data.get('attribute_item'), data.get('locked_item'), data.get('equipped_item'))
    
    def __str__(self):
        return f"ItemUseFilter(id={self.id}, enchanted_item={self.enchanted_item}, blessed_item={self.blessed_item}, ensoul_item={self.ensoul_item}, variation_item={self.variation_item}, lookchange_item={self.lookchange_item}, attribute_item={self.attribute_item}, locked_item={self.locked_item}, equipped_item={self.equipped_item})"



class Item(object):

    def __init__(self, id, default_price, craft_charge_points, craft_charge_cost, is_locked, enchant_enable, enchant_group_id, challenge_point_group_id, hero_book_point):
        self.id = id
        self.default_price = default_price
        self.craft_charge_points = craft_charge_points
        self.craft_charge_cost = craft_charge_cost
        self.is_locked = is_locked
        self.enchant_enable = enchant_enable
        self.enchant_group_id = enchant_group_id
        self.challenge_point_group_id = challenge_point_group_id
        self.hero_book_point = hero_book_point

    @classmethod
    def from_string(self, line) -> 'Item':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'default_price', 'craft_charge_points', 'craft_charge_cost', 'is_locked', 'enchant_enable', 'enchant_group_id', 'challenge_point_group_id', 'hero_book_point']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('default_price'), data.get('craft_charge_points'), data.get('craft_charge_cost'), data.get('is_locked'), data.get('enchant_enable'), data.get('enchant_group_id'), data.get('challenge_point_group_id'), data.get('hero_book_point'))
    
    def __str__(self):
        return f"Item(id={self.id}, default_price={self.default_price}, craft_charge_points={self.craft_charge_points}, craft_charge_cost={self.craft_charge_cost}, is_locked={self.is_locked}, enchant_enable={self.enchant_enable}, enchant_group_id={self.enchant_group_id}, challenge_point_group_id={self.challenge_point_group_id}, hero_book_point={self.hero_book_point})"



class ItemBaseinfo(object):

    def __init__(self, id, default_price, craft_charge_points, craft_charge_cost, is_locked, enchant_enable, enchant_group_id, challenge_point_group_id, hero_book_point):
        self.id = id
        self.default_price = default_price
        self.craft_charge_points = craft_charge_points
        self.craft_charge_cost = craft_charge_cost
        self.is_locked = is_locked
        self.enchant_enable = enchant_enable
        self.enchant_group_id = enchant_group_id
        self.challenge_point_group_id = challenge_point_group_id
        self.hero_book_point = hero_book_point

    @classmethod
    def from_string(self, line) -> 'ItemBaseinfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'default_price', 'craft_charge_points', 'craft_charge_cost', 'is_locked', 'enchant_enable', 'enchant_group_id', 'challenge_point_group_id', 'hero_book_point']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('default_price'), data.get('craft_charge_points'), data.get('craft_charge_cost'), data.get('is_locked'), data.get('enchant_enable'), data.get('enchant_group_id'), data.get('challenge_point_group_id'), data.get('hero_book_point'))
    
    def __str__(self):
        return f"ItemBaseinfo(id={self.id}, default_price={self.default_price}, craft_charge_points={self.craft_charge_points}, craft_charge_cost={self.craft_charge_cost}, is_locked={self.is_locked}, enchant_enable={self.enchant_enable}, enchant_group_id={self.enchant_group_id}, challenge_point_group_id={self.challenge_point_group_id}, hero_book_point={self.hero_book_point})"



class L2GameDataName(object):

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(self, line) -> 'L2GameDataName':
        split_params = line.split('\t')[1:-1]
        attributes = ['name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'))
    
    def __str__(self):
        return f"L2GameDataName(name={self.name})"



class L2PassAdvance(object):

    def __init__(self, advance_type, advance_id, advance_type_name, target_item, target_item_enchant, target_item_desc):
        self.advance_type = advance_type
        self.advance_id = advance_id
        self.advance_type_name = advance_type_name
        self.target_item = target_item
        self.target_item_enchant = target_item_enchant
        self.target_item_desc = target_item_desc

    @classmethod
    def from_string(self, line) -> 'L2PassAdvance':
        split_params = line.split('\t')[1:-1]
        attributes = ['advance_type', 'advance_id', 'advance_type_name', 'target_item', 'target_item_enchant', 'target_item_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('advance_type'), data.get('advance_id'), data.get('advance_type_name'), data.get('target_item'), data.get('target_item_enchant'), data.get('target_item_desc'))
    
    def __str__(self):
        return f"L2PassAdvance(advance_type={self.advance_type}, advance_id={self.advance_id}, advance_type_name={self.advance_type_name}, target_item={self.target_item}, target_item_enchant={self.target_item_enchant}, target_item_desc={self.target_item_desc})"



class L2PassAdvance(object):

    def __init__(self, advance_type, advance_id, advance_type_name, target_item, target_item_enchant, target_item_desc):
        self.advance_type = advance_type
        self.advance_id = advance_id
        self.advance_type_name = advance_type_name
        self.target_item = target_item
        self.target_item_enchant = target_item_enchant
        self.target_item_desc = target_item_desc

    @classmethod
    def from_string(self, line) -> 'L2PassAdvance':
        split_params = line.split('\t')[1:-1]
        attributes = ['advance_type', 'advance_id', 'advance_type_name', 'target_item', 'target_item_enchant', 'target_item_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('advance_type'), data.get('advance_id'), data.get('advance_type_name'), data.get('target_item'), data.get('target_item_enchant'), data.get('target_item_desc'))
    
    def __str__(self):
        return f"L2PassAdvance(advance_type={self.advance_type}, advance_id={self.advance_id}, advance_type_name={self.advance_type_name}, target_item={self.target_item}, target_item_enchant={self.target_item_enchant}, target_item_desc={self.target_item_desc})"



class L2PassReward(object):

    def __init__(self, pass_type, pass_id, required_points, advance_premium_cost, hunting_premium_cost, reward, premium_reward, applycountry):
        self.pass_type = pass_type
        self.pass_id = pass_id
        self.required_points = required_points
        self.advance_premium_cost = advance_premium_cost
        self.hunting_premium_cost = hunting_premium_cost
        self.reward = reward
        self.premium_reward = premium_reward
        self.applycountry = applycountry

    @classmethod
    def from_string(self, line) -> 'L2PassReward':
        split_params = line.split('\t')[1:-1]
        attributes = ['pass_type', 'pass_id', 'required_points', 'advance_premium_cost', 'hunting_premium_cost', 'reward', 'premium_reward', 'applycountry']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('pass_type'), data.get('pass_id'), data.get('required_points'), data.get('advance_premium_cost'), data.get('hunting_premium_cost'), data.get('reward'), data.get('premium_reward'), data.get('applycountry'))
    
    def __str__(self):
        return f"L2PassReward(pass_type={self.pass_type}, pass_id={self.pass_id}, required_points={self.required_points}, advance_premium_cost={self.advance_premium_cost}, hunting_premium_cost={self.hunting_premium_cost}, reward={self.reward}, premium_reward={self.premium_reward}, applycountry={self.applycountry})"



class LCoinShopBanner(object):

    def __init__(self, TextureName, LinkURL, unk502):
        self.TextureName = TextureName
        self.LinkURL = LinkURL
        self.unk502 = unk502

    @classmethod
    def from_string(self, line) -> 'LCoinShopBanner':
        split_params = line.split('\t')[1:-1]
        attributes = ['TextureName', 'LinkURL', 'unk502']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('TextureName'), data.get('LinkURL'), data.get('unk502'))
    
    def __str__(self):
        return f"LCoinShopBanner(TextureName={self.TextureName}, LinkURL={self.LinkURL}, unk502={self.unk502})"



class LCoinShopCategory(object):

    def __init__(self, category_id, string_id, string_color, ribbon_texture_lshop, optional, show_server):
        self.category_id = category_id
        self.string_id = string_id
        self.string_color = string_color
        self.ribbon_texture_lshop = ribbon_texture_lshop
        self.optional = optional
        self.show_server = show_server

    @classmethod
    def from_string(self, line) -> 'LCoinShopCategory':
        split_params = line.split('\t')[1:-1]
        attributes = ['category_id', 'string_id', 'string_color', 'ribbon_texture_lshop', 'optional', 'show_server']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('category_id'), data.get('string_id'), data.get('string_color'), data.get('ribbon_texture_lshop'), data.get('optional'), data.get('show_server'))
    
    def __str__(self):
        return f"LCoinShopCategory(category_id={self.category_id}, string_id={self.string_id}, string_color={self.string_color}, ribbon_texture_lshop={self.ribbon_texture_lshop}, optional={self.optional}, show_server={self.show_server})"



class LCoinShopProduct(object):

    def __init__(self, product_id, ServerId, ShopType, category, mark_type, product_item, product_type, buy_limit, product_desc, product_htm):
        self.product_id = product_id
        self.ServerId = ServerId
        self.ShopType = ShopType
        self.category = category
        self.mark_type = mark_type
        self.product_item = product_item
        self.product_type = product_type
        self.buy_limit = buy_limit
        self.product_desc = product_desc
        self.product_htm = product_htm

    @classmethod
    def from_string(self, line) -> 'LCoinShopProduct':
        split_params = line.split('\t')[1:-1]
        attributes = ['product_id', 'ServerId', 'ShopType', 'category', 'mark_type', 'product_item', 'product_type', 'buy_limit', 'product_desc', 'product_htm']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('product_id'), data.get('ServerId'), data.get('ShopType'), data.get('category'), data.get('mark_type'), data.get('product_item'), data.get('product_type'), data.get('buy_limit'), data.get('product_desc'), data.get('product_htm'))
    
    def __str__(self):
        return f"LCoinShopProduct(product_id={self.product_id}, ServerId={self.ServerId}, ShopType={self.ShopType}, category={self.category}, mark_type={self.mark_type}, product_item={self.product_item}, product_type={self.product_type}, buy_limit={self.buy_limit}, product_desc={self.product_desc}, product_htm={self.product_htm})"



class LCoinShopProduct(object):

    def __init__(self, product_id, ServerId, ShopType, category, mark_type, product_item, product_type, buy_limit, product_desc, product_htm):
        self.product_id = product_id
        self.ServerId = ServerId
        self.ShopType = ShopType
        self.category = category
        self.mark_type = mark_type
        self.product_item = product_item
        self.product_type = product_type
        self.buy_limit = buy_limit
        self.product_desc = product_desc
        self.product_htm = product_htm

    @classmethod
    def from_string(self, line) -> 'LCoinShopProduct':
        split_params = line.split('\t')[1:-1]
        attributes = ['product_id', 'ServerId', 'ShopType', 'category', 'mark_type', 'product_item', 'product_type', 'buy_limit', 'product_desc', 'product_htm']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('product_id'), data.get('ServerId'), data.get('ShopType'), data.get('category'), data.get('mark_type'), data.get('product_item'), data.get('product_type'), data.get('buy_limit'), data.get('product_desc'), data.get('product_htm'))
    
    def __str__(self):
        return f"LCoinShopProduct(product_id={self.product_id}, ServerId={self.ServerId}, ShopType={self.ShopType}, category={self.category}, mark_type={self.mark_type}, product_item={self.product_item}, product_type={self.product_type}, buy_limit={self.buy_limit}, product_desc={self.product_desc}, product_htm={self.product_htm})"



class LetterCollectData(object):

    def __init__(self, id, letters):
        self.id = id
        self.letters = letters

    @classmethod
    def from_string(self, line) -> 'LetterCollectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'letters']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('letters'))
    
    def __str__(self):
        return f"LetterCollectData(id={self.id}, letters={self.letters})"



class LevelAmbience(object):

    def __init__(self, id, map_x, map_y, default_state, state):
        self.id = id
        self.map_x = map_x
        self.map_y = map_y
        self.default_state = default_state
        self.state = state

    @classmethod
    def from_string(self, line) -> 'LevelAmbience':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'map_x', 'map_y', 'default_state', 'state']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('map_x'), data.get('map_y'), data.get('default_state'), data.get('state'))
    
    def __str__(self):
        return f"LevelAmbience(id={self.id}, map_x={self.map_x}, map_y={self.map_y}, default_state={self.default_state}, state={self.state})"



class LevelUpItemBonusData(object):

    def __init__(self, object_id):
        self.object_id = object_id

    @classmethod
    def from_string(self, line) -> 'LevelUpItemBonusData':
        split_params = line.split('\t')[1:-1]
        attributes = ['object_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('object_id'))
    
    def __str__(self):
        return f"LevelUpItemBonusData(object_id={self.object_id})"



class LinkedAnimData(object):

    def __init__(self, clazz, attack, social):
        self.clazz = clazz
        self.attack = attack
        self.social = social

    @classmethod
    def from_string(self, line) -> 'LinkedAnimData':
        split_params = line.split('\t')[1:-1]
        attributes = ['clazz', 'attack', 'social']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('clazz'), data.get('attack'), data.get('social'))
    
    def __str__(self):
        return f"LinkedAnimData(clazz={self.clazz}, attack={self.attack}, social={self.social})"



class Localize(object):

    def __init__(self, target, targettype, targetid, skilllv, value, applycountry):
        self.target = target
        self.targettype = targettype
        self.targetid = targetid
        self.skilllv = skilllv
        self.value = value
        self.applycountry = applycountry

    @classmethod
    def from_string(self, line) -> 'Localize':
        split_params = line.split('\t')[1:-1]
        attributes = ['target', 'targettype', 'targetid', 'skilllv', 'value', 'applycountry']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('target'), data.get('targettype'), data.get('targetid'), data.get('skilllv'), data.get('value'), data.get('applycountry'))
    
    def __str__(self):
        return f"Localize(target={self.target}, targettype={self.targettype}, targetid={self.targetid}, skilllv={self.skilllv}, value={self.value}, applycountry={self.applycountry})"



class Logongrp(AbstractItemInfo):

    def __init__(self, x, y, z, yaw):
        super().__init__(object_id)
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw

    @classmethod
    def from_string(cls, line) -> 'Logongrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['x', 'y', 'z', 'yaw']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('x'), data.get('y'), data.get('z'), data.get('yaw'))
    
    def __str__(self):
        return f"Logongrp(x={self.x}, y={self.y}, z={self.z}, yaw={self.yaw})"



class LollyCubeData(object):

    def __init__(self, skill_id, skill_level, reward_item_class_id, reward_item_modify_price, additional_item_class_id, additional_reward_item_class_id, additional_reward_item_num, additional_gain_rate):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.reward_item_class_id = reward_item_class_id
        self.reward_item_modify_price = reward_item_modify_price
        self.additional_item_class_id = additional_item_class_id
        self.additional_reward_item_class_id = additional_reward_item_class_id
        self.additional_reward_item_num = additional_reward_item_num
        self.additional_gain_rate = additional_gain_rate

    @classmethod
    def from_string(self, line) -> 'LollyCubeData':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'reward_item_class_id', 'reward_item_modify_price', 'additional_item_class_id', 'additional_reward_item_class_id', 'additional_reward_item_num', 'additional_gain_rate']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('reward_item_class_id'), data.get('reward_item_modify_price'), data.get('additional_item_class_id'), data.get('additional_reward_item_class_id'), data.get('additional_reward_item_num'), data.get('additional_gain_rate'))
    
    def __str__(self):
        return f"LollyCubeData(skill_id={self.skill_id}, skill_level={self.skill_level}, reward_item_class_id={self.reward_item_class_id}, reward_item_modify_price={self.reward_item_modify_price}, additional_item_class_id={self.additional_item_class_id}, additional_reward_item_class_id={self.additional_reward_item_class_id}, additional_reward_item_num={self.additional_reward_item_num}, additional_gain_rate={self.additional_gain_rate})"



class Mable(object):

    def __init__(self, cell_id, cell_color, cell_name, cell_reward, event_group_Id):
        self.cell_id = cell_id
        self.cell_color = cell_color
        self.cell_name = cell_name
        self.cell_reward = cell_reward
        self.event_group_Id = event_group_Id

    @classmethod
    def from_string(self, line) -> 'Mable':
        split_params = line.split('\t')[1:-1]
        attributes = ['cell_id', 'cell_color', 'cell_name', 'cell_reward', 'event_group_Id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('cell_id'), data.get('cell_color'), data.get('cell_name'), data.get('cell_reward'), data.get('event_group_Id'))
    
    def __str__(self):
        return f"Mable(cell_id={self.cell_id}, cell_color={self.cell_color}, cell_name={self.cell_name}, cell_reward={self.cell_reward}, event_group_Id={self.event_group_Id})"



class MableGame(object):

    def __init__(self, cell_id, cell_color, cell_name, cell_reward, event_group_Id):
        self.cell_id = cell_id
        self.cell_color = cell_color
        self.cell_name = cell_name
        self.cell_reward = cell_reward
        self.event_group_Id = event_group_Id

    @classmethod
    def from_string(self, line) -> 'MableGame':
        split_params = line.split('\t')[1:-1]
        attributes = ['cell_id', 'cell_color', 'cell_name', 'cell_reward', 'event_group_Id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('cell_id'), data.get('cell_color'), data.get('cell_name'), data.get('cell_reward'), data.get('event_group_Id'))
    
    def __str__(self):
        return f"MableGame(cell_id={self.cell_id}, cell_color={self.cell_color}, cell_name={self.cell_name}, cell_reward={self.cell_reward}, event_group_Id={self.event_group_Id})"



class MableGameEvent(object):

    def __init__(self, event_group, event_id, event_group_description, event_description):
        self.event_group = event_group
        self.event_id = event_id
        self.event_group_description = event_group_description
        self.event_description = event_description

    @classmethod
    def from_string(self, line) -> 'MableGameEvent':
        split_params = line.split('\t')[1:-1]
        attributes = ['event_group', 'event_id', 'event_group_description', 'event_description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('event_group'), data.get('event_id'), data.get('event_group_description'), data.get('event_description'))
    
    def __str__(self):
        return f"MableGameEvent(event_group={self.event_group}, event_id={self.event_id}, event_group_description={self.event_group_description}, event_description={self.event_description})"



class MantleException(object):

    def __init__(self, object_id, texture):
        self.object_id = object_id
        self.texture = texture

    @classmethod
    def from_string(self, line) -> 'MantleException':
        split_params = line.split('\t')[1:-1]
        attributes = ['object_id', 'texture']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('object_id'), data.get('texture'))
    
    def __str__(self):
        return f"MantleException(object_id={self.object_id}, texture={self.texture})"



class MissionLevel(object):

    def __init__(self, season_date, limit_lv, start_level, lcoin_amount, base_reward, key_reward, special_reward, extra_reward):
        self.season_date = season_date
        self.limit_lv = limit_lv
        self.start_level = start_level
        self.lcoin_amount = lcoin_amount
        self.base_reward = base_reward
        self.key_reward = key_reward
        self.special_reward = special_reward
        self.extra_reward = extra_reward

    @classmethod
    def from_string(self, line) -> 'MissionLevel':
        split_params = line.split('\t')[1:-1]
        attributes = ['season_date', 'limit_lv', 'start_level', 'lcoin_amount', 'base_reward', 'key_reward', 'special_reward', 'extra_reward']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('season_date'), data.get('limit_lv'), data.get('start_level'), data.get('lcoin_amount'), data.get('base_reward'), data.get('key_reward'), data.get('special_reward'), data.get('extra_reward'))
    
    def __str__(self):
        return f"MissionLevel(season_date={self.season_date}, limit_lv={self.limit_lv}, start_level={self.start_level}, lcoin_amount={self.lcoin_amount}, base_reward={self.base_reward}, key_reward={self.key_reward}, special_reward={self.special_reward}, extra_reward={self.extra_reward})"



class MobSkillAnimgrp(AbstractItemInfo):

    def __init__(self, npc_id, skill_id, seq_name):
        super().__init__(object_id)
        self.npc_id = npc_id
        self.skill_id = skill_id
        self.seq_name = seq_name

    @classmethod
    def from_string(cls, line) -> 'MobSkillAnimgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_id', 'skill_id', 'seq_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('npc_id'), data.get('skill_id'), data.get('seq_name'))
    
    def __str__(self):
        return f"MobSkillAnimgrp(npc_id={self.npc_id}, skill_id={self.skill_id}, seq_name={self.seq_name})"



class MonsterBook(object):

    def __init__(self, id, trophy_id, npc_id, sort_order, npc_level, npc_conbonus, npc_menbonus, drop_item, card_texture, card_panel, zone_id, faction_id, reward_fp, reward_exp, reward_sp, reward_item_1, reward_item_2, reward_item_3, reward_item_4, view_x, view_y, view_s, view_rot, view_dist):
        self.id = id
        self.trophy_id = trophy_id
        self.npc_id = npc_id
        self.sort_order = sort_order
        self.npc_level = npc_level
        self.npc_conbonus = npc_conbonus
        self.npc_menbonus = npc_menbonus
        self.drop_item = drop_item
        self.card_texture = card_texture
        self.card_panel = card_panel
        self.zone_id = zone_id
        self.faction_id = faction_id
        self.reward_fp = reward_fp
        self.reward_exp = reward_exp
        self.reward_sp = reward_sp
        self.reward_item_1 = reward_item_1
        self.reward_item_2 = reward_item_2
        self.reward_item_3 = reward_item_3
        self.reward_item_4 = reward_item_4
        self.view_x = view_x
        self.view_y = view_y
        self.view_s = view_s
        self.view_rot = view_rot
        self.view_dist = view_dist

    @classmethod
    def from_string(self, line) -> 'MonsterBook':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'trophy_id', 'npc_id', 'sort_order', 'npc_level', 'npc_conbonus', 'npc_menbonus', 'drop_item', 'card_texture', 'card_panel', 'zone_id', 'faction_id', 'reward_fp', 'reward_exp', 'reward_sp', 'reward_item_1', 'reward_item_2', 'reward_item_3', 'reward_item_4', 'view_x', 'view_y', 'view_s', 'view_rot', 'view_dist']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('trophy_id'), data.get('npc_id'), data.get('sort_order'), data.get('npc_level'), data.get('npc_conbonus'), data.get('npc_menbonus'), data.get('drop_item'), data.get('card_texture'), data.get('card_panel'), data.get('zone_id'), data.get('faction_id'), data.get('reward_fp'), data.get('reward_exp'), data.get('reward_sp'), data.get('reward_item_1'), data.get('reward_item_2'), data.get('reward_item_3'), data.get('reward_item_4'), data.get('view_x'), data.get('view_y'), data.get('view_s'), data.get('view_rot'), data.get('view_dist'))
    
    def __str__(self):
        return f"MonsterBook(id={self.id}, trophy_id={self.trophy_id}, npc_id={self.npc_id}, sort_order={self.sort_order}, npc_level={self.npc_level}, npc_conbonus={self.npc_conbonus}, npc_menbonus={self.npc_menbonus}, drop_item={self.drop_item}, card_texture={self.card_texture}, card_panel={self.card_panel}, zone_id={self.zone_id}, faction_id={self.faction_id}, reward_fp={self.reward_fp}, reward_exp={self.reward_exp}, reward_sp={self.reward_sp}, reward_item_1={self.reward_item_1}, reward_item_2={self.reward_item_2}, reward_item_3={self.reward_item_3}, reward_item_4={self.reward_item_4}, view_x={self.view_x}, view_y={self.view_y}, view_s={self.view_s}, view_rot={self.view_rot}, view_dist={self.view_dist})"



class MSAffectData(object):

    def __init__(self, skill_id, skill_level, skill_sublevel, affect_range, decal, is_directional):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_sublevel = skill_sublevel
        self.affect_range = affect_range
        self.decal = decal
        self.is_directional = is_directional

    @classmethod
    def from_string(self, line) -> 'MSAffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_sublevel', 'affect_range', 'decal', 'is_directional']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('skill_sublevel'), data.get('affect_range'), data.get('decal'), data.get('is_directional'))
    
    def __str__(self):
        return f"MSAffectData(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_sublevel={self.skill_sublevel}, affect_range={self.affect_range}, decal={self.decal}, is_directional={self.is_directional})"



class MSConditionData(object):

    def __init__(self, skill_id, skill_level, skill_sublevel, mask, equiptype, attackitemtype, stattype, statpercentage, up, hpconsume, mpconsume1, mpconsume2, itemid, itemnum, casterpriorskilllist, targetpriorskilllist, classtype, casterwithoutskilllist):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_sublevel = skill_sublevel
        self.mask = mask
        self.equiptype = equiptype
        self.attackitemtype = attackitemtype
        self.stattype = stattype
        self.statpercentage = statpercentage
        self.up = up
        self.hpconsume = hpconsume
        self.mpconsume1 = mpconsume1
        self.mpconsume2 = mpconsume2
        self.itemid = itemid
        self.itemnum = itemnum
        self.casterpriorskilllist = casterpriorskilllist
        self.targetpriorskilllist = targetpriorskilllist
        self.classtype = classtype
        self.casterwithoutskilllist = casterwithoutskilllist

    @classmethod
    def from_string(self, line) -> 'MSConditionData':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_sublevel', 'mask', 'equiptype', 'attackitemtype', 'stattype', 'statpercentage', 'up', 'hpconsume', 'mpconsume1', 'mpconsume2', 'itemid', 'itemnum', 'casterpriorskilllist', 'targetpriorskilllist', 'classtype', 'casterwithoutskilllist']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('skill_sublevel'), data.get('mask'), data.get('equiptype'), data.get('attackitemtype'), data.get('stattype'), data.get('statpercentage'), data.get('up'), data.get('hpconsume'), data.get('mpconsume1'), data.get('mpconsume2'), data.get('itemid'), data.get('itemnum'), data.get('casterpriorskilllist'), data.get('targetpriorskilllist'), data.get('classtype'), data.get('casterwithoutskilllist'))
    
    def __str__(self):
        return f"MSConditionData(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_sublevel={self.skill_sublevel}, mask={self.mask}, equiptype={self.equiptype}, attackitemtype={self.attackitemtype}, stattype={self.stattype}, statpercentage={self.statpercentage}, up={self.up}, hpconsume={self.hpconsume}, mpconsume1={self.mpconsume1}, mpconsume2={self.mpconsume2}, itemid={self.itemid}, itemnum={self.itemnum}, casterpriorskilllist={self.casterpriorskilllist}, targetpriorskilllist={self.targetpriorskilllist}, classtype={self.classtype}, casterwithoutskilllist={self.casterwithoutskilllist})"



class MusicInfo(object):

    def __init__(self, id, title):
        self.id = id
        self.title = title

    @classmethod
    def from_string(self, line) -> 'MusicInfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'title']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('title'))
    
    def __str__(self):
        return f"MusicInfo(id={self.id}, title={self.title})"



class NewQuestData(object):

    def __init__(self, quest_id, quest_type, quest_name, quest_level, pre_quest, clazz, quest_item, start_item, start_npc, start_npc_loc, end_npc, end_npc_loc, quest_loc, goal_string, goal_num, reward_level, reward_exp, reward_sp, reward_item):
        self.quest_id = quest_id
        self.quest_type = quest_type
        self.quest_name = quest_name
        self.quest_level = quest_level
        self.pre_quest = pre_quest
        self.clazz = clazz
        self.quest_item = quest_item
        self.start_item = start_item
        self.start_npc = start_npc
        self.start_npc_loc = start_npc_loc
        self.end_npc = end_npc
        self.end_npc_loc = end_npc_loc
        self.quest_loc = quest_loc
        self.goal_string = goal_string
        self.goal_num = goal_num
        self.reward_level = reward_level
        self.reward_exp = reward_exp
        self.reward_sp = reward_sp
        self.reward_item = reward_item

    @classmethod
    def from_string(self, line) -> 'NewQuestData':
        split_params = line.split('\t')[1:-1]
        attributes = ['quest_id', 'quest_type', 'quest_name', 'quest_level', 'pre_quest', 'clazz', 'quest_item', 'start_item', 'start_npc', 'start_npc_loc', 'end_npc', 'end_npc_loc', 'quest_loc', 'goal_string', 'goal_num', 'reward_level', 'reward_exp', 'reward_sp', 'reward_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('quest_id'), data.get('quest_type'), data.get('quest_name'), data.get('quest_level'), data.get('pre_quest'), data.get('clazz'), data.get('quest_item'), data.get('start_item'), data.get('start_npc'), data.get('start_npc_loc'), data.get('end_npc'), data.get('end_npc_loc'), data.get('quest_loc'), data.get('goal_string'), data.get('goal_num'), data.get('reward_level'), data.get('reward_exp'), data.get('reward_sp'), data.get('reward_item'))
    
    def __str__(self):
        return f"NewQuestData(quest_id={self.quest_id}, quest_type={self.quest_type}, quest_name={self.quest_name}, quest_level={self.quest_level}, pre_quest={self.pre_quest}, clazz={self.clazz}, quest_item={self.quest_item}, start_item={self.start_item}, start_npc={self.start_npc}, start_npc_loc={self.start_npc_loc}, end_npc={self.end_npc}, end_npc_loc={self.end_npc_loc}, quest_loc={self.quest_loc}, goal_string={self.goal_string}, goal_num={self.goal_num}, reward_level={self.reward_level}, reward_exp={self.reward_exp}, reward_sp={self.reward_sp}, reward_item={self.reward_item})"



class NewQuestData(object):

    def __init__(self, quest_id, quest_type, quest_name, quest_level, pre_quest, clazz, quest_item, start_item, start_npc, start_npc_loc, end_npc, end_npc_loc, quest_loc, goal_string, goal_num, reward_level, reward_exp, reward_sp, reward_item):
        self.quest_id = quest_id
        self.quest_type = quest_type
        self.quest_name = quest_name
        self.quest_level = quest_level
        self.pre_quest = pre_quest
        self.clazz = clazz
        self.quest_item = quest_item
        self.start_item = start_item
        self.start_npc = start_npc
        self.start_npc_loc = start_npc_loc
        self.end_npc = end_npc
        self.end_npc_loc = end_npc_loc
        self.quest_loc = quest_loc
        self.goal_string = goal_string
        self.goal_num = goal_num
        self.reward_level = reward_level
        self.reward_exp = reward_exp
        self.reward_sp = reward_sp
        self.reward_item = reward_item

    @classmethod
    def from_string(self, line) -> 'NewQuestData':
        split_params = line.split('\t')[1:-1]
        attributes = ['quest_id', 'quest_type', 'quest_name', 'quest_level', 'pre_quest', 'clazz', 'quest_item', 'start_item', 'start_npc', 'start_npc_loc', 'end_npc', 'end_npc_loc', 'quest_loc', 'goal_string', 'goal_num', 'reward_level', 'reward_exp', 'reward_sp', 'reward_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('quest_id'), data.get('quest_type'), data.get('quest_name'), data.get('quest_level'), data.get('pre_quest'), data.get('clazz'), data.get('quest_item'), data.get('start_item'), data.get('start_npc'), data.get('start_npc_loc'), data.get('end_npc'), data.get('end_npc_loc'), data.get('quest_loc'), data.get('goal_string'), data.get('goal_num'), data.get('reward_level'), data.get('reward_exp'), data.get('reward_sp'), data.get('reward_item'))
    
    def __str__(self):
        return f"NewQuestData(quest_id={self.quest_id}, quest_type={self.quest_type}, quest_name={self.quest_name}, quest_level={self.quest_level}, pre_quest={self.pre_quest}, clazz={self.clazz}, quest_item={self.quest_item}, start_item={self.start_item}, start_npc={self.start_npc}, start_npc_loc={self.start_npc_loc}, end_npc={self.end_npc}, end_npc_loc={self.end_npc_loc}, quest_loc={self.quest_loc}, goal_string={self.goal_string}, goal_num={self.goal_num}, reward_level={self.reward_level}, reward_exp={self.reward_exp}, reward_sp={self.reward_sp}, reward_item={self.reward_item})"



class NewQuestDialog(object):

    def __init__(self, quest_id, start_dialog, accept_dialog, complete_dialog, end_dialog, quest_info):
        self.quest_id = quest_id
        self.start_dialog = start_dialog
        self.accept_dialog = accept_dialog
        self.complete_dialog = complete_dialog
        self.end_dialog = end_dialog
        self.quest_info = quest_info

    @classmethod
    def from_string(self, line) -> 'NewQuestDialog':
        split_params = line.split('\t')[1:-1]
        attributes = ['quest_id', 'start_dialog', 'accept_dialog', 'complete_dialog', 'end_dialog', 'quest_info']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('quest_id'), data.get('start_dialog'), data.get('accept_dialog'), data.get('complete_dialog'), data.get('end_dialog'), data.get('quest_info'))
    
    def __str__(self):
        return f"NewQuestDialog(quest_id={self.quest_id}, start_dialog={self.start_dialog}, accept_dialog={self.accept_dialog}, complete_dialog={self.complete_dialog}, end_dialog={self.end_dialog}, quest_info={self.quest_info})"



class NewQuestDialog(object):

    def __init__(self, quest_id, start_dialog, accept_dialog, complete_dialog, end_dialog, quest_info):
        self.quest_id = quest_id
        self.start_dialog = start_dialog
        self.accept_dialog = accept_dialog
        self.complete_dialog = complete_dialog
        self.end_dialog = end_dialog
        self.quest_info = quest_info

    @classmethod
    def from_string(self, line) -> 'NewQuestDialog':
        split_params = line.split('\t')[1:-1]
        attributes = ['quest_id', 'start_dialog', 'accept_dialog', 'complete_dialog', 'end_dialog', 'quest_info']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('quest_id'), data.get('start_dialog'), data.get('accept_dialog'), data.get('complete_dialog'), data.get('end_dialog'), data.get('quest_info'))
    
    def __str__(self):
        return f"NewQuestDialog(quest_id={self.quest_id}, start_dialog={self.start_dialog}, accept_dialog={self.accept_dialog}, complete_dialog={self.complete_dialog}, end_dialog={self.end_dialog}, quest_info={self.quest_info})"



class NewQuestNpcPortrait(object):

    def __init__(self, npc_id, view_offsetX, view_offsetY, view_offsetZ, view_dist, view_rotationYaw, view_scale):
        self.npc_id = npc_id
        self.view_offsetX = view_offsetX
        self.view_offsetY = view_offsetY
        self.view_offsetZ = view_offsetZ
        self.view_dist = view_dist
        self.view_rotationYaw = view_rotationYaw
        self.view_scale = view_scale

    @classmethod
    def from_string(self, line) -> 'NewQuestNpcPortrait':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_id', 'view_offsetX', 'view_offsetY', 'view_offsetZ', 'view_dist', 'view_rotationYaw', 'view_scale']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('npc_id'), data.get('view_offsetX'), data.get('view_offsetY'), data.get('view_offsetZ'), data.get('view_dist'), data.get('view_rotationYaw'), data.get('view_scale'))
    
    def __str__(self):
        return f"NewQuestNpcPortrait(npc_id={self.npc_id}, view_offsetX={self.view_offsetX}, view_offsetY={self.view_offsetY}, view_offsetZ={self.view_offsetZ}, view_dist={self.view_dist}, view_rotationYaw={self.view_rotationYaw}, view_scale={self.view_scale})"



class NickNameItem(object):

    def __init__(self, id, color, icon):
        self.id = id
        self.color = color
        self.icon = icon

    @classmethod
    def from_string(self, line) -> 'NickNameItem':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'color', 'icon']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('color'), data.get('icon'))
    
    def __str__(self):
        return f"NickNameItem(id={self.id}, color={self.color}, icon={self.icon})"



class NonAttackingSkillAnim(object):

    def __init__(self, Animation, NonAtkAnimation):
        self.Animation = Animation
        self.NonAtkAnimation = NonAtkAnimation

    @classmethod
    def from_string(self, line) -> 'NonAttackingSkillAnim':
        split_params = line.split('\t')[1:-1]
        attributes = ['Animation', 'NonAtkAnimation']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('Animation'), data.get('NonAtkAnimation'))
    
    def __str__(self):
        return f"NonAttackingSkillAnim(Animation={self.Animation}, NonAtkAnimation={self.NonAtkAnimation})"



class Npcgrp(AbstractItemInfo):

    def __init__(self, npc_id, class_name, mesh_name, texture_name, texture_name_second, property_list, npc_speed, attack_sound1, defense_sound1, damage_sound, deco_effect, quest, attack_effect, sound_vol, sound_radius, sound_random, social, hpshowable, dialog_sound, Silhouette, summon_sort, summon_max_count, summon_grade, drawscale, use_zoomincam, npc_icon_name, sound_priority, ground_high, ground_low, collision_radius, collision_radius_2, collision_height, collision_height_2, slot_lhand, slot_rhand, slot_chest, org_hp, org_mp, npc_type):
        super().__init__(object_id)
        self.npc_id = npc_id
        self.class_name = class_name
        self.mesh_name = mesh_name
        self.texture_name = texture_name
        self.texture_name_second = texture_name_second
        self.property_list = property_list
        self.npc_speed = npc_speed
        self.attack_sound1 = attack_sound1
        self.defense_sound1 = defense_sound1
        self.damage_sound = damage_sound
        self.deco_effect = deco_effect
        self.quest = quest
        self.attack_effect = attack_effect
        self.sound_vol = sound_vol
        self.sound_radius = sound_radius
        self.sound_random = sound_random
        self.social = social
        self.hpshowable = hpshowable
        self.dialog_sound = dialog_sound
        self.Silhouette = Silhouette
        self.summon_sort = summon_sort
        self.summon_max_count = summon_max_count
        self.summon_grade = summon_grade
        self.drawscale = drawscale
        self.use_zoomincam = use_zoomincam
        self.npc_icon_name = npc_icon_name
        self.sound_priority = sound_priority
        self.ground_high = ground_high
        self.ground_low = ground_low
        self.collision_radius = collision_radius
        self.collision_radius_2 = collision_radius_2
        self.collision_height = collision_height
        self.collision_height_2 = collision_height_2
        self.slot_lhand = slot_lhand
        self.slot_rhand = slot_rhand
        self.slot_chest = slot_chest
        self.org_hp = org_hp
        self.org_mp = org_mp
        self.npc_type = npc_type

    @classmethod
    def from_string(cls, line) -> 'Npcgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_id', 'class_name', 'mesh_name', 'texture_name', 'texture_name_second', 'property_list', 'npc_speed', 'attack_sound1', 'defense_sound1', 'damage_sound', 'deco_effect', 'quest', 'attack_effect', 'sound_vol', 'sound_radius', 'sound_random', 'social', 'hpshowable', 'dialog_sound', 'Silhouette', 'summon_sort', 'summon_max_count', 'summon_grade', 'drawscale', 'use_zoomincam', 'npc_icon_name', 'sound_priority', 'ground_high', 'ground_low', 'collision_radius', 'collision_radius_2', 'collision_height', 'collision_height_2', 'slot_lhand', 'slot_rhand', 'slot_chest', 'org_hp', 'org_mp', 'npc_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('npc_id'), data.get('class_name'), data.get('mesh_name'), data.get('texture_name'), data.get('texture_name_second'), data.get('property_list'), data.get('npc_speed'), data.get('attack_sound1'), data.get('defense_sound1'), data.get('damage_sound'), data.get('deco_effect'), data.get('quest'), data.get('attack_effect'), data.get('sound_vol'), data.get('sound_radius'), data.get('sound_random'), data.get('social'), data.get('hpshowable'), data.get('dialog_sound'), data.get('Silhouette'), data.get('summon_sort'), data.get('summon_max_count'), data.get('summon_grade'), data.get('drawscale'), data.get('use_zoomincam'), data.get('npc_icon_name'), data.get('sound_priority'), data.get('ground_high'), data.get('ground_low'), data.get('collision_radius'), data.get('collision_radius_2'), data.get('collision_height'), data.get('collision_height_2'), data.get('slot_lhand'), data.get('slot_rhand'), data.get('slot_chest'), data.get('org_hp'), data.get('org_mp'), data.get('npc_type'))
    
    def __str__(self):
        return f"Npcgrp(npc_id={self.npc_id}, class_name={self.class_name}, mesh_name={self.mesh_name}, texture_name={self.texture_name}, texture_name_second={self.texture_name_second}, property_list={self.property_list}, npc_speed={self.npc_speed}, attack_sound1={self.attack_sound1}, defense_sound1={self.defense_sound1}, damage_sound={self.damage_sound}, deco_effect={self.deco_effect}, quest={self.quest}, attack_effect={self.attack_effect}, sound_vol={self.sound_vol}, sound_radius={self.sound_radius}, sound_random={self.sound_random}, social={self.social}, hpshowable={self.hpshowable}, dialog_sound={self.dialog_sound}, Silhouette={self.Silhouette}, summon_sort={self.summon_sort}, summon_max_count={self.summon_max_count}, summon_grade={self.summon_grade}, drawscale={self.drawscale}, use_zoomincam={self.use_zoomincam}, npc_icon_name={self.npc_icon_name}, sound_priority={self.sound_priority}, ground_high={self.ground_high}, ground_low={self.ground_low}, collision_radius={self.collision_radius}, collision_radius_2={self.collision_radius_2}, collision_height={self.collision_height}, collision_height_2={self.collision_height_2}, slot_lhand={self.slot_lhand}, slot_rhand={self.slot_rhand}, slot_chest={self.slot_chest}, org_hp={self.org_hp}, org_mp={self.org_mp}, npc_type={self.npc_type})"



class NpcName(object):

    def __init__(self, id, name, nick, nickcolor):
        self.id = id
        self.name = name
        self.nick = nick
        self.nickcolor = nickcolor

    @classmethod
    def from_string(self, line) -> 'NpcName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'nick', 'nickcolor']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('nick'), data.get('nickcolor'))
    
    def __str__(self):
        return f"NpcName(id={self.id}, name={self.name}, nick={self.nick}, nickcolor={self.nickcolor})"



class NpcName(object):

    def __init__(self, id, name, nick, nickcolor):
        self.id = id
        self.name = name
        self.nick = nick
        self.nickcolor = nickcolor

    @classmethod
    def from_string(self, line) -> 'NpcName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'nick', 'nickcolor']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('nick'), data.get('nickcolor'))
    
    def __str__(self):
        return f"NpcName(id={self.id}, name={self.name}, nick={self.nick}, nickcolor={self.nickcolor})"



class NpcString(object):

    def __init__(self, stringID, string):
        self.stringID = stringID
        self.string = string

    @classmethod
    def from_string(self, line) -> 'NpcString':
        split_params = line.split('\t')[1:-1]
        attributes = ['stringID', 'string']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('stringID'), data.get('string'))
    
    def __str__(self):
        return f"NpcString(stringID={self.stringID}, string={self.string})"



class NpcString(object):

    def __init__(self, stringID, string):
        self.stringID = stringID
        self.string = string

    @classmethod
    def from_string(self, line) -> 'NpcString':
        split_params = line.split('\t')[1:-1]
        attributes = ['stringID', 'string']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('stringID'), data.get('string'))
    
    def __str__(self):
        return f"NpcString(stringID={self.stringID}, string={self.string})"



class NPCTeleporter(object):

    def __init__(self, npc_id, npc_loc, teleport_zone_id, unk):
        self.npc_id = npc_id
        self.npc_loc = npc_loc
        self.teleport_zone_id = teleport_zone_id
        self.unk = unk

    @classmethod
    def from_string(self, line) -> 'NPCTeleporter':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_id', 'npc_loc', 'teleport_zone_id', 'unk']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('npc_id'), data.get('npc_loc'), data.get('teleport_zone_id'), data.get('unk'))
    
    def __str__(self):
        return f"NPCTeleporter(npc_id={self.npc_id}, npc_loc={self.npc_loc}, teleport_zone_id={self.teleport_zone_id}, unk={self.unk})"



class NserviceTopping(object):

    def __init__(self, skill_id, skill_level, sub_level, slot_num, is_default):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.sub_level = sub_level
        self.slot_num = slot_num
        self.is_default = is_default

    @classmethod
    def from_string(self, line) -> 'NserviceTopping':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'sub_level', 'slot_num', 'is_default']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('sub_level'), data.get('slot_num'), data.get('is_default'))
    
    def __str__(self):
        return f"NserviceTopping(skill_id={self.skill_id}, skill_level={self.skill_level}, sub_level={self.sub_level}, slot_num={self.slot_num}, is_default={self.is_default})"



class NserviceToppingBuff(object):

    def __init__(self, skill_id, skill_level, sub_level, slot_num, is_default):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.sub_level = sub_level
        self.slot_num = slot_num
        self.is_default = is_default

    @classmethod
    def from_string(self, line) -> 'NserviceToppingBuff':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'sub_level', 'slot_num', 'is_default']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('sub_level'), data.get('slot_num'), data.get('is_default'))
    
    def __str__(self):
        return f"NserviceToppingBuff(skill_id={self.skill_id}, skill_level={self.skill_level}, sub_level={self.sub_level}, slot_num={self.slot_num}, is_default={self.is_default})"



class Obscene(object):

    def __init__(self, id, string):
        self.id = id
        self.string = string

    @classmethod
    def from_string(self, line) -> 'Obscene':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'string']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('string'))
    
    def __str__(self):
        return f"Obscene(id={self.id}, string={self.string})"



class OneDayReward(object):

    def __init__(self, id, reward_id, reward_name, reward_desc, reward_period, class_filter, reset_period, condition_count, condition_level, can_condition_level, can_condition_day, category, check_type, server_range, show_server, reward_item, targetloc_scale):
        self.id = id
        self.reward_id = reward_id
        self.reward_name = reward_name
        self.reward_desc = reward_desc
        self.reward_period = reward_period
        self.class_filter = class_filter
        self.reset_period = reset_period
        self.condition_count = condition_count
        self.condition_level = condition_level
        self.can_condition_level = can_condition_level
        self.can_condition_day = can_condition_day
        self.category = category
        self.check_type = check_type
        self.server_range = server_range
        self.show_server = show_server
        self.reward_item = reward_item
        self.targetloc_scale = targetloc_scale

    @classmethod
    def from_string(self, line) -> 'OneDayReward':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'reward_id', 'reward_name', 'reward_desc', 'reward_period', 'class_filter', 'reset_period', 'condition_count', 'condition_level', 'can_condition_level', 'can_condition_day', 'category', 'check_type', 'server_range', 'show_server', 'reward_item', 'targetloc_scale']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('reward_id'), data.get('reward_name'), data.get('reward_desc'), data.get('reward_period'), data.get('class_filter'), data.get('reset_period'), data.get('condition_count'), data.get('condition_level'), data.get('can_condition_level'), data.get('can_condition_day'), data.get('category'), data.get('check_type'), data.get('server_range'), data.get('show_server'), data.get('reward_item'), data.get('targetloc_scale'))
    
    def __str__(self):
        return f"OneDayReward(id={self.id}, reward_id={self.reward_id}, reward_name={self.reward_name}, reward_desc={self.reward_desc}, reward_period={self.reward_period}, class_filter={self.class_filter}, reset_period={self.reset_period}, condition_count={self.condition_count}, condition_level={self.condition_level}, can_condition_level={self.can_condition_level}, can_condition_day={self.can_condition_day}, category={self.category}, check_type={self.check_type}, server_range={self.server_range}, show_server={self.show_server}, reward_item={self.reward_item}, targetloc_scale={self.targetloc_scale})"



class Optiondata(object):

    def __init__(self, option_id, option_quality, option_type, option_desc1, option_desc2, option_desc3):
        self.option_id = option_id
        self.option_quality = option_quality
        self.option_type = option_type
        self.option_desc1 = option_desc1
        self.option_desc2 = option_desc2
        self.option_desc3 = option_desc3

    @classmethod
    def from_string(self, line) -> 'Optiondata':
        split_params = line.split('\t')[1:-1]
        attributes = ['option_id', 'option_quality', 'option_type', 'option_desc1', 'option_desc2', 'option_desc3']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('option_id'), data.get('option_quality'), data.get('option_type'), data.get('option_desc1'), data.get('option_desc2'), data.get('option_desc3'))
    
    def __str__(self):
        return f"Optiondata(option_id={self.option_id}, option_quality={self.option_quality}, option_type={self.option_type}, option_desc1={self.option_desc1}, option_desc2={self.option_desc2}, option_desc3={self.option_desc3})"



class OptiondataClient(object):

    def __init__(self, option_id, option_quality, option_type, option_desc1, option_desc2, option_desc3):
        self.option_id = option_id
        self.option_quality = option_quality
        self.option_type = option_type
        self.option_desc1 = option_desc1
        self.option_desc2 = option_desc2
        self.option_desc3 = option_desc3

    @classmethod
    def from_string(self, line) -> 'OptiondataClient':
        split_params = line.split('\t')[1:-1]
        attributes = ['option_id', 'option_quality', 'option_type', 'option_desc1', 'option_desc2', 'option_desc3']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('option_id'), data.get('option_quality'), data.get('option_type'), data.get('option_desc1'), data.get('option_desc2'), data.get('option_desc3'))
    
    def __str__(self):
        return f"OptiondataClient(option_id={self.option_id}, option_quality={self.option_quality}, option_type={self.option_type}, option_desc1={self.option_desc1}, option_desc2={self.option_desc2}, option_desc3={self.option_desc3})"



class PawnAnimData(object):

    def __init__(self, name, texture_params, int_params, int_params2, float_params):
        self.name = name
        self.texture_params = texture_params
        self.int_params = int_params
        self.int_params2 = int_params2
        self.float_params = float_params

    @classmethod
    def from_string(self, line) -> 'PawnAnimData':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'texture_params', 'int_params', 'int_params2', 'float_params']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('texture_params'), data.get('int_params'), data.get('int_params2'), data.get('float_params'))
    
    def __str__(self):
        return f"PawnAnimData(name={self.name}, texture_params={self.texture_params}, int_params={self.int_params}, int_params2={self.int_params2}, float_params={self.float_params})"



class PetAcquireSkill(object):

    def __init__(self, pet_id, acquire_skills):
        self.pet_id = pet_id
        self.acquire_skills = acquire_skills

    @classmethod
    def from_string(self, line) -> 'PetAcquireSkill':
        split_params = line.split('\t')[1:-1]
        attributes = ['pet_id', 'acquire_skills']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('pet_id'), data.get('acquire_skills'))
    
    def __str__(self):
        return f"PetAcquireSkill(pet_id={self.pet_id}, acquire_skills={self.acquire_skills})"



class PetEvolve(object):

    def __init__(self, pet_id, evolve_step, evolve_condition, evolve_cost):
        self.pet_id = pet_id
        self.evolve_step = evolve_step
        self.evolve_condition = evolve_condition
        self.evolve_cost = evolve_cost

    @classmethod
    def from_string(self, line) -> 'PetEvolve':
        split_params = line.split('\t')[1:-1]
        attributes = ['pet_id', 'evolve_step', 'evolve_condition', 'evolve_cost']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('pet_id'), data.get('evolve_step'), data.get('evolve_condition'), data.get('evolve_cost'))
    
    def __str__(self):
        return f"PetEvolve(pet_id={self.pet_id}, evolve_step={self.evolve_step}, evolve_condition={self.evolve_condition}, evolve_cost={self.evolve_cost})"



class PetLook(object):

    def __init__(self, look_id, ave, name, desc):
        self.look_id = look_id
        self.ave = ave
        self.name = name
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'PetLook':
        split_params = line.split('\t')[1:-1]
        attributes = ['look_id', 'ave', 'name', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('look_id'), data.get('ave'), data.get('name'), data.get('desc'))
    
    def __str__(self):
        return f"PetLook(look_id={self.look_id}, ave={self.ave}, name={self.name}, desc={self.desc})"



class PetName(object):

    def __init__(self, id, skill_id, skill_level, name, desc):
        self.id = id
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.name = name
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'PetName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'skill_id', 'skill_level', 'name', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('skill_id'), data.get('skill_level'), data.get('name'), data.get('desc'))
    
    def __str__(self):
        return f"PetName(id={self.id}, skill_id={self.skill_id}, skill_level={self.skill_level}, name={self.name}, desc={self.desc})"



class PetRaceEmblem(object):

    def __init__(self, pet_id, pet_type, unk, name, race_emblem, HUD_emblem_tex_name):
        self.pet_id = pet_id
        self.pet_type = pet_type
        self.unk = unk
        self.name = name
        self.race_emblem = race_emblem
        self.HUD_emblem_tex_name = HUD_emblem_tex_name

    @classmethod
    def from_string(self, line) -> 'PetRaceEmblem':
        split_params = line.split('\t')[1:-1]
        attributes = ['pet_id', 'pet_type', 'unk', 'name', 'race_emblem', 'HUD_emblem_tex_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('pet_id'), data.get('pet_type'), data.get('unk'), data.get('name'), data.get('race_emblem'), data.get('HUD_emblem_tex_name'))
    
    def __str__(self):
        return f"PetRaceEmblem(pet_id={self.pet_id}, pet_type={self.pet_type}, unk={self.unk}, name={self.name}, race_emblem={self.race_emblem}, HUD_emblem_tex_name={self.HUD_emblem_tex_name})"



class PetExtract(object):

    def __init__(self, key, pet_id, pet_level, extract_exp, extract_item, default_cost, extract_cost):
        self.key = key
        self.pet_id = pet_id
        self.pet_level = pet_level
        self.extract_exp = extract_exp
        self.extract_item = extract_item
        self.default_cost = default_cost
        self.extract_cost = extract_cost

    @classmethod
    def from_string(self, line) -> 'PetExtract':
        split_params = line.split('\t')[1:-1]
        attributes = ['key', 'pet_id', 'pet_level', 'extract_exp', 'extract_item', 'default_cost', 'extract_cost']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('key'), data.get('pet_id'), data.get('pet_level'), data.get('extract_exp'), data.get('extract_item'), data.get('default_cost'), data.get('extract_cost'))
    
    def __str__(self):
        return f"PetExtract(key={self.key}, pet_id={self.pet_id}, pet_level={self.pet_level}, extract_exp={self.extract_exp}, extract_item={self.extract_item}, default_cost={self.default_cost}, extract_cost={self.extract_cost})"



class PledgeCrestPreset(object):

    def __init__(self, id, crest):
        self.id = id
        self.crest = crest

    @classmethod
    def from_string(self, line) -> 'PledgeCrestPreset':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'crest']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('crest'))
    
    def __str__(self):
        return f"PledgeCrestPreset(id={self.id}, crest={self.crest})"



class PledgeLevelDesc(object):

    def __init__(self, level, num_general, num_elite, level_desc):
        self.level = level
        self.num_general = num_general
        self.num_elite = num_elite
        self.level_desc = level_desc

    @classmethod
    def from_string(self, line) -> 'PledgeLevelDesc':
        split_params = line.split('\t')[1:-1]
        attributes = ['level', 'num_general', 'num_elite', 'level_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('level'), data.get('num_general'), data.get('num_elite'), data.get('level_desc'))
    
    def __str__(self):
        return f"PledgeLevelDesc(level={self.level}, num_general={self.num_general}, num_elite={self.num_elite}, level_desc={self.level_desc})"



class PledgeLevel(object):

    def __init__(self, level, need_pledge_exp, num_general, merit_desc, open_contents, selling_item_list, skill_name_list):
        self.level = level
        self.need_pledge_exp = need_pledge_exp
        self.num_general = num_general
        self.merit_desc = merit_desc
        self.open_contents = open_contents
        self.selling_item_list = selling_item_list
        self.skill_name_list = skill_name_list

    @classmethod
    def from_string(self, line) -> 'PledgeLevel':
        split_params = line.split('\t')[1:-1]
        attributes = ['level', 'need_pledge_exp', 'num_general', 'merit_desc', 'open_contents', 'selling_item_list', 'skill_name_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('level'), data.get('need_pledge_exp'), data.get('num_general'), data.get('merit_desc'), data.get('open_contents'), data.get('selling_item_list'), data.get('skill_name_list'))
    
    def __str__(self):
        return f"PledgeLevel(level={self.level}, need_pledge_exp={self.need_pledge_exp}, num_general={self.num_general}, merit_desc={self.merit_desc}, open_contents={self.open_contents}, selling_item_list={self.selling_item_list}, skill_name_list={self.skill_name_list})"



class PledgeMasteryInfo(object):

    def __init__(self, mastery_id, mastery_type, mastery_name, req_mastery, and_or, req_point, req_namevalue, pledge_skill, mastery_skill, duration, merit, description):
        self.mastery_id = mastery_id
        self.mastery_type = mastery_type
        self.mastery_name = mastery_name
        self.req_mastery = req_mastery
        self.and_or = and_or
        self.req_point = req_point
        self.req_namevalue = req_namevalue
        self.pledge_skill = pledge_skill
        self.mastery_skill = mastery_skill
        self.duration = duration
        self.merit = merit
        self.description = description

    @classmethod
    def from_string(self, line) -> 'PledgeMasteryInfo':
        split_params = line.split('\t')[1:-1]
        attributes = ['mastery_id', 'mastery_type', 'mastery_name', 'req_mastery', 'and_or', 'req_point', 'req_namevalue', 'pledge_skill', 'mastery_skill', 'duration', 'merit', 'description']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('mastery_id'), data.get('mastery_type'), data.get('mastery_name'), data.get('req_mastery'), data.get('and_or'), data.get('req_point'), data.get('req_namevalue'), data.get('pledge_skill'), data.get('mastery_skill'), data.get('duration'), data.get('merit'), data.get('description'))
    
    def __str__(self):
        return f"PledgeMasteryInfo(mastery_id={self.mastery_id}, mastery_type={self.mastery_type}, mastery_name={self.mastery_name}, req_mastery={self.req_mastery}, and_or={self.and_or}, req_point={self.req_point}, req_namevalue={self.req_namevalue}, pledge_skill={self.pledge_skill}, mastery_skill={self.mastery_skill}, duration={self.duration}, merit={self.merit}, description={self.description})"



class PledgeMission(object):

    def __init__(self, id, category, is_repeat, name, pledge_level, c_pledge_mastery, min_level, max_level, job_main, job_dual, job_sub, pre_mission_id, start_date, start_time, end_date, end_time, activate_time, deactivate_time, unknown_bytes, available_day, goal_desc, goal_count, reward_pledge_name_value, reward_pvp_point, reward_items):
        self.id = id
        self.category = category
        self.is_repeat = is_repeat
        self.name = name
        self.pledge_level = pledge_level
        self.c_pledge_mastery = c_pledge_mastery
        self.min_level = min_level
        self.max_level = max_level
        self.job_main = job_main
        self.job_dual = job_dual
        self.job_sub = job_sub
        self.pre_mission_id = pre_mission_id
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.activate_time = activate_time
        self.deactivate_time = deactivate_time
        self.unknown_bytes = unknown_bytes
        self.available_day = available_day
        self.goal_desc = goal_desc
        self.goal_count = goal_count
        self.reward_pledge_name_value = reward_pledge_name_value
        self.reward_pvp_point = reward_pvp_point
        self.reward_items = reward_items

    @classmethod
    def from_string(self, line) -> 'PledgeMission':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'category', 'is_repeat', 'name', 'pledge_level', 'c_pledge_mastery', 'min_level', 'max_level', 'job_main', 'job_dual', 'job_sub', 'pre_mission_id', 'start_date', 'start_time', 'end_date', 'end_time', 'activate_time', 'deactivate_time', 'unknown_bytes', 'available_day', 'goal_desc', 'goal_count', 'reward_pledge_name_value', 'reward_pvp_point', 'reward_items']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('category'), data.get('is_repeat'), data.get('name'), data.get('pledge_level'), data.get('c_pledge_mastery'), data.get('min_level'), data.get('max_level'), data.get('job_main'), data.get('job_dual'), data.get('job_sub'), data.get('pre_mission_id'), data.get('start_date'), data.get('start_time'), data.get('end_date'), data.get('end_time'), data.get('activate_time'), data.get('deactivate_time'), data.get('unknown_bytes'), data.get('available_day'), data.get('goal_desc'), data.get('goal_count'), data.get('reward_pledge_name_value'), data.get('reward_pvp_point'), data.get('reward_items'))
    
    def __str__(self):
        return f"PledgeMission(id={self.id}, category={self.category}, is_repeat={self.is_repeat}, name={self.name}, pledge_level={self.pledge_level}, c_pledge_mastery={self.c_pledge_mastery}, min_level={self.min_level}, max_level={self.max_level}, job_main={self.job_main}, job_dual={self.job_dual}, job_sub={self.job_sub}, pre_mission_id={self.pre_mission_id}, start_date={self.start_date}, start_time={self.start_time}, end_date={self.end_date}, end_time={self.end_time}, activate_time={self.activate_time}, deactivate_time={self.deactivate_time}, unknown_bytes={self.unknown_bytes}, available_day={self.available_day}, goal_desc={self.goal_desc}, goal_count={self.goal_count}, reward_pledge_name_value={self.reward_pledge_name_value}, reward_pvp_point={self.reward_pvp_point}, reward_items={self.reward_items})"



class PledgeShopProduct(object):

    def __init__(self, shop_index, product_id, ServerId, ShopType, product_name, product_item, buy_item, limit_lv, pledge_limit_lv, buy_limit, product_desc):
        self.shop_index = shop_index
        self.product_id = product_id
        self.ServerId = ServerId
        self.ShopType = ShopType
        self.product_name = product_name
        self.product_item = product_item
        self.buy_item = buy_item
        self.limit_lv = limit_lv
        self.pledge_limit_lv = pledge_limit_lv
        self.buy_limit = buy_limit
        self.product_desc = product_desc

    @classmethod
    def from_string(self, line) -> 'PledgeShopProduct':
        split_params = line.split('\t')[1:-1]
        attributes = ['shop_index', 'product_id', 'ServerId', 'ShopType', 'product_name', 'product_item', 'buy_item', 'limit_lv', 'pledge_limit_lv', 'buy_limit', 'product_desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('shop_index'), data.get('product_id'), data.get('ServerId'), data.get('ShopType'), data.get('product_name'), data.get('product_item'), data.get('buy_item'), data.get('limit_lv'), data.get('pledge_limit_lv'), data.get('buy_limit'), data.get('product_desc'))
    
    def __str__(self):
        return f"PledgeShopProduct(shop_index={self.shop_index}, product_id={self.product_id}, ServerId={self.ServerId}, ShopType={self.ShopType}, product_name={self.product_name}, product_item={self.product_item}, buy_item={self.buy_item}, limit_lv={self.limit_lv}, pledge_limit_lv={self.pledge_limit_lv}, buy_limit={self.buy_limit}, product_desc={self.product_desc})"



class PopupEvent(object):

    def __init__(self, id, teleport_id, type, title_stringid, field_stringid, desc_stringid, popup_texture, hud_texture, hud_over_texture, hud_push_texture):
        self.id = id
        self.teleport_id = teleport_id
        self.type = type
        self.title_stringid = title_stringid
        self.field_stringid = field_stringid
        self.desc_stringid = desc_stringid
        self.popup_texture = popup_texture
        self.hud_texture = hud_texture
        self.hud_over_texture = hud_over_texture
        self.hud_push_texture = hud_push_texture

    @classmethod
    def from_string(self, line) -> 'PopupEvent':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'teleport_id', 'type', 'title_stringid', 'field_stringid', 'desc_stringid', 'popup_texture', 'hud_texture', 'hud_over_texture', 'hud_push_texture']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('teleport_id'), data.get('type'), data.get('title_stringid'), data.get('field_stringid'), data.get('desc_stringid'), data.get('popup_texture'), data.get('hud_texture'), data.get('hud_over_texture'), data.get('hud_push_texture'))
    
    def __str__(self):
        return f"PopupEvent(id={self.id}, teleport_id={self.teleport_id}, type={self.type}, title_stringid={self.title_stringid}, field_stringid={self.field_stringid}, desc_stringid={self.desc_stringid}, popup_texture={self.popup_texture}, hud_texture={self.hud_texture}, hud_over_texture={self.hud_over_texture}, hud_push_texture={self.hud_push_texture})"



class PostEffectData(object):

    def __init__(self, effect_id, effect_name, effect_sort, effect_play_type, play_time, effect_fix, effect_cor1_factor1, effect_cor1_factor2, effect_cor1_factor3, effect_cor2_factor1, effect_cor2_factor2, effect_cor2_factor3, effect_reservefactor1, effect_reservefactor2, effect_colorgrading1, effect_colorgrading2):
        self.effect_id = effect_id
        self.effect_name = effect_name
        self.effect_sort = effect_sort
        self.effect_play_type = effect_play_type
        self.play_time = play_time
        self.effect_fix = effect_fix
        self.effect_cor1_factor1 = effect_cor1_factor1
        self.effect_cor1_factor2 = effect_cor1_factor2
        self.effect_cor1_factor3 = effect_cor1_factor3
        self.effect_cor2_factor1 = effect_cor2_factor1
        self.effect_cor2_factor2 = effect_cor2_factor2
        self.effect_cor2_factor3 = effect_cor2_factor3
        self.effect_reservefactor1 = effect_reservefactor1
        self.effect_reservefactor2 = effect_reservefactor2
        self.effect_colorgrading1 = effect_colorgrading1
        self.effect_colorgrading2 = effect_colorgrading2

    @classmethod
    def from_string(self, line) -> 'PostEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['effect_id', 'effect_name', 'effect_sort', 'effect_play_type', 'play_time', 'effect_fix', 'effect_cor1_factor1', 'effect_cor1_factor2', 'effect_cor1_factor3', 'effect_cor2_factor1', 'effect_cor2_factor2', 'effect_cor2_factor3', 'effect_reservefactor1', 'effect_reservefactor2', 'effect_colorgrading1', 'effect_colorgrading2']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('effect_id'), data.get('effect_name'), data.get('effect_sort'), data.get('effect_play_type'), data.get('play_time'), data.get('effect_fix'), data.get('effect_cor1_factor1'), data.get('effect_cor1_factor2'), data.get('effect_cor1_factor3'), data.get('effect_cor2_factor1'), data.get('effect_cor2_factor2'), data.get('effect_cor2_factor3'), data.get('effect_reservefactor1'), data.get('effect_reservefactor2'), data.get('effect_colorgrading1'), data.get('effect_colorgrading2'))
    
    def __str__(self):
        return f"PostEffectData(effect_id={self.effect_id}, effect_name={self.effect_name}, effect_sort={self.effect_sort}, effect_play_type={self.effect_play_type}, play_time={self.play_time}, effect_fix={self.effect_fix}, effect_cor1_factor1={self.effect_cor1_factor1}, effect_cor1_factor2={self.effect_cor1_factor2}, effect_cor1_factor3={self.effect_cor1_factor3}, effect_cor2_factor1={self.effect_cor2_factor1}, effect_cor2_factor2={self.effect_cor2_factor2}, effect_cor2_factor3={self.effect_cor2_factor3}, effect_reservefactor1={self.effect_reservefactor1}, effect_reservefactor2={self.effect_reservefactor2}, effect_colorgrading1={self.effect_colorgrading1}, effect_colorgrading2={self.effect_colorgrading2})"



class PrisonData(object):

    def __init__(self, prison_type, pk_count_cond, donation, need_item, holding_minute):
        self.prison_type = prison_type
        self.pk_count_cond = pk_count_cond
        self.donation = donation
        self.need_item = need_item
        self.holding_minute = holding_minute

    @classmethod
    def from_string(self, line) -> 'PrisonData':
        split_params = line.split('\t')[1:-1]
        attributes = ['prison_type', 'pk_count_cond', 'donation', 'need_item', 'holding_minute']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('prison_type'), data.get('pk_count_cond'), data.get('donation'), data.get('need_item'), data.get('holding_minute'))
    
    def __str__(self):
        return f"PrisonData(prison_type={self.prison_type}, pk_count_cond={self.pk_count_cond}, donation={self.donation}, need_item={self.need_item}, holding_minute={self.holding_minute})"



class ProductName(object):

    def __init__(self, id, outer_name, description, icon, icon_panel, mainsubject):
        self.id = id
        self.outer_name = outer_name
        self.description = description
        self.icon = icon
        self.icon_panel = icon_panel
        self.mainsubject = mainsubject

    @classmethod
    def from_string(self, line) -> 'ProductName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'outer_name', 'description', 'icon', 'icon_panel', 'mainsubject']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('outer_name'), data.get('description'), data.get('icon'), data.get('icon_panel'), data.get('mainsubject'))
    
    def __str__(self):
        return f"ProductName(id={self.id}, outer_name={self.outer_name}, description={self.description}, icon={self.icon}, icon_panel={self.icon_panel}, mainsubject={self.mainsubject})"



class ProductName(object):

    def __init__(self, id, outer_name, description, icon, icon_panel, mainsubject):
        self.id = id
        self.outer_name = outer_name
        self.description = description
        self.icon = icon
        self.icon_panel = icon_panel
        self.mainsubject = mainsubject

    @classmethod
    def from_string(self, line) -> 'ProductName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'outer_name', 'description', 'icon', 'icon_panel', 'mainsubject']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('outer_name'), data.get('description'), data.get('icon'), data.get('icon_panel'), data.get('mainsubject'))
    
    def __str__(self):
        return f"ProductName(id={self.id}, outer_name={self.outer_name}, description={self.description}, icon={self.icon}, icon_panel={self.icon_panel}, mainsubject={self.mainsubject})"



class PurchaseLimitCraft(object):

    def __init__(self, shop_index, product_id, ServerId, ShopType, category, category_sub, MarkType, MaxBuyCount, product_name, product_item, product_enchant, buy_item, limit_lv, buy_limit, RequirementBuySkills, KeepOptionFee, KeepOption, automatic_type):
        self.shop_index = shop_index
        self.product_id = product_id
        self.ServerId = ServerId
        self.ShopType = ShopType
        self.category = category
        self.category_sub = category_sub
        self.MarkType = MarkType
        self.MaxBuyCount = MaxBuyCount
        self.product_name = product_name
        self.product_item = product_item
        self.product_enchant = product_enchant
        self.buy_item = buy_item
        self.limit_lv = limit_lv
        self.buy_limit = buy_limit
        self.RequirementBuySkills = RequirementBuySkills
        self.KeepOptionFee = KeepOptionFee
        self.KeepOption = KeepOption
        self.automatic_type = automatic_type

    @classmethod
    def from_string(self, line) -> 'PurchaseLimitCraft':
        split_params = line.split('\t')[1:-1]
        attributes = ['shop_index', 'product_id', 'ServerId', 'ShopType', 'category', 'category_sub', 'MarkType', 'MaxBuyCount', 'product_name', 'product_item', 'product_enchant', 'buy_item', 'limit_lv', 'buy_limit', 'RequirementBuySkills', 'KeepOptionFee', 'KeepOption', 'automatic_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('shop_index'), data.get('product_id'), data.get('ServerId'), data.get('ShopType'), data.get('category'), data.get('category_sub'), data.get('MarkType'), data.get('MaxBuyCount'), data.get('product_name'), data.get('product_item'), data.get('product_enchant'), data.get('buy_item'), data.get('limit_lv'), data.get('buy_limit'), data.get('RequirementBuySkills'), data.get('KeepOptionFee'), data.get('KeepOption'), data.get('automatic_type'))
    
    def __str__(self):
        return f"PurchaseLimitCraft(shop_index={self.shop_index}, product_id={self.product_id}, ServerId={self.ServerId}, ShopType={self.ShopType}, category={self.category}, category_sub={self.category_sub}, MarkType={self.MarkType}, MaxBuyCount={self.MaxBuyCount}, product_name={self.product_name}, product_item={self.product_item}, product_enchant={self.product_enchant}, buy_item={self.buy_item}, limit_lv={self.limit_lv}, buy_limit={self.buy_limit}, RequirementBuySkills={self.RequirementBuySkills}, KeepOptionFee={self.KeepOptionFee}, KeepOption={self.KeepOption}, automatic_type={self.automatic_type})"



class PurchaseLimitCraftCategory(object):

    def __init__(self, category_id, string_id, string_color, ribbon_texture, optional, show_server):
        self.category_id = category_id
        self.string_id = string_id
        self.string_color = string_color
        self.ribbon_texture = ribbon_texture
        self.optional = optional
        self.show_server = show_server

    @classmethod
    def from_string(self, line) -> 'PurchaseLimitCraftCategory':
        split_params = line.split('\t')[1:-1]
        attributes = ['category_id', 'string_id', 'string_color', 'ribbon_texture', 'optional', 'show_server']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('category_id'), data.get('string_id'), data.get('string_color'), data.get('ribbon_texture'), data.get('optional'), data.get('show_server'))
    
    def __str__(self):
        return f"PurchaseLimitCraftCategory(category_id={self.category_id}, string_id={self.string_id}, string_color={self.string_color}, ribbon_texture={self.ribbon_texture}, optional={self.optional}, show_server={self.show_server})"



class PurchaseLimitCraft(object):

    def __init__(self, shop_index, product_id, ServerId, ShopType, category, category_sub, MarkType, MaxBuyCount, product_name, product_item, product_enchant, buy_item, limit_lv, buy_limit, RequirementBuySkills, KeepOptionFee, KeepOption, automatic_type):
        self.shop_index = shop_index
        self.product_id = product_id
        self.ServerId = ServerId
        self.ShopType = ShopType
        self.category = category
        self.category_sub = category_sub
        self.MarkType = MarkType
        self.MaxBuyCount = MaxBuyCount
        self.product_name = product_name
        self.product_item = product_item
        self.product_enchant = product_enchant
        self.buy_item = buy_item
        self.limit_lv = limit_lv
        self.buy_limit = buy_limit
        self.RequirementBuySkills = RequirementBuySkills
        self.KeepOptionFee = KeepOptionFee
        self.KeepOption = KeepOption
        self.automatic_type = automatic_type

    @classmethod
    def from_string(self, line) -> 'PurchaseLimitCraft':
        split_params = line.split('\t')[1:-1]
        attributes = ['shop_index', 'product_id', 'ServerId', 'ShopType', 'category', 'category_sub', 'MarkType', 'MaxBuyCount', 'product_name', 'product_item', 'product_enchant', 'buy_item', 'limit_lv', 'buy_limit', 'RequirementBuySkills', 'KeepOptionFee', 'KeepOption', 'automatic_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('shop_index'), data.get('product_id'), data.get('ServerId'), data.get('ShopType'), data.get('category'), data.get('category_sub'), data.get('MarkType'), data.get('MaxBuyCount'), data.get('product_name'), data.get('product_item'), data.get('product_enchant'), data.get('buy_item'), data.get('limit_lv'), data.get('buy_limit'), data.get('RequirementBuySkills'), data.get('KeepOptionFee'), data.get('KeepOption'), data.get('automatic_type'))
    
    def __str__(self):
        return f"PurchaseLimitCraft(shop_index={self.shop_index}, product_id={self.product_id}, ServerId={self.ServerId}, ShopType={self.ShopType}, category={self.category}, category_sub={self.category_sub}, MarkType={self.MarkType}, MaxBuyCount={self.MaxBuyCount}, product_name={self.product_name}, product_item={self.product_item}, product_enchant={self.product_enchant}, buy_item={self.buy_item}, limit_lv={self.limit_lv}, buy_limit={self.buy_limit}, RequirementBuySkills={self.RequirementBuySkills}, KeepOptionFee={self.KeepOptionFee}, KeepOption={self.KeepOption}, automatic_type={self.automatic_type})"



class PvpbookRequiredItem(object):

    def __init__(self, type, item_id, item_amount):
        self.type = type
        self.item_id = item_id
        self.item_amount = item_amount

    @classmethod
    def from_string(self, line) -> 'PvpbookRequiredItem':
        split_params = line.split('\t')[1:-1]
        attributes = ['type', 'item_id', 'item_amount']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('type'), data.get('item_id'), data.get('item_amount'))
    
    def __str__(self):
        return f"PvpbookRequiredItem(type={self.type}, item_id={self.item_id}, item_amount={self.item_amount})"



class QuestMarkConditionData(object):

    def __init__(self, quest_id, npc_id, race_filter, class_filter, start_npc_loc):
        self.quest_id = quest_id
        self.npc_id = npc_id
        self.race_filter = race_filter
        self.class_filter = class_filter
        self.start_npc_loc = start_npc_loc

    @classmethod
    def from_string(self, line) -> 'QuestMarkConditionData':
        split_params = line.split('\t')[1:-1]
        attributes = ['quest_id', 'npc_id', 'race_filter', 'class_filter', 'start_npc_loc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('quest_id'), data.get('npc_id'), data.get('race_filter'), data.get('class_filter'), data.get('start_npc_loc'))
    
    def __str__(self):
        return f"QuestMarkConditionData(quest_id={self.quest_id}, npc_id={self.npc_id}, race_filter={self.race_filter}, class_filter={self.class_filter}, start_npc_loc={self.start_npc_loc})"



class QuestName(object):

    def __init__(self, tag, id, level, title, sub_name, desc, goal_id, goal_type, goal_num, target_loc, add_target_locs, q_level, lvl_min, lvl_max, quest_type, entity_name, get_item_in_quest, UNK_1, UNK_2, start_npc_id, start_npc_loc, q_requirement, quest_intro, class_limit, have_item, clan_pet_quest, cleared_quest, mark_type, category_id, priority_level, search_zoneid, iscategory, reward_id, reward_num, pre_level, faction_id, faction_level):
        self.tag = tag
        self.id = id
        self.level = level
        self.title = title
        self.sub_name = sub_name
        self.desc = desc
        self.goal_id = goal_id
        self.goal_type = goal_type
        self.goal_num = goal_num
        self.target_loc = target_loc
        self.add_target_locs = add_target_locs
        self.q_level = q_level
        self.lvl_min = lvl_min
        self.lvl_max = lvl_max
        self.quest_type = quest_type
        self.entity_name = entity_name
        self.get_item_in_quest = get_item_in_quest
        self.UNK_1 = UNK_1
        self.UNK_2 = UNK_2
        self.start_npc_id = start_npc_id
        self.start_npc_loc = start_npc_loc
        self.q_requirement = q_requirement
        self.quest_intro = quest_intro
        self.class_limit = class_limit
        self.have_item = have_item
        self.clan_pet_quest = clan_pet_quest
        self.cleared_quest = cleared_quest
        self.mark_type = mark_type
        self.category_id = category_id
        self.priority_level = priority_level
        self.search_zoneid = search_zoneid
        self.iscategory = iscategory
        self.reward_id = reward_id
        self.reward_num = reward_num
        self.pre_level = pre_level
        self.faction_id = faction_id
        self.faction_level = faction_level

    @classmethod
    def from_string(self, line) -> 'QuestName':
        split_params = line.split('\t')[1:-1]
        attributes = ['tag', 'id', 'level', 'title', 'sub_name', 'desc', 'goal_id', 'goal_type', 'goal_num', 'target_loc', 'add_target_locs', 'q_level', 'lvl_min', 'lvl_max', 'quest_type', 'entity_name', 'get_item_in_quest', 'UNK_1', 'UNK_2', 'start_npc_id', 'start_npc_loc', 'q_requirement', 'quest_intro', 'class_limit', 'have_item', 'clan_pet_quest', 'cleared_quest', 'mark_type', 'category_id', 'priority_level', 'search_zoneid', 'iscategory', 'reward_id', 'reward_num', 'pre_level', 'faction_id', 'faction_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('tag'), data.get('id'), data.get('level'), data.get('title'), data.get('sub_name'), data.get('desc'), data.get('goal_id'), data.get('goal_type'), data.get('goal_num'), data.get('target_loc'), data.get('add_target_locs'), data.get('q_level'), data.get('lvl_min'), data.get('lvl_max'), data.get('quest_type'), data.get('entity_name'), data.get('get_item_in_quest'), data.get('UNK_1'), data.get('UNK_2'), data.get('start_npc_id'), data.get('start_npc_loc'), data.get('q_requirement'), data.get('quest_intro'), data.get('class_limit'), data.get('have_item'), data.get('clan_pet_quest'), data.get('cleared_quest'), data.get('mark_type'), data.get('category_id'), data.get('priority_level'), data.get('search_zoneid'), data.get('iscategory'), data.get('reward_id'), data.get('reward_num'), data.get('pre_level'), data.get('faction_id'), data.get('faction_level'))
    
    def __str__(self):
        return f"QuestName(tag={self.tag}, id={self.id}, level={self.level}, title={self.title}, sub_name={self.sub_name}, desc={self.desc}, goal_id={self.goal_id}, goal_type={self.goal_type}, goal_num={self.goal_num}, target_loc={self.target_loc}, add_target_locs={self.add_target_locs}, q_level={self.q_level}, lvl_min={self.lvl_min}, lvl_max={self.lvl_max}, quest_type={self.quest_type}, entity_name={self.entity_name}, get_item_in_quest={self.get_item_in_quest}, UNK_1={self.UNK_1}, UNK_2={self.UNK_2}, start_npc_id={self.start_npc_id}, start_npc_loc={self.start_npc_loc}, q_requirement={self.q_requirement}, quest_intro={self.quest_intro}, class_limit={self.class_limit}, have_item={self.have_item}, clan_pet_quest={self.clan_pet_quest}, cleared_quest={self.cleared_quest}, mark_type={self.mark_type}, category_id={self.category_id}, priority_level={self.priority_level}, search_zoneid={self.search_zoneid}, iscategory={self.iscategory}, reward_id={self.reward_id}, reward_num={self.reward_num}, pre_level={self.pre_level}, faction_id={self.faction_id}, faction_level={self.faction_level})"



class QuestName(object):

    def __init__(self, tag, id, level, title, sub_name, desc, goal_id, goal_type, goal_num, target_loc, add_target_locs, q_level, lvl_min, lvl_max, quest_type, entity_name, get_item_in_quest, UNK_1, UNK_2, start_npc_id, start_npc_loc, q_requirement, quest_intro, class_limit, have_item, clan_pet_quest, cleared_quest, mark_type, category_id, priority_level, search_zoneid, iscategory, reward_id, reward_num, pre_level, faction_id, faction_level):
        self.tag = tag
        self.id = id
        self.level = level
        self.title = title
        self.sub_name = sub_name
        self.desc = desc
        self.goal_id = goal_id
        self.goal_type = goal_type
        self.goal_num = goal_num
        self.target_loc = target_loc
        self.add_target_locs = add_target_locs
        self.q_level = q_level
        self.lvl_min = lvl_min
        self.lvl_max = lvl_max
        self.quest_type = quest_type
        self.entity_name = entity_name
        self.get_item_in_quest = get_item_in_quest
        self.UNK_1 = UNK_1
        self.UNK_2 = UNK_2
        self.start_npc_id = start_npc_id
        self.start_npc_loc = start_npc_loc
        self.q_requirement = q_requirement
        self.quest_intro = quest_intro
        self.class_limit = class_limit
        self.have_item = have_item
        self.clan_pet_quest = clan_pet_quest
        self.cleared_quest = cleared_quest
        self.mark_type = mark_type
        self.category_id = category_id
        self.priority_level = priority_level
        self.search_zoneid = search_zoneid
        self.iscategory = iscategory
        self.reward_id = reward_id
        self.reward_num = reward_num
        self.pre_level = pre_level
        self.faction_id = faction_id
        self.faction_level = faction_level

    @classmethod
    def from_string(self, line) -> 'QuestName':
        split_params = line.split('\t')[1:-1]
        attributes = ['tag', 'id', 'level', 'title', 'sub_name', 'desc', 'goal_id', 'goal_type', 'goal_num', 'target_loc', 'add_target_locs', 'q_level', 'lvl_min', 'lvl_max', 'quest_type', 'entity_name', 'get_item_in_quest', 'UNK_1', 'UNK_2', 'start_npc_id', 'start_npc_loc', 'q_requirement', 'quest_intro', 'class_limit', 'have_item', 'clan_pet_quest', 'cleared_quest', 'mark_type', 'category_id', 'priority_level', 'search_zoneid', 'iscategory', 'reward_id', 'reward_num', 'pre_level', 'faction_id', 'faction_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('tag'), data.get('id'), data.get('level'), data.get('title'), data.get('sub_name'), data.get('desc'), data.get('goal_id'), data.get('goal_type'), data.get('goal_num'), data.get('target_loc'), data.get('add_target_locs'), data.get('q_level'), data.get('lvl_min'), data.get('lvl_max'), data.get('quest_type'), data.get('entity_name'), data.get('get_item_in_quest'), data.get('UNK_1'), data.get('UNK_2'), data.get('start_npc_id'), data.get('start_npc_loc'), data.get('q_requirement'), data.get('quest_intro'), data.get('class_limit'), data.get('have_item'), data.get('clan_pet_quest'), data.get('cleared_quest'), data.get('mark_type'), data.get('category_id'), data.get('priority_level'), data.get('search_zoneid'), data.get('iscategory'), data.get('reward_id'), data.get('reward_num'), data.get('pre_level'), data.get('faction_id'), data.get('faction_level'))
    
    def __str__(self):
        return f"QuestName(tag={self.tag}, id={self.id}, level={self.level}, title={self.title}, sub_name={self.sub_name}, desc={self.desc}, goal_id={self.goal_id}, goal_type={self.goal_type}, goal_num={self.goal_num}, target_loc={self.target_loc}, add_target_locs={self.add_target_locs}, q_level={self.q_level}, lvl_min={self.lvl_min}, lvl_max={self.lvl_max}, quest_type={self.quest_type}, entity_name={self.entity_name}, get_item_in_quest={self.get_item_in_quest}, UNK_1={self.UNK_1}, UNK_2={self.UNK_2}, start_npc_id={self.start_npc_id}, start_npc_loc={self.start_npc_loc}, q_requirement={self.q_requirement}, quest_intro={self.quest_intro}, class_limit={self.class_limit}, have_item={self.have_item}, clan_pet_quest={self.clan_pet_quest}, cleared_quest={self.cleared_quest}, mark_type={self.mark_type}, category_id={self.category_id}, priority_level={self.priority_level}, search_zoneid={self.search_zoneid}, iscategory={self.iscategory}, reward_id={self.reward_id}, reward_num={self.reward_num}, pre_level={self.pre_level}, faction_id={self.faction_id}, faction_level={self.faction_level})"



class RaidData(object):

    def __init__(self, id, raid_id, raid_lvl, search_zoneid, loc, desc, raid_ppl, respawn_type, view_item, respawn_time, rc_level, teleport_loc, use_teleport_loc):
        self.id = id
        self.raid_id = raid_id
        self.raid_lvl = raid_lvl
        self.search_zoneid = search_zoneid
        self.loc = loc
        self.desc = desc
        self.raid_ppl = raid_ppl
        self.respawn_type = respawn_type
        self.view_item = view_item
        self.respawn_time = respawn_time
        self.rc_level = rc_level
        self.teleport_loc = teleport_loc
        self.use_teleport_loc = use_teleport_loc

    @classmethod
    def from_string(self, line) -> 'RaidData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'raid_id', 'raid_lvl', 'search_zoneid', 'loc', 'desc', 'raid_ppl', 'respawn_type', 'view_item', 'respawn_time', 'rc_level', 'teleport_loc', 'use_teleport_loc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('raid_id'), data.get('raid_lvl'), data.get('search_zoneid'), data.get('loc'), data.get('desc'), data.get('raid_ppl'), data.get('respawn_type'), data.get('view_item'), data.get('respawn_time'), data.get('rc_level'), data.get('teleport_loc'), data.get('use_teleport_loc'))
    
    def __str__(self):
        return f"RaidData(id={self.id}, raid_id={self.raid_id}, raid_lvl={self.raid_lvl}, search_zoneid={self.search_zoneid}, loc={self.loc}, desc={self.desc}, raid_ppl={self.raid_ppl}, respawn_type={self.respawn_type}, view_item={self.view_item}, respawn_time={self.respawn_time}, rc_level={self.rc_level}, teleport_loc={self.teleport_loc}, use_teleport_loc={self.use_teleport_loc})"



class RankingSystemData(object):

    def __init__(self, id, type, grouptype, grade, gradescope, rewardskillID):
        self.id = id
        self.type = type
        self.grouptype = grouptype
        self.grade = grade
        self.gradescope = gradescope
        self.rewardskillID = rewardskillID

    @classmethod
    def from_string(self, line) -> 'RankingSystemData':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'grouptype', 'grade', 'gradescope', 'rewardskillID']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('grouptype'), data.get('grade'), data.get('gradescope'), data.get('rewardskillID'))
    
    def __str__(self):
        return f"RankingSystemData(id={self.id}, type={self.type}, grouptype={self.grouptype}, grade={self.grade}, gradescope={self.gradescope}, rewardskillID={self.rewardskillID})"



class RankingInzonedata(object):

    def __init__(self, ranking_id, inzone_id, enter_type, check_type, reward_type, reward_view):
        self.ranking_id = ranking_id
        self.inzone_id = inzone_id
        self.enter_type = enter_type
        self.check_type = check_type
        self.reward_type = reward_type
        self.reward_view = reward_view

    @classmethod
    def from_string(self, line) -> 'RankingInzonedata':
        split_params = line.split('\t')[1:-1]
        attributes = ['ranking_id', 'inzone_id', 'enter_type', 'check_type', 'reward_type', 'reward_view']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ranking_id'), data.get('inzone_id'), data.get('enter_type'), data.get('check_type'), data.get('reward_type'), data.get('reward_view'))
    
    def __str__(self):
        return f"RankingInzonedata(ranking_id={self.ranking_id}, inzone_id={self.inzone_id}, enter_type={self.enter_type}, check_type={self.check_type}, reward_type={self.reward_type}, reward_view={self.reward_view})"



class Recipe(object):

    def __init__(self, name, id, recipe_id, level, product_id, product_num, is_showtree, is_multiple_product, mp_consume, success_rate, material):
        self.name = name
        self.id = id
        self.recipe_id = recipe_id
        self.level = level
        self.product_id = product_id
        self.product_num = product_num
        self.is_showtree = is_showtree
        self.is_multiple_product = is_multiple_product
        self.mp_consume = mp_consume
        self.success_rate = success_rate
        self.material = material

    @classmethod
    def from_string(self, line) -> 'Recipe':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'id', 'recipe_id', 'level', 'product_id', 'product_num', 'is_showtree', 'is_multiple_product', 'mp_consume', 'success_rate', 'material']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('id'), data.get('recipe_id'), data.get('level'), data.get('product_id'), data.get('product_num'), data.get('is_showtree'), data.get('is_multiple_product'), data.get('mp_consume'), data.get('success_rate'), data.get('material'))
    
    def __str__(self):
        return f"Recipe(name={self.name}, id={self.id}, recipe_id={self.recipe_id}, level={self.level}, product_id={self.product_id}, product_num={self.product_num}, is_showtree={self.is_showtree}, is_multiple_product={self.is_multiple_product}, mp_consume={self.mp_consume}, success_rate={self.success_rate}, material={self.material})"



class RecoveryCoupon(object):

    def __init__(self, item_id, categories, title_sysstring_id, default_multisellId, extra_multisell_id, extra_multisell_servers):
        self.item_id = item_id
        self.categories = categories
        self.title_sysstring_id = title_sysstring_id
        self.default_multisellId = default_multisellId
        self.extra_multisell_id = extra_multisell_id
        self.extra_multisell_servers = extra_multisell_servers

    @classmethod
    def from_string(self, line) -> 'RecoveryCoupon':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'categories', 'title_sysstring_id', 'default_multisellId', 'extra_multisell_id', 'extra_multisell_servers']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('categories'), data.get('title_sysstring_id'), data.get('default_multisellId'), data.get('extra_multisell_id'), data.get('extra_multisell_servers'))
    
    def __str__(self):
        return f"RecoveryCoupon(item_id={self.item_id}, categories={self.categories}, title_sysstring_id={self.title_sysstring_id}, default_multisellId={self.default_multisellId}, extra_multisell_id={self.extra_multisell_id}, extra_multisell_servers={self.extra_multisell_servers})"



class Relics(object):

    def __init__(self, relics_collection_id, category, relics_collection_name, option_id, unk, option_filter, need_relics):
        self.relics_collection_id = relics_collection_id
        self.category = category
        self.relics_collection_name = relics_collection_name
        self.option_id = option_id
        self.unk = unk
        self.option_filter = option_filter
        self.need_relics = need_relics

    @classmethod
    def from_string(self, line) -> 'Relics':
        split_params = line.split('\t')[1:-1]
        attributes = ['relics_collection_id', 'category', 'relics_collection_name', 'option_id', 'unk', 'option_filter', 'need_relics']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('relics_collection_id'), data.get('category'), data.get('relics_collection_name'), data.get('option_id'), data.get('unk'), data.get('option_filter'), data.get('need_relics'))
    
    def __str__(self):
        return f"Relics(relics_collection_id={self.relics_collection_id}, category={self.category}, relics_collection_name={self.relics_collection_name}, option_id={self.option_id}, unk={self.unk}, option_filter={self.option_filter}, need_relics={self.need_relics})"



class RelicsCollection(object):

    def __init__(self, relics_collection_id, category, relics_collection_name, option_id, unk, option_filter, need_relics):
        self.relics_collection_id = relics_collection_id
        self.category = category
        self.relics_collection_name = relics_collection_name
        self.option_id = option_id
        self.unk = unk
        self.option_filter = option_filter
        self.need_relics = need_relics

    @classmethod
    def from_string(self, line) -> 'RelicsCollection':
        split_params = line.split('\t')[1:-1]
        attributes = ['relics_collection_id', 'category', 'relics_collection_name', 'option_id', 'unk', 'option_filter', 'need_relics']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('relics_collection_id'), data.get('category'), data.get('relics_collection_name'), data.get('option_id'), data.get('unk'), data.get('option_filter'), data.get('need_relics'))
    
    def __str__(self):
        return f"RelicsCollection(relics_collection_id={self.relics_collection_id}, category={self.category}, relics_collection_name={self.relics_collection_name}, option_id={self.option_id}, unk={self.unk}, option_filter={self.option_filter}, need_relics={self.need_relics})"



class RelicsMain(object):

    def __init__(self, relics_id, item_id, grade, skill_id, enchanted, npc_id, npc_level, sort_order):
        self.relics_id = relics_id
        self.item_id = item_id
        self.grade = grade
        self.skill_id = skill_id
        self.enchanted = enchanted
        self.npc_id = npc_id
        self.npc_level = npc_level
        self.sort_order = sort_order

    @classmethod
    def from_string(self, line) -> 'RelicsMain':
        split_params = line.split('\t')[1:-1]
        attributes = ['relics_id', 'item_id', 'grade', 'skill_id', 'enchanted', 'npc_id', 'npc_level', 'sort_order']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('relics_id'), data.get('item_id'), data.get('grade'), data.get('skill_id'), data.get('enchanted'), data.get('npc_id'), data.get('npc_level'), data.get('sort_order'))
    
    def __str__(self):
        return f"RelicsMain(relics_id={self.relics_id}, item_id={self.item_id}, grade={self.grade}, skill_id={self.skill_id}, enchanted={self.enchanted}, npc_id={self.npc_id}, npc_level={self.npc_level}, sort_order={self.sort_order})"



class RelicsPlaydata(object):

    def __init__(self, relics_id, grade, fail_item, cost_item, upgrade_probs):
        self.relics_id = relics_id
        self.grade = grade
        self.fail_item = fail_item
        self.cost_item = cost_item
        self.upgrade_probs = upgrade_probs

    @classmethod
    def from_string(self, line) -> 'RelicsPlaydata':
        split_params = line.split('\t')[1:-1]
        attributes = ['relics_id', 'grade', 'fail_item', 'cost_item', 'upgrade_probs']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('relics_id'), data.get('grade'), data.get('fail_item'), data.get('cost_item'), data.get('upgrade_probs'))
    
    def __str__(self):
        return f"RelicsPlaydata(relics_id={self.relics_id}, grade={self.grade}, fail_item={self.fail_item}, cost_item={self.cost_item}, upgrade_probs={self.upgrade_probs})"



class ReplaceSkillIcon(object):

    def __init__(self, abnormal_status, abnormal_status_level, abnormal_status_sublevel, original_skill_id, replace_skill_id, replace_lv, unk_414_skill_id):
        self.abnormal_status = abnormal_status
        self.abnormal_status_level = abnormal_status_level
        self.abnormal_status_sublevel = abnormal_status_sublevel
        self.original_skill_id = original_skill_id
        self.replace_skill_id = replace_skill_id
        self.replace_lv = replace_lv
        self.unk_414_skill_id = unk_414_skill_id

    @classmethod
    def from_string(self, line) -> 'ReplaceSkillIcon':
        split_params = line.split('\t')[1:-1]
        attributes = ['abnormal_status', 'abnormal_status_level', 'abnormal_status_sublevel', 'original_skill_id', 'replace_skill_id', 'replace_lv', 'unk_414_skill_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('abnormal_status'), data.get('abnormal_status_level'), data.get('abnormal_status_sublevel'), data.get('original_skill_id'), data.get('replace_skill_id'), data.get('replace_lv'), data.get('unk_414_skill_id'))
    
    def __str__(self):
        return f"ReplaceSkillIcon(abnormal_status={self.abnormal_status}, abnormal_status_level={self.abnormal_status_level}, abnormal_status_sublevel={self.abnormal_status_sublevel}, original_skill_id={self.original_skill_id}, replace_skill_id={self.replace_skill_id}, replace_lv={self.replace_lv}, unk_414_skill_id={self.unk_414_skill_id})"



class RideData(object):

    def __init__(self, ride_type, ride_npc_id, attach_bone_name, mfighter_loc, ffighter_loc, mmagic_loc, fmagic_loc, melf_loc, felf_loc, mdarkelf_loc, fdarkelf_loc, mdwarf_loc, fdwarf_loc, morc_loc, forc_loc, mshaman_loc, fshaman_loc, mkamael_loc, fkamael_loc, mertheia_loc, fertheia_loc, msylph_loc, fsylph_loc, mHighElf_loc, fHighElf_loc, empty_loc, mfighter_rot, ffighter_rot, mmagic_rot, fmagic_rot, melf_rot, felf_rot, mdarkelf_rot, fdarkelf_rot, mdwarf_rot, fdwarf_rot, morc_rot, forc_rot, mshaman_rot, fshaman_rot, mkamael_rot, fkamael_rot, mertheia_rot, fertheia_rot, msylph_rot, fsylph_rot, mHighElf_rot, fHighElf_rot, empty_rot, nameoffset):
        self.ride_type = ride_type
        self.ride_npc_id = ride_npc_id
        self.attach_bone_name = attach_bone_name
        self.mfighter_loc = mfighter_loc
        self.ffighter_loc = ffighter_loc
        self.mmagic_loc = mmagic_loc
        self.fmagic_loc = fmagic_loc
        self.melf_loc = melf_loc
        self.felf_loc = felf_loc
        self.mdarkelf_loc = mdarkelf_loc
        self.fdarkelf_loc = fdarkelf_loc
        self.mdwarf_loc = mdwarf_loc
        self.fdwarf_loc = fdwarf_loc
        self.morc_loc = morc_loc
        self.forc_loc = forc_loc
        self.mshaman_loc = mshaman_loc
        self.fshaman_loc = fshaman_loc
        self.mkamael_loc = mkamael_loc
        self.fkamael_loc = fkamael_loc
        self.mertheia_loc = mertheia_loc
        self.fertheia_loc = fertheia_loc
        self.msylph_loc = msylph_loc
        self.fsylph_loc = fsylph_loc
        self.mHighElf_loc = mHighElf_loc
        self.fHighElf_loc = fHighElf_loc
        self.empty_loc = empty_loc
        self.mfighter_rot = mfighter_rot
        self.ffighter_rot = ffighter_rot
        self.mmagic_rot = mmagic_rot
        self.fmagic_rot = fmagic_rot
        self.melf_rot = melf_rot
        self.felf_rot = felf_rot
        self.mdarkelf_rot = mdarkelf_rot
        self.fdarkelf_rot = fdarkelf_rot
        self.mdwarf_rot = mdwarf_rot
        self.fdwarf_rot = fdwarf_rot
        self.morc_rot = morc_rot
        self.forc_rot = forc_rot
        self.mshaman_rot = mshaman_rot
        self.fshaman_rot = fshaman_rot
        self.mkamael_rot = mkamael_rot
        self.fkamael_rot = fkamael_rot
        self.mertheia_rot = mertheia_rot
        self.fertheia_rot = fertheia_rot
        self.msylph_rot = msylph_rot
        self.fsylph_rot = fsylph_rot
        self.mHighElf_rot = mHighElf_rot
        self.fHighElf_rot = fHighElf_rot
        self.empty_rot = empty_rot
        self.nameoffset = nameoffset

    @classmethod
    def from_string(self, line) -> 'RideData':
        split_params = line.split('\t')[1:-1]
        attributes = ['ride_type', 'ride_npc_id', 'attach_bone_name', 'mfighter_loc', 'ffighter_loc', 'mmagic_loc', 'fmagic_loc', 'melf_loc', 'felf_loc', 'mdarkelf_loc', 'fdarkelf_loc', 'mdwarf_loc', 'fdwarf_loc', 'morc_loc', 'forc_loc', 'mshaman_loc', 'fshaman_loc', 'mkamael_loc', 'fkamael_loc', 'mertheia_loc', 'fertheia_loc', 'msylph_loc', 'fsylph_loc', 'mHighElf_loc', 'fHighElf_loc', 'empty_loc', 'mfighter_rot', 'ffighter_rot', 'mmagic_rot', 'fmagic_rot', 'melf_rot', 'felf_rot', 'mdarkelf_rot', 'fdarkelf_rot', 'mdwarf_rot', 'fdwarf_rot', 'morc_rot', 'forc_rot', 'mshaman_rot', 'fshaman_rot', 'mkamael_rot', 'fkamael_rot', 'mertheia_rot', 'fertheia_rot', 'msylph_rot', 'fsylph_rot', 'mHighElf_rot', 'fHighElf_rot', 'empty_rot', 'nameoffset']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ride_type'), data.get('ride_npc_id'), data.get('attach_bone_name'), data.get('mfighter_loc'), data.get('ffighter_loc'), data.get('mmagic_loc'), data.get('fmagic_loc'), data.get('melf_loc'), data.get('felf_loc'), data.get('mdarkelf_loc'), data.get('fdarkelf_loc'), data.get('mdwarf_loc'), data.get('fdwarf_loc'), data.get('morc_loc'), data.get('forc_loc'), data.get('mshaman_loc'), data.get('fshaman_loc'), data.get('mkamael_loc'), data.get('fkamael_loc'), data.get('mertheia_loc'), data.get('fertheia_loc'), data.get('msylph_loc'), data.get('fsylph_loc'), data.get('mHighElf_loc'), data.get('fHighElf_loc'), data.get('empty_loc'), data.get('mfighter_rot'), data.get('ffighter_rot'), data.get('mmagic_rot'), data.get('fmagic_rot'), data.get('melf_rot'), data.get('felf_rot'), data.get('mdarkelf_rot'), data.get('fdarkelf_rot'), data.get('mdwarf_rot'), data.get('fdwarf_rot'), data.get('morc_rot'), data.get('forc_rot'), data.get('mshaman_rot'), data.get('fshaman_rot'), data.get('mkamael_rot'), data.get('fkamael_rot'), data.get('mertheia_rot'), data.get('fertheia_rot'), data.get('msylph_rot'), data.get('fsylph_rot'), data.get('mHighElf_rot'), data.get('fHighElf_rot'), data.get('empty_rot'), data.get('nameoffset'))
    
    def __str__(self):
        return f"RideData(ride_type={self.ride_type}, ride_npc_id={self.ride_npc_id}, attach_bone_name={self.attach_bone_name}, mfighter_loc={self.mfighter_loc}, ffighter_loc={self.ffighter_loc}, mmagic_loc={self.mmagic_loc}, fmagic_loc={self.fmagic_loc}, melf_loc={self.melf_loc}, felf_loc={self.felf_loc}, mdarkelf_loc={self.mdarkelf_loc}, fdarkelf_loc={self.fdarkelf_loc}, mdwarf_loc={self.mdwarf_loc}, fdwarf_loc={self.fdwarf_loc}, morc_loc={self.morc_loc}, forc_loc={self.forc_loc}, mshaman_loc={self.mshaman_loc}, fshaman_loc={self.fshaman_loc}, mkamael_loc={self.mkamael_loc}, fkamael_loc={self.fkamael_loc}, mertheia_loc={self.mertheia_loc}, fertheia_loc={self.fertheia_loc}, msylph_loc={self.msylph_loc}, fsylph_loc={self.fsylph_loc}, mHighElf_loc={self.mHighElf_loc}, fHighElf_loc={self.fHighElf_loc}, empty_loc={self.empty_loc}, mfighter_rot={self.mfighter_rot}, ffighter_rot={self.ffighter_rot}, mmagic_rot={self.mmagic_rot}, fmagic_rot={self.fmagic_rot}, melf_rot={self.melf_rot}, felf_rot={self.felf_rot}, mdarkelf_rot={self.mdarkelf_rot}, fdarkelf_rot={self.fdarkelf_rot}, mdwarf_rot={self.mdwarf_rot}, fdwarf_rot={self.fdwarf_rot}, morc_rot={self.morc_rot}, forc_rot={self.forc_rot}, mshaman_rot={self.mshaman_rot}, fshaman_rot={self.fshaman_rot}, mkamael_rot={self.mkamael_rot}, fkamael_rot={self.fkamael_rot}, mertheia_rot={self.mertheia_rot}, fertheia_rot={self.fertheia_rot}, msylph_rot={self.msylph_rot}, fsylph_rot={self.fsylph_rot}, mHighElf_rot={self.mHighElf_rot}, fHighElf_rot={self.fHighElf_rot}, empty_rot={self.empty_rot}, nameoffset={self.nameoffset})"



class ScenePlayerData(object):

    def __init__(self, scene_id, scene_name, play_time):
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.play_time = play_time

    @classmethod
    def from_string(self, line) -> 'ScenePlayerData':
        split_params = line.split('\t')[1:-1]
        attributes = ['scene_id', 'scene_name', 'play_time']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('scene_id'), data.get('scene_name'), data.get('play_time'))
    
    def __str__(self):
        return f"ScenePlayerData(scene_id={self.scene_id}, scene_name={self.scene_name}, play_time={self.play_time})"



class ServerName(object):

    def __init__(self, id, color, name, visible_id):
        self.id = id
        self.color = color
        self.name = name
        self.visible_id = visible_id

    @classmethod
    def from_string(self, line) -> 'ServerName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'color', 'name', 'visible_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('color'), data.get('name'), data.get('visible_id'))
    
    def __str__(self):
        return f"ServerName(id={self.id}, color={self.color}, name={self.name}, visible_id={self.visible_id})"



class SetItemGrp(AbstractItemInfo):

    def __init__(self, num, essential_setitem_id, essential_setitem_desc, additional_setitem_id, additional_setitem_desc, unk1, unk2, enchant_setitem_condition):
        super().__init__(object_id)
        self.num = num
        self.essential_setitem_id = essential_setitem_id
        self.essential_setitem_desc = essential_setitem_desc
        self.additional_setitem_id = additional_setitem_id
        self.additional_setitem_desc = additional_setitem_desc
        self.unk1 = unk1
        self.unk2 = unk2
        self.enchant_setitem_condition = enchant_setitem_condition

    @classmethod
    def from_string(cls, line) -> 'SetItemGrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['num', 'essential_setitem_id', 'essential_setitem_desc', 'additional_setitem_id', 'additional_setitem_desc', 'unk1', 'unk2', 'enchant_setitem_condition']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('num'), data.get('essential_setitem_id'), data.get('essential_setitem_desc'), data.get('additional_setitem_id'), data.get('additional_setitem_desc'), data.get('unk1'), data.get('unk2'), data.get('enchant_setitem_condition'))
    
    def __str__(self):
        return f"SetItemGrp(num={self.num}, essential_setitem_id={self.essential_setitem_id}, essential_setitem_desc={self.essential_setitem_desc}, additional_setitem_id={self.additional_setitem_id}, additional_setitem_desc={self.additional_setitem_desc}, unk1={self.unk1}, unk2={self.unk2}, enchant_setitem_condition={self.enchant_setitem_condition})"



class SetItemGrp(AbstractItemInfo):

    def __init__(self, num, essential_setitem_id, essential_setitem_desc, additional_setitem_id, additional_setitem_desc, unk1, unk2, enchant_setitem_condition):
        super().__init__(object_id)
        self.num = num
        self.essential_setitem_id = essential_setitem_id
        self.essential_setitem_desc = essential_setitem_desc
        self.additional_setitem_id = additional_setitem_id
        self.additional_setitem_desc = additional_setitem_desc
        self.unk1 = unk1
        self.unk2 = unk2
        self.enchant_setitem_condition = enchant_setitem_condition

    @classmethod
    def from_string(cls, line) -> 'SetItemGrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['num', 'essential_setitem_id', 'essential_setitem_desc', 'additional_setitem_id', 'additional_setitem_desc', 'unk1', 'unk2', 'enchant_setitem_condition']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('num'), data.get('essential_setitem_id'), data.get('essential_setitem_desc'), data.get('additional_setitem_id'), data.get('additional_setitem_desc'), data.get('unk1'), data.get('unk2'), data.get('enchant_setitem_condition'))
    
    def __str__(self):
        return f"SetItemGrp(num={self.num}, essential_setitem_id={self.essential_setitem_id}, essential_setitem_desc={self.essential_setitem_desc}, additional_setitem_id={self.additional_setitem_id}, additional_setitem_desc={self.additional_setitem_desc}, unk1={self.unk1}, unk2={self.unk2}, enchant_setitem_condition={self.enchant_setitem_condition})"



class ShortcutAlias(object):

    def __init__(self, id, command, strnum, msgnum):
        self.id = id
        self.command = command
        self.strnum = strnum
        self.msgnum = msgnum

    @classmethod
    def from_string(self, line) -> 'ShortcutAlias':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'command', 'strnum', 'msgnum']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('command'), data.get('strnum'), data.get('msgnum'))
    
    def __str__(self):
        return f"ShortcutAlias(id={self.id}, command={self.command}, strnum={self.strnum}, msgnum={self.msgnum})"



class ShuttleData(object):

    def __init__(self, type_id, shuttle_yaw, shuttle_mesh, door_mesh, blocking_mesh, wall_mesh, ShuttleSound, ShuttleStartSound, ShuttleStopSound, ShuttleSoundVol, ShuttleSoundVolWhenStop, ShuttleSoundRadii):
        self.type_id = type_id
        self.shuttle_yaw = shuttle_yaw
        self.shuttle_mesh = shuttle_mesh
        self.door_mesh = door_mesh
        self.blocking_mesh = blocking_mesh
        self.wall_mesh = wall_mesh
        self.ShuttleSound = ShuttleSound
        self.ShuttleStartSound = ShuttleStartSound
        self.ShuttleStopSound = ShuttleStopSound
        self.ShuttleSoundVol = ShuttleSoundVol
        self.ShuttleSoundVolWhenStop = ShuttleSoundVolWhenStop
        self.ShuttleSoundRadii = ShuttleSoundRadii

    @classmethod
    def from_string(self, line) -> 'ShuttleData':
        split_params = line.split('\t')[1:-1]
        attributes = ['type_id', 'shuttle_yaw', 'shuttle_mesh', 'door_mesh', 'blocking_mesh', 'wall_mesh', 'ShuttleSound', 'ShuttleStartSound', 'ShuttleStopSound', 'ShuttleSoundVol', 'ShuttleSoundVolWhenStop', 'ShuttleSoundRadii']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('type_id'), data.get('shuttle_yaw'), data.get('shuttle_mesh'), data.get('door_mesh'), data.get('blocking_mesh'), data.get('wall_mesh'), data.get('ShuttleSound'), data.get('ShuttleStartSound'), data.get('ShuttleStopSound'), data.get('ShuttleSoundVol'), data.get('ShuttleSoundVolWhenStop'), data.get('ShuttleSoundRadii'))
    
    def __str__(self):
        return f"ShuttleData(type_id={self.type_id}, shuttle_yaw={self.shuttle_yaw}, shuttle_mesh={self.shuttle_mesh}, door_mesh={self.door_mesh}, blocking_mesh={self.blocking_mesh}, wall_mesh={self.wall_mesh}, ShuttleSound={self.ShuttleSound}, ShuttleStartSound={self.ShuttleStartSound}, ShuttleStopSound={self.ShuttleStopSound}, ShuttleSoundVol={self.ShuttleSoundVol}, ShuttleSoundVolWhenStop={self.ShuttleSoundVolWhenStop}, ShuttleSoundRadii={self.ShuttleSoundRadii})"



class SkillAcquire(object):

    def __init__(self, block_skill_id, class_id, skill_id, consume_sp, consume_adena, consume_priority_item, consume_item, multisell_group_id, system_msg_id, level, get_lv, category_index):
        self.block_skill_id = block_skill_id
        self.class_id = class_id
        self.skill_id = skill_id
        self.consume_sp = consume_sp
        self.consume_adena = consume_adena
        self.consume_priority_item = consume_priority_item
        self.consume_item = consume_item
        self.multisell_group_id = multisell_group_id
        self.system_msg_id = system_msg_id
        self.level = level
        self.get_lv = get_lv
        self.category_index = category_index

    @classmethod
    def from_string(self, line) -> 'SkillAcquire':
        split_params = line.split('\t')[1:-1]
        attributes = ['block_skill_id', 'class_id', 'skill_id', 'consume_sp', 'consume_adena', 'consume_priority_item', 'consume_item', 'multisell_group_id', 'system_msg_id', 'level', 'get_lv', 'category_index']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('block_skill_id'), data.get('class_id'), data.get('skill_id'), data.get('consume_sp'), data.get('consume_adena'), data.get('consume_priority_item'), data.get('consume_item'), data.get('multisell_group_id'), data.get('system_msg_id'), data.get('level'), data.get('get_lv'), data.get('category_index'))
    
    def __str__(self):
        return f"SkillAcquire(block_skill_id={self.block_skill_id}, class_id={self.class_id}, skill_id={self.skill_id}, consume_sp={self.consume_sp}, consume_adena={self.consume_adena}, consume_priority_item={self.consume_priority_item}, consume_item={self.consume_item}, multisell_group_id={self.multisell_group_id}, system_msg_id={self.system_msg_id}, level={self.level}, get_lv={self.get_lv}, category_index={self.category_index})"



class SkillEnchantCharge(object):

    def __init__(self, group_item, exp_grade, commission_item_id, group_id, target_level):
        self.group_item = group_item
        self.exp_grade = exp_grade
        self.commission_item_id = commission_item_id
        self.group_id = group_id
        self.target_level = target_level

    @classmethod
    def from_string(self, line) -> 'SkillEnchantCharge':
        split_params = line.split('\t')[1:-1]
        attributes = ['group_item', 'exp_grade', 'commission_item_id', 'group_id', 'target_level']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('group_item'), data.get('exp_grade'), data.get('commission_item_id'), data.get('group_id'), data.get('target_level'))
    
    def __str__(self):
        return f"SkillEnchantCharge(group_item={self.group_item}, exp_grade={self.exp_grade}, commission_item_id={self.commission_item_id}, group_id={self.group_id}, target_level={self.target_level})"



class Skillenchantsetting(object):

    def __init__(self, error):
        self.error = error

    @classmethod
    def from_string(self, line) -> 'Skillenchantsetting':
        split_params = line.split('\t')[1:-1]
        attributes = ['error']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('error'))
    
    def __str__(self):
        return f"Skillenchantsetting(error={self.error})"



class Skillgrp(AbstractItemInfo):

    def __init__(self, skill_id, level, sublevel, icon_type, icon_hide, MagicType, operate_type, mp_consume, cast_range, cast_style, hit_time, cool_time, reuse_delay, effect_point, is_magic, origin_skill, is_double, animation, skill_visual_effect, icon, icon_panel, debuff, resist_cast, enchant_skill_level, enchant_icon, hp_consume, rumble_self, rumble_target, level_hide, dp_consume, energy_consume, abnormal_time, trait_type, target_type, affect_scope, grade, group_type, order_id, auto_use_type, icon_panel_2):
        super().__init__(skill_id)
        self.id = skill_id
        self.level = level
        self.sublevel = sublevel
        self.icon_type = icon_type
        self.icon_hide = icon_hide
        self.MagicType = MagicType
        self.operate_type = operate_type
        self.mp_consume = mp_consume
        self.cast_range = cast_range
        self.cast_style = cast_style
        self.hit_time = hit_time
        self.cool_time = cool_time
        self.reuse_delay = reuse_delay
        self.effect_point = effect_point
        self.is_magic = is_magic
        self.origin_skill = origin_skill
        self.is_double = is_double
        self.animation = animation
        self.skill_visual_effect = skill_visual_effect
        self.icon = icon
        self.icon_panel = icon_panel
        self.debuff = debuff
        self.resist_cast = resist_cast
        self.enchant_skill_level = enchant_skill_level
        self.enchant_icon = enchant_icon
        self.hp_consume = hp_consume
        self.rumble_self = rumble_self
        self.rumble_target = rumble_target
        self.level_hide = level_hide
        self.dp_consume = dp_consume
        self.energy_consume = energy_consume
        self.abnormal_time = abnormal_time
        self.trait_type = trait_type
        self.target_type = target_type
        self.affect_scope = affect_scope
        self.grade = grade
        self.group_type = group_type
        self.order_id = order_id
        self.auto_use_type = auto_use_type
        self.icon_panel_2 = icon_panel_2

    @classmethod
    def from_string(cls, line) -> 'Skillgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'level', 'sublevel', 'icon_type', 'icon_hide', 'MagicType', 'operate_type', 'mp_consume', 'cast_range', 'cast_style', 'hit_time', 'cool_time', 'reuse_delay', 'effect_point', 'is_magic', 'origin_skill', 'is_double', 'animation', 'skill_visual_effect', 'icon', 'icon_panel', 'debuff', 'resist_cast', 'enchant_skill_level', 'enchant_icon', 'hp_consume', 'rumble_self', 'rumble_target', 'level_hide', 'dp_consume', 'energy_consume', 'abnormal_time', 'trait_type', 'target_type', 'affect_scope', 'grade', 'group_type', 'order_id', 'auto_use_type', 'icon_panel_2']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('id'), data.get('level'), data.get('sublevel'), data.get('icon_type'), data.get('icon_hide'), data.get('MagicType'), data.get('operate_type'), data.get('mp_consume'), data.get('cast_range'), data.get('cast_style'), data.get('hit_time'), data.get('cool_time'), data.get('reuse_delay'), data.get('effect_point'), data.get('is_magic'), data.get('origin_skill'), data.get('is_double'), data.get('animation'), data.get('skill_visual_effect'), data.get('icon'), data.get('icon_panel'), data.get('debuff'), data.get('resist_cast'), data.get('enchant_skill_level'), data.get('enchant_icon'), data.get('hp_consume'), data.get('rumble_self'), data.get('rumble_target'), data.get('level_hide'), data.get('dp_consume'), data.get('energy_consume'), data.get('abnormal_time'), data.get('trait_type'), data.get('target_type'), data.get('affect_scope'), data.get('grade'), data.get('group_type'), data.get('order_id'), data.get('auto_use_type'), data.get('icon_panel_2'))
    
    def __str__(self):
        return f"Skillgrp(id={self.id}, level={self.level}, sublevel={self.sublevel}, icon_type={self.icon_type}, icon_hide={self.icon_hide}, MagicType={self.MagicType}, operate_type={self.operate_type}, mp_consume={self.mp_consume}, cast_range={self.cast_range}, cast_style={self.cast_style}, hit_time={self.hit_time}, cool_time={self.cool_time}, reuse_delay={self.reuse_delay}, effect_point={self.effect_point}, is_magic={self.is_magic}, origin_skill={self.origin_skill}, is_double={self.is_double}, animation={self.animation}, skill_visual_effect={self.skill_visual_effect}, icon={self.icon}, icon_panel={self.icon_panel}, debuff={self.debuff}, resist_cast={self.resist_cast}, enchant_skill_level={self.enchant_skill_level}, enchant_icon={self.enchant_icon}, hp_consume={self.hp_consume}, rumble_self={self.rumble_self}, rumble_target={self.rumble_target}, level_hide={self.level_hide}, dp_consume={self.dp_consume}, energy_consume={self.energy_consume}, abnormal_time={self.abnormal_time}, trait_type={self.trait_type}, target_type={self.target_type}, affect_scope={self.affect_scope}, grade={self.grade}, group_type={self.group_type}, order_id={self.order_id}, auto_use_type={self.auto_use_type}, icon_panel_2={self.icon_panel_2})"

    def __repr__(self) -> str:
        return f"Skillgrp(id={self.id}, level={self.level}, sublevel={self.sublevel}, icon_type={self.icon_type}, icon_hide={self.icon_hide}, MagicType={self.MagicType}, operate_type={self.operate_type}, mp_consume={self.mp_consume}, cast_range={self.cast_range}, cast_style={self.cast_style}, hit_time={self.hit_time}, cool_time={self.cool_time}, reuse_delay={self.reuse_delay}, effect_point={self.effect_point}, is_magic={self.is_magic}, origin_skill={self.origin_skill}, is_double={self.is_double}, animation={self.animation}, skill_visual_effect={self.skill_visual_effect}, icon={self.icon}, icon_panel={self.icon_panel}, debuff={self.debuff}, resist_cast={self.resist_cast}, enchant_skill_level={self.enchant_skill_level}, enchant_icon={self.enchant_icon}, hp_consume={self.hp_consume}, rumble_self={self.rumble_self}, rumble_target={self.rumble_target}, level_hide={self.level_hide}, dp_consume={self.dp_consume}, energy_consume={self.energy_consume}, abnormal_time={self.abnormal_time}, trait_type={self.trait_type}, target_type={self.target_type}, affect_scope={self.affect_scope}, grade={self.grade}, group_type={self.group_type}, order_id={self.order_id}, auto_use_type={self.auto_use_type}, icon_panel_2={self.icon_panel_2})"

class SkillName(object):

    def __init__(self, skill_id, skill_level, skill_sublevel, name, desc, desc_param, enchant_name, enchant_name_param, enchant_desc, enchant_desc_param):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_sublevel = skill_sublevel
        self.name = name
        self.desc = desc
        self.desc_param = desc_param
        self.enchant_name = enchant_name
        self.enchant_name_param = enchant_name_param
        self.enchant_desc = enchant_desc
        self.enchant_desc_param = enchant_desc_param

    @classmethod
    def from_string(self, line) -> 'SkillName':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_sublevel', 'name', 'desc', 'desc_param', 'enchant_name', 'enchant_name_param', 'enchant_desc', 'enchant_desc_param']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('skill_sublevel'), data.get('name'), data.get('desc'), data.get('desc_param'), data.get('enchant_name'), data.get('enchant_name_param'), data.get('enchant_desc'), data.get('enchant_desc_param'))
    
    def __str__(self):
        return f"SkillName(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_sublevel={self.skill_sublevel}, name={self.name}, desc={self.desc}, desc_param={self.desc_param}, enchant_name={self.enchant_name}, enchant_name_param={self.enchant_name_param}, enchant_desc={self.enchant_desc}, enchant_desc_param={self.enchant_desc_param})"



class SkillName(object):

    def __init__(self, skill_id, skill_level, skill_sublevel, name, desc, desc_param, enchant_name, enchant_name_param, enchant_desc, enchant_desc_param):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_sublevel = skill_sublevel
        self.name = name
        self.desc = desc
        self.desc_param = desc_param
        self.enchant_name = enchant_name
        self.enchant_name_param = enchant_name_param
        self.enchant_desc = enchant_desc
        self.enchant_desc_param = enchant_desc_param

    @classmethod
    def from_string(self, line) -> 'SkillName':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_sublevel', 'name', 'desc', 'desc_param', 'enchant_name', 'enchant_name_param', 'enchant_desc', 'enchant_desc_param']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('skill_level'), data.get('skill_sublevel'), data.get('name'), data.get('desc'), data.get('desc_param'), data.get('enchant_name'), data.get('enchant_name_param'), data.get('enchant_desc'), data.get('enchant_desc_param'))
    
    def __str__(self):
        return f"SkillName(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_sublevel={self.skill_sublevel}, name={self.name}, desc={self.desc}, desc_param={self.desc_param}, enchant_name={self.enchant_name}, enchant_name_param={self.enchant_name_param}, enchant_desc={self.enchant_desc}, enchant_desc_param={self.enchant_desc_param})"



class SkillSoundgrp(AbstractItemInfo):

    def __init__(self, skill_id, skill_level, skill_sublevel, spelleffect_sound_1, spelleffect_sound_2, spelleffect_sound_3, spelleffect_sound_vol_1, spelleffect_sound_rad_1, spelleffect_sound_delay_1, spelleffect_sound_vol_2, spelleffect_sound_rad_2, spelleffect_sound_delay_2, spelleffect_sound_vol_3, spelleffect_sound_rad_3, spelleffect_sound_delay_3, shoteffect_sound_1, shoteffect_sound_2, shoteffect_sound_3, shoteffect_sound_vol_1, shoteffect_sound_rad_1, shoteffect_sound_delay_1, shoteffect_sound_vol_2, shoteffect_sound_rad_2, shoteffect_sound_delay_2, shoteffect_sound_vol_3, shoteffect_sound_rad_3, shoteffect_sound_delay_3, expeffect_sound_1, expeffect_sound_2, expeffect_sound_3, expeffect_sound_vol_1, expeffect_sound_rad_1, expeffect_sound_delay_1, expeffect_sound_vol_2, expeffect_sound_rad_2, expeffect_sound_delay_2, expeffect_sound_vol_3, expeffect_sound_rad_3, expeffect_sound_delay_3, mfighter_cast, ffighter_cast, mmagic_cast, fmagic_cast, melf_cast, felf_cast, mdarkelf_cast, fdarkelf_cast, mdwarf_cast, fdwarf_cast, morc_cast, forc_cast, mshaman_cast, fshaman_cast, mkamael_cast, fkamael_cast, mertheia_cast, fertheia_cast, msylph_cast, fsylph_cast, mhighelf_cast, fhighelf_cast, mextra_throw, mfighter_magic, ffighter_magic, mmagic_magic, fmagic_magic, melf_magic, felf_magic, mdarkelf_magic, fdarkelf_magic, mdwarf_magic, fdwarf_magic, morc_magic, forc_magic, mshaman_magic, fshaman_magic, mkamael_magic, fkamael_magic, mertheia_magic, fertheia_magic, msylph_magic, fsylph_magic, mhighelf_magic, fhighelf_magic, fextra_throw, cast_volume, cast_rad):
        super().__init__(object_id)
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_sublevel = skill_sublevel
        self.spelleffect_sound_1 = spelleffect_sound_1
        self.spelleffect_sound_2 = spelleffect_sound_2
        self.spelleffect_sound_3 = spelleffect_sound_3
        self.spelleffect_sound_vol_1 = spelleffect_sound_vol_1
        self.spelleffect_sound_rad_1 = spelleffect_sound_rad_1
        self.spelleffect_sound_delay_1 = spelleffect_sound_delay_1
        self.spelleffect_sound_vol_2 = spelleffect_sound_vol_2
        self.spelleffect_sound_rad_2 = spelleffect_sound_rad_2
        self.spelleffect_sound_delay_2 = spelleffect_sound_delay_2
        self.spelleffect_sound_vol_3 = spelleffect_sound_vol_3
        self.spelleffect_sound_rad_3 = spelleffect_sound_rad_3
        self.spelleffect_sound_delay_3 = spelleffect_sound_delay_3
        self.shoteffect_sound_1 = shoteffect_sound_1
        self.shoteffect_sound_2 = shoteffect_sound_2
        self.shoteffect_sound_3 = shoteffect_sound_3
        self.shoteffect_sound_vol_1 = shoteffect_sound_vol_1
        self.shoteffect_sound_rad_1 = shoteffect_sound_rad_1
        self.shoteffect_sound_delay_1 = shoteffect_sound_delay_1
        self.shoteffect_sound_vol_2 = shoteffect_sound_vol_2
        self.shoteffect_sound_rad_2 = shoteffect_sound_rad_2
        self.shoteffect_sound_delay_2 = shoteffect_sound_delay_2
        self.shoteffect_sound_vol_3 = shoteffect_sound_vol_3
        self.shoteffect_sound_rad_3 = shoteffect_sound_rad_3
        self.shoteffect_sound_delay_3 = shoteffect_sound_delay_3
        self.expeffect_sound_1 = expeffect_sound_1
        self.expeffect_sound_2 = expeffect_sound_2
        self.expeffect_sound_3 = expeffect_sound_3
        self.expeffect_sound_vol_1 = expeffect_sound_vol_1
        self.expeffect_sound_rad_1 = expeffect_sound_rad_1
        self.expeffect_sound_delay_1 = expeffect_sound_delay_1
        self.expeffect_sound_vol_2 = expeffect_sound_vol_2
        self.expeffect_sound_rad_2 = expeffect_sound_rad_2
        self.expeffect_sound_delay_2 = expeffect_sound_delay_2
        self.expeffect_sound_vol_3 = expeffect_sound_vol_3
        self.expeffect_sound_rad_3 = expeffect_sound_rad_3
        self.expeffect_sound_delay_3 = expeffect_sound_delay_3
        self.mfighter_cast = mfighter_cast
        self.ffighter_cast = ffighter_cast
        self.mmagic_cast = mmagic_cast
        self.fmagic_cast = fmagic_cast
        self.melf_cast = melf_cast
        self.felf_cast = felf_cast
        self.mdarkelf_cast = mdarkelf_cast
        self.fdarkelf_cast = fdarkelf_cast
        self.mdwarf_cast = mdwarf_cast
        self.fdwarf_cast = fdwarf_cast
        self.morc_cast = morc_cast
        self.forc_cast = forc_cast
        self.mshaman_cast = mshaman_cast
        self.fshaman_cast = fshaman_cast
        self.mkamael_cast = mkamael_cast
        self.fkamael_cast = fkamael_cast
        self.mertheia_cast = mertheia_cast
        self.fertheia_cast = fertheia_cast
        self.msylph_cast = msylph_cast
        self.fsylph_cast = fsylph_cast
        self.mhighelf_cast = mhighelf_cast
        self.fhighelf_cast = fhighelf_cast
        self.mextra_throw = mextra_throw
        self.mfighter_magic = mfighter_magic
        self.ffighter_magic = ffighter_magic
        self.mmagic_magic = mmagic_magic
        self.fmagic_magic = fmagic_magic
        self.melf_magic = melf_magic
        self.felf_magic = felf_magic
        self.mdarkelf_magic = mdarkelf_magic
        self.fdarkelf_magic = fdarkelf_magic
        self.mdwarf_magic = mdwarf_magic
        self.fdwarf_magic = fdwarf_magic
        self.morc_magic = morc_magic
        self.forc_magic = forc_magic
        self.mshaman_magic = mshaman_magic
        self.fshaman_magic = fshaman_magic
        self.mkamael_magic = mkamael_magic
        self.fkamael_magic = fkamael_magic
        self.mertheia_magic = mertheia_magic
        self.fertheia_magic = fertheia_magic
        self.msylph_magic = msylph_magic
        self.fsylph_magic = fsylph_magic
        self.mhighelf_magic = mhighelf_magic
        self.fhighelf_magic = fhighelf_magic
        self.fextra_throw = fextra_throw
        self.cast_volume = cast_volume
        self.cast_rad = cast_rad

    @classmethod
    def from_string(cls, line) -> 'SkillSoundgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'skill_level', 'skill_sublevel', 'spelleffect_sound_1', 'spelleffect_sound_2', 'spelleffect_sound_3', 'spelleffect_sound_vol_1', 'spelleffect_sound_rad_1', 'spelleffect_sound_delay_1', 'spelleffect_sound_vol_2', 'spelleffect_sound_rad_2', 'spelleffect_sound_delay_2', 'spelleffect_sound_vol_3', 'spelleffect_sound_rad_3', 'spelleffect_sound_delay_3', 'shoteffect_sound_1', 'shoteffect_sound_2', 'shoteffect_sound_3', 'shoteffect_sound_vol_1', 'shoteffect_sound_rad_1', 'shoteffect_sound_delay_1', 'shoteffect_sound_vol_2', 'shoteffect_sound_rad_2', 'shoteffect_sound_delay_2', 'shoteffect_sound_vol_3', 'shoteffect_sound_rad_3', 'shoteffect_sound_delay_3', 'expeffect_sound_1', 'expeffect_sound_2', 'expeffect_sound_3', 'expeffect_sound_vol_1', 'expeffect_sound_rad_1', 'expeffect_sound_delay_1', 'expeffect_sound_vol_2', 'expeffect_sound_rad_2', 'expeffect_sound_delay_2', 'expeffect_sound_vol_3', 'expeffect_sound_rad_3', 'expeffect_sound_delay_3', 'mfighter_cast', 'ffighter_cast', 'mmagic_cast', 'fmagic_cast', 'melf_cast', 'felf_cast', 'mdarkelf_cast', 'fdarkelf_cast', 'mdwarf_cast', 'fdwarf_cast', 'morc_cast', 'forc_cast', 'mshaman_cast', 'fshaman_cast', 'mkamael_cast', 'fkamael_cast', 'mertheia_cast', 'fertheia_cast', 'msylph_cast', 'fsylph_cast', 'mhighelf_cast', 'fhighelf_cast', 'mextra_throw', 'mfighter_magic', 'ffighter_magic', 'mmagic_magic', 'fmagic_magic', 'melf_magic', 'felf_magic', 'mdarkelf_magic', 'fdarkelf_magic', 'mdwarf_magic', 'fdwarf_magic', 'morc_magic', 'forc_magic', 'mshaman_magic', 'fshaman_magic', 'mkamael_magic', 'fkamael_magic', 'mertheia_magic', 'fertheia_magic', 'msylph_magic', 'fsylph_magic', 'mhighelf_magic', 'fhighelf_magic', 'fextra_throw', 'cast_volume', 'cast_rad']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('skill_id'), data.get('skill_level'), data.get('skill_sublevel'), data.get('spelleffect_sound_1'), data.get('spelleffect_sound_2'), data.get('spelleffect_sound_3'), data.get('spelleffect_sound_vol_1'), data.get('spelleffect_sound_rad_1'), data.get('spelleffect_sound_delay_1'), data.get('spelleffect_sound_vol_2'), data.get('spelleffect_sound_rad_2'), data.get('spelleffect_sound_delay_2'), data.get('spelleffect_sound_vol_3'), data.get('spelleffect_sound_rad_3'), data.get('spelleffect_sound_delay_3'), data.get('shoteffect_sound_1'), data.get('shoteffect_sound_2'), data.get('shoteffect_sound_3'), data.get('shoteffect_sound_vol_1'), data.get('shoteffect_sound_rad_1'), data.get('shoteffect_sound_delay_1'), data.get('shoteffect_sound_vol_2'), data.get('shoteffect_sound_rad_2'), data.get('shoteffect_sound_delay_2'), data.get('shoteffect_sound_vol_3'), data.get('shoteffect_sound_rad_3'), data.get('shoteffect_sound_delay_3'), data.get('expeffect_sound_1'), data.get('expeffect_sound_2'), data.get('expeffect_sound_3'), data.get('expeffect_sound_vol_1'), data.get('expeffect_sound_rad_1'), data.get('expeffect_sound_delay_1'), data.get('expeffect_sound_vol_2'), data.get('expeffect_sound_rad_2'), data.get('expeffect_sound_delay_2'), data.get('expeffect_sound_vol_3'), data.get('expeffect_sound_rad_3'), data.get('expeffect_sound_delay_3'), data.get('mfighter_cast'), data.get('ffighter_cast'), data.get('mmagic_cast'), data.get('fmagic_cast'), data.get('melf_cast'), data.get('felf_cast'), data.get('mdarkelf_cast'), data.get('fdarkelf_cast'), data.get('mdwarf_cast'), data.get('fdwarf_cast'), data.get('morc_cast'), data.get('forc_cast'), data.get('mshaman_cast'), data.get('fshaman_cast'), data.get('mkamael_cast'), data.get('fkamael_cast'), data.get('mertheia_cast'), data.get('fertheia_cast'), data.get('msylph_cast'), data.get('fsylph_cast'), data.get('mhighelf_cast'), data.get('fhighelf_cast'), data.get('mextra_throw'), data.get('mfighter_magic'), data.get('ffighter_magic'), data.get('mmagic_magic'), data.get('fmagic_magic'), data.get('melf_magic'), data.get('felf_magic'), data.get('mdarkelf_magic'), data.get('fdarkelf_magic'), data.get('mdwarf_magic'), data.get('fdwarf_magic'), data.get('morc_magic'), data.get('forc_magic'), data.get('mshaman_magic'), data.get('fshaman_magic'), data.get('mkamael_magic'), data.get('fkamael_magic'), data.get('mertheia_magic'), data.get('fertheia_magic'), data.get('msylph_magic'), data.get('fsylph_magic'), data.get('mhighelf_magic'), data.get('fhighelf_magic'), data.get('fextra_throw'), data.get('cast_volume'), data.get('cast_rad'))
    
    def __str__(self):
        return f"SkillSoundgrp(skill_id={self.skill_id}, skill_level={self.skill_level}, skill_sublevel={self.skill_sublevel}, spelleffect_sound_1={self.spelleffect_sound_1}, spelleffect_sound_2={self.spelleffect_sound_2}, spelleffect_sound_3={self.spelleffect_sound_3}, spelleffect_sound_vol_1={self.spelleffect_sound_vol_1}, spelleffect_sound_rad_1={self.spelleffect_sound_rad_1}, spelleffect_sound_delay_1={self.spelleffect_sound_delay_1}, spelleffect_sound_vol_2={self.spelleffect_sound_vol_2}, spelleffect_sound_rad_2={self.spelleffect_sound_rad_2}, spelleffect_sound_delay_2={self.spelleffect_sound_delay_2}, spelleffect_sound_vol_3={self.spelleffect_sound_vol_3}, spelleffect_sound_rad_3={self.spelleffect_sound_rad_3}, spelleffect_sound_delay_3={self.spelleffect_sound_delay_3}, shoteffect_sound_1={self.shoteffect_sound_1}, shoteffect_sound_2={self.shoteffect_sound_2}, shoteffect_sound_3={self.shoteffect_sound_3}, shoteffect_sound_vol_1={self.shoteffect_sound_vol_1}, shoteffect_sound_rad_1={self.shoteffect_sound_rad_1}, shoteffect_sound_delay_1={self.shoteffect_sound_delay_1}, shoteffect_sound_vol_2={self.shoteffect_sound_vol_2}, shoteffect_sound_rad_2={self.shoteffect_sound_rad_2}, shoteffect_sound_delay_2={self.shoteffect_sound_delay_2}, shoteffect_sound_vol_3={self.shoteffect_sound_vol_3}, shoteffect_sound_rad_3={self.shoteffect_sound_rad_3}, shoteffect_sound_delay_3={self.shoteffect_sound_delay_3}, expeffect_sound_1={self.expeffect_sound_1}, expeffect_sound_2={self.expeffect_sound_2}, expeffect_sound_3={self.expeffect_sound_3}, expeffect_sound_vol_1={self.expeffect_sound_vol_1}, expeffect_sound_rad_1={self.expeffect_sound_rad_1}, expeffect_sound_delay_1={self.expeffect_sound_delay_1}, expeffect_sound_vol_2={self.expeffect_sound_vol_2}, expeffect_sound_rad_2={self.expeffect_sound_rad_2}, expeffect_sound_delay_2={self.expeffect_sound_delay_2}, expeffect_sound_vol_3={self.expeffect_sound_vol_3}, expeffect_sound_rad_3={self.expeffect_sound_rad_3}, expeffect_sound_delay_3={self.expeffect_sound_delay_3}, mfighter_cast={self.mfighter_cast}, ffighter_cast={self.ffighter_cast}, mmagic_cast={self.mmagic_cast}, fmagic_cast={self.fmagic_cast}, melf_cast={self.melf_cast}, felf_cast={self.felf_cast}, mdarkelf_cast={self.mdarkelf_cast}, fdarkelf_cast={self.fdarkelf_cast}, mdwarf_cast={self.mdwarf_cast}, fdwarf_cast={self.fdwarf_cast}, morc_cast={self.morc_cast}, forc_cast={self.forc_cast}, mshaman_cast={self.mshaman_cast}, fshaman_cast={self.fshaman_cast}, mkamael_cast={self.mkamael_cast}, fkamael_cast={self.fkamael_cast}, mertheia_cast={self.mertheia_cast}, fertheia_cast={self.fertheia_cast}, msylph_cast={self.msylph_cast}, fsylph_cast={self.fsylph_cast}, mhighelf_cast={self.mhighelf_cast}, fhighelf_cast={self.fhighelf_cast}, mextra_throw={self.mextra_throw}, mfighter_magic={self.mfighter_magic}, ffighter_magic={self.ffighter_magic}, mmagic_magic={self.mmagic_magic}, fmagic_magic={self.fmagic_magic}, melf_magic={self.melf_magic}, felf_magic={self.felf_magic}, mdarkelf_magic={self.mdarkelf_magic}, fdarkelf_magic={self.fdarkelf_magic}, mdwarf_magic={self.mdwarf_magic}, fdwarf_magic={self.fdwarf_magic}, morc_magic={self.morc_magic}, forc_magic={self.forc_magic}, mshaman_magic={self.mshaman_magic}, fshaman_magic={self.fshaman_magic}, mkamael_magic={self.mkamael_magic}, fkamael_magic={self.fkamael_magic}, mertheia_magic={self.mertheia_magic}, fertheia_magic={self.fertheia_magic}, msylph_magic={self.msylph_magic}, fsylph_magic={self.fsylph_magic}, mhighelf_magic={self.mhighelf_magic}, fhighelf_magic={self.fhighelf_magic}, fextra_throw={self.fextra_throw}, cast_volume={self.cast_volume}, cast_rad={self.cast_rad})"



class SkillSoundSource(object):

    def __init__(self, skill_id, spelleffect_sound_1_source, spelleffect_sound_2_source, spelleffect_sound_3_source, shoteffect_sound_1_source, shoteffect_sound_2_source, shoteffect_sound_3_source, expeffect_sound_1_source, expeffect_sound_2_source, expeffect_sound_3_source):
        self.skill_id = skill_id
        self.spelleffect_sound_1_source = spelleffect_sound_1_source
        self.spelleffect_sound_2_source = spelleffect_sound_2_source
        self.spelleffect_sound_3_source = spelleffect_sound_3_source
        self.shoteffect_sound_1_source = shoteffect_sound_1_source
        self.shoteffect_sound_2_source = shoteffect_sound_2_source
        self.shoteffect_sound_3_source = shoteffect_sound_3_source
        self.expeffect_sound_1_source = expeffect_sound_1_source
        self.expeffect_sound_2_source = expeffect_sound_2_source
        self.expeffect_sound_3_source = expeffect_sound_3_source

    @classmethod
    def from_string(self, line) -> 'SkillSoundSource':
        split_params = line.split('\t')[1:-1]
        attributes = ['skill_id', 'spelleffect_sound_1_source', 'spelleffect_sound_2_source', 'spelleffect_sound_3_source', 'shoteffect_sound_1_source', 'shoteffect_sound_2_source', 'shoteffect_sound_3_source', 'expeffect_sound_1_source', 'expeffect_sound_2_source', 'expeffect_sound_3_source']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('skill_id'), data.get('spelleffect_sound_1_source'), data.get('spelleffect_sound_2_source'), data.get('spelleffect_sound_3_source'), data.get('shoteffect_sound_1_source'), data.get('shoteffect_sound_2_source'), data.get('shoteffect_sound_3_source'), data.get('expeffect_sound_1_source'), data.get('expeffect_sound_2_source'), data.get('expeffect_sound_3_source'))
    
    def __str__(self):
        return f"SkillSoundSource(skill_id={self.skill_id}, spelleffect_sound_1_source={self.spelleffect_sound_1_source}, spelleffect_sound_2_source={self.spelleffect_sound_2_source}, spelleffect_sound_3_source={self.spelleffect_sound_3_source}, shoteffect_sound_1_source={self.shoteffect_sound_1_source}, shoteffect_sound_2_source={self.shoteffect_sound_2_source}, shoteffect_sound_3_source={self.shoteffect_sound_3_source}, expeffect_sound_1_source={self.expeffect_sound_1_source}, expeffect_sound_2_source={self.expeffect_sound_2_source}, expeffect_sound_3_source={self.expeffect_sound_3_source})"



class StatBonusName(object):

    def __init__(self, stat_bonus_type, stat_grade, desc):
        self.stat_bonus_type = stat_bonus_type
        self.stat_grade = stat_grade
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'StatBonusName':
        split_params = line.split('\t')[1:-1]
        attributes = ['stat_bonus_type', 'stat_grade', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('stat_bonus_type'), data.get('stat_grade'), data.get('desc'))
    
    def __str__(self):
        return f"StatBonusName(stat_bonus_type={self.stat_bonus_type}, stat_grade={self.stat_grade}, desc={self.desc})"



class StatBonusReset(object):

    def __init__(self, range, consume_items):
        self.range = range
        self.consume_items = consume_items

    @classmethod
    def from_string(self, line) -> 'StatBonusReset':
        split_params = line.split('\t')[1:-1]
        attributes = ['range', 'consume_items']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('range'), data.get('consume_items'))
    
    def __str__(self):
        return f"StatBonusReset(range={self.range}, consume_items={self.consume_items})"



class StaticObject(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_string(self, line) -> 'StaticObject':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'))
    
    def __str__(self):
        return f"StaticObject(id={self.id}, name={self.name})"



class StaticObject(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_string(self, line) -> 'StaticObject':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'))
    
    def __str__(self):
        return f"StaticObject(id={self.id}, name={self.name})"



class StatisticName(object):

    def __init__(self, id, type, type_reserved, category, name, unit, unit_type, zero_invisible, category_list):
        self.id = id
        self.type = type
        self.type_reserved = type_reserved
        self.category = category
        self.name = name
        self.unit = unit
        self.unit_type = unit_type
        self.zero_invisible = zero_invisible
        self.category_list = category_list

    @classmethod
    def from_string(self, line) -> 'StatisticName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'type_reserved', 'category', 'name', 'unit', 'unit_type', 'zero_invisible', 'category_list']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('type_reserved'), data.get('category'), data.get('name'), data.get('unit'), data.get('unit_type'), data.get('zero_invisible'), data.get('category_list'))
    
    def __str__(self):
        return f"StatisticName(id={self.id}, type={self.type}, type_reserved={self.type_reserved}, category={self.category}, name={self.name}, unit={self.unit}, unit_type={self.unit_type}, zero_invisible={self.zero_invisible}, category_list={self.category_list})"



class SteadyBox(object):

    def __init__(self, id, type, title, desc):
        self.id = id
        self.type = type
        self.title = title
        self.desc = desc

    @classmethod
    def from_string(self, line) -> 'SteadyBox':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'type', 'title', 'desc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('type'), data.get('title'), data.get('desc'))
    
    def __str__(self):
        return f"SteadyBox(id={self.id}, type={self.type}, title={self.title}, desc={self.desc})"



class StoreURL(object):

    def __init__(self, img, url, unk):
        self.img = img
        self.url = url
        self.unk = unk

    @classmethod
    def from_string(self, line) -> 'StoreURL':
        split_params = line.split('\t')[1:-1]
        attributes = ['img', 'url', 'unk']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('img'), data.get('url'), data.get('unk'))
    
    def __str__(self):
        return f"StoreURL(img={self.img}, url={self.url}, unk={self.unk})"



class Subjugation(object):

    def __init__(self, id, name, desc, banner, min_level, max_level, max_subjugation_point, max_gacha_point, max_periodic_gacha_point, gacha_cost_item, gacha_cost_num, max_use_point, teleport_id, cycle, hot_times, show_gacha_main, show_gacha_sub, reward_rank1, reward_rank2, reward_rank3, reward_rank4, reward_rank5):
        self.id = id
        self.name = name
        self.desc = desc
        self.banner = banner
        self.min_level = min_level
        self.max_level = max_level
        self.max_subjugation_point = max_subjugation_point
        self.max_gacha_point = max_gacha_point
        self.max_periodic_gacha_point = max_periodic_gacha_point
        self.gacha_cost_item = gacha_cost_item
        self.gacha_cost_num = gacha_cost_num
        self.max_use_point = max_use_point
        self.teleport_id = teleport_id
        self.cycle = cycle
        self.hot_times = hot_times
        self.show_gacha_main = show_gacha_main
        self.show_gacha_sub = show_gacha_sub
        self.reward_rank1 = reward_rank1
        self.reward_rank2 = reward_rank2
        self.reward_rank3 = reward_rank3
        self.reward_rank4 = reward_rank4
        self.reward_rank5 = reward_rank5

    @classmethod
    def from_string(self, line) -> 'Subjugation':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'desc', 'banner', 'min_level', 'max_level', 'max_subjugation_point', 'max_gacha_point', 'max_periodic_gacha_point', 'gacha_cost_item', 'gacha_cost_num', 'max_use_point', 'teleport_id', 'cycle', 'hot_times', 'show_gacha_main', 'show_gacha_sub', 'reward_rank1', 'reward_rank2', 'reward_rank3', 'reward_rank4', 'reward_rank5']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('desc'), data.get('banner'), data.get('min_level'), data.get('max_level'), data.get('max_subjugation_point'), data.get('max_gacha_point'), data.get('max_periodic_gacha_point'), data.get('gacha_cost_item'), data.get('gacha_cost_num'), data.get('max_use_point'), data.get('teleport_id'), data.get('cycle'), data.get('hot_times'), data.get('show_gacha_main'), data.get('show_gacha_sub'), data.get('reward_rank1'), data.get('reward_rank2'), data.get('reward_rank3'), data.get('reward_rank4'), data.get('reward_rank5'))
    
    def __str__(self):
        return f"Subjugation(id={self.id}, name={self.name}, desc={self.desc}, banner={self.banner}, min_level={self.min_level}, max_level={self.max_level}, max_subjugation_point={self.max_subjugation_point}, max_gacha_point={self.max_gacha_point}, max_periodic_gacha_point={self.max_periodic_gacha_point}, gacha_cost_item={self.gacha_cost_item}, gacha_cost_num={self.gacha_cost_num}, max_use_point={self.max_use_point}, teleport_id={self.teleport_id}, cycle={self.cycle}, hot_times={self.hot_times}, show_gacha_main={self.show_gacha_main}, show_gacha_sub={self.show_gacha_sub}, reward_rank1={self.reward_rank1}, reward_rank2={self.reward_rank2}, reward_rank3={self.reward_rank3}, reward_rank4={self.reward_rank4}, reward_rank5={self.reward_rank5})"



class SymbolName(object):

    def __init__(self, id, filename, alias, UNK_0):
        self.id = id
        self.filename = filename
        self.alias = alias
        self.UNK_0 = UNK_0

    @classmethod
    def from_string(self, line) -> 'SymbolName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'filename', 'alias', 'UNK_0']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('filename'), data.get('alias'), data.get('UNK_0'))
    
    def __str__(self):
        return f"SymbolName(id={self.id}, filename={self.filename}, alias={self.alias}, UNK_0={self.UNK_0})"



class SymbolName(object):

    def __init__(self, id, filename, alias, UNK_0):
        self.id = id
        self.filename = filename
        self.alias = alias
        self.UNK_0 = UNK_0

    @classmethod
    def from_string(self, line) -> 'SymbolName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'filename', 'alias', 'UNK_0']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('filename'), data.get('alias'), data.get('UNK_0'))
    
    def __str__(self):
        return f"SymbolName(id={self.id}, filename={self.filename}, alias={self.alias}, UNK_0={self.UNK_0})"



class SysString(object):

    def __init__(self, stringID, string):
        self.stringID = stringID
        self.string = string

    @classmethod
    def from_string(self, line) -> 'SysString':
        split_params = line.split('\t')[1:-1]
        attributes = ['stringID', 'string']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('stringID'), data.get('string'))
    
    def __str__(self):
        return f"SysString(stringID={self.stringID}, string={self.string})"



class SysString(object):

    def __init__(self, stringID, string):
        self.stringID = stringID
        self.string = string

    @classmethod
    def from_string(self, line) -> 'SysString':
        split_params = line.split('\t')[1:-1]
        attributes = ['stringID', 'string']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('stringID'), data.get('string'))
    
    def __str__(self):
        return f"SysString(stringID={self.stringID}, string={self.string})"



class SystemMsg(object):

    def __init__(self, id, UNK_0, message, group, color, sound, voice, unk_414, win, font, lftime, bkg, anim, scrnmsg, scrnparam, gfxscrnmsg, gfxscrnparam, type):
        self.id = id
        self.UNK_0 = UNK_0
        self.message = message
        self.group = group
        self.color = color
        self.sound = sound
        self.voice = voice
        self.unk_414 = unk_414
        self.win = win
        self.font = font
        self.lftime = lftime
        self.bkg = bkg
        self.anim = anim
        self.scrnmsg = scrnmsg
        self.scrnparam = scrnparam
        self.gfxscrnmsg = gfxscrnmsg
        self.gfxscrnparam = gfxscrnparam
        self.type = type

    @classmethod
    def from_string(self, line) -> 'SystemMsg':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'UNK_0', 'message', 'group', 'color', 'sound', 'voice', 'unk_414', 'win', 'font', 'lftime', 'bkg', 'anim', 'scrnmsg', 'scrnparam', 'gfxscrnmsg', 'gfxscrnparam', 'type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('UNK_0'), data.get('message'), data.get('group'), data.get('color'), data.get('sound'), data.get('voice'), data.get('unk_414'), data.get('win'), data.get('font'), data.get('lftime'), data.get('bkg'), data.get('anim'), data.get('scrnmsg'), data.get('scrnparam'), data.get('gfxscrnmsg'), data.get('gfxscrnparam'), data.get('type'))
    
    def __str__(self):
        return f"SystemMsg(id={self.id}, UNK_0={self.UNK_0}, message={self.message}, group={self.group}, color={self.color}, sound={self.sound}, voice={self.voice}, unk_414={self.unk_414}, win={self.win}, font={self.font}, lftime={self.lftime}, bkg={self.bkg}, anim={self.anim}, scrnmsg={self.scrnmsg}, scrnparam={self.scrnparam}, gfxscrnmsg={self.gfxscrnmsg}, gfxscrnparam={self.gfxscrnparam}, type={self.type})"



class SystemMsg(object):

    def __init__(self, id, UNK_0, message, group, color, sound, voice, unk_414, win, font, lftime, bkg, anim, scrnmsg, scrnparam, gfxscrnmsg, gfxscrnparam, type):
        self.id = id
        self.UNK_0 = UNK_0
        self.message = message
        self.group = group
        self.color = color
        self.sound = sound
        self.voice = voice
        self.unk_414 = unk_414
        self.win = win
        self.font = font
        self.lftime = lftime
        self.bkg = bkg
        self.anim = anim
        self.scrnmsg = scrnmsg
        self.scrnparam = scrnparam
        self.gfxscrnmsg = gfxscrnmsg
        self.gfxscrnparam = gfxscrnparam
        self.type = type

    @classmethod
    def from_string(self, line) -> 'SystemMsg':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'UNK_0', 'message', 'group', 'color', 'sound', 'voice', 'unk_414', 'win', 'font', 'lftime', 'bkg', 'anim', 'scrnmsg', 'scrnparam', 'gfxscrnmsg', 'gfxscrnparam', 'type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('UNK_0'), data.get('message'), data.get('group'), data.get('color'), data.get('sound'), data.get('voice'), data.get('unk_414'), data.get('win'), data.get('font'), data.get('lftime'), data.get('bkg'), data.get('anim'), data.get('scrnmsg'), data.get('scrnparam'), data.get('gfxscrnmsg'), data.get('gfxscrnparam'), data.get('type'))
    
    def __str__(self):
        return f"SystemMsg(id={self.id}, UNK_0={self.UNK_0}, message={self.message}, group={self.group}, color={self.color}, sound={self.sound}, voice={self.voice}, unk_414={self.unk_414}, win={self.win}, font={self.font}, lftime={self.lftime}, bkg={self.bkg}, anim={self.anim}, scrnmsg={self.scrnmsg}, scrnparam={self.scrnparam}, gfxscrnmsg={self.gfxscrnmsg}, gfxscrnparam={self.gfxscrnparam}, type={self.type})"



class Teleportlist(object):

    def __init__(self, huntingzone_id, town_id, priority, price, usable_level, usable_transfer_degree, server_range, tag_start_time, tag_end_time, tag_type, rc_zone_id):
        self.huntingzone_id = huntingzone_id
        self.town_id = town_id
        self.priority = priority
        self.price = price
        self.usable_level = usable_level
        self.usable_transfer_degree = usable_transfer_degree
        self.server_range = server_range
        self.tag_start_time = tag_start_time
        self.tag_end_time = tag_end_time
        self.tag_type = tag_type
        self.rc_zone_id = rc_zone_id

    @classmethod
    def from_string(self, line) -> 'Teleportlist':
        split_params = line.split('\t')[1:-1]
        attributes = ['huntingzone_id', 'town_id', 'priority', 'price', 'usable_level', 'usable_transfer_degree', 'server_range', 'tag_start_time', 'tag_end_time', 'tag_type', 'rc_zone_id']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('huntingzone_id'), data.get('town_id'), data.get('priority'), data.get('price'), data.get('usable_level'), data.get('usable_transfer_degree'), data.get('server_range'), data.get('tag_start_time'), data.get('tag_end_time'), data.get('tag_type'), data.get('rc_zone_id'))
    
    def __str__(self):
        return f"Teleportlist(huntingzone_id={self.huntingzone_id}, town_id={self.town_id}, priority={self.priority}, price={self.price}, usable_level={self.usable_level}, usable_transfer_degree={self.usable_transfer_degree}, server_range={self.server_range}, tag_start_time={self.tag_start_time}, tag_end_time={self.tag_end_time}, tag_type={self.tag_type}, rc_zone_id={self.rc_zone_id})"



class TimeZoneData(object):

    def __init__(self, type, field_id, name, desc, refill_item_list, fieldImage, isWorld, isPvp, isEvent, fieldInfo, is_account_share):
        self.type = type
        self.field_id = field_id
        self.name = name
        self.desc = desc
        self.refill_item_list = refill_item_list
        self.fieldImage = fieldImage
        self.isWorld = isWorld
        self.isPvp = isPvp
        self.isEvent = isEvent
        self.fieldInfo = fieldInfo
        self.is_account_share = is_account_share

    @classmethod
    def from_string(self, line) -> 'TimeZoneData':
        split_params = line.split('\t')[1:-1]
        attributes = ['type', 'field_id', 'name', 'desc', 'refill_item_list', 'fieldImage', 'isWorld', 'isPvp', 'isEvent', 'fieldInfo', 'is_account_share']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('type'), data.get('field_id'), data.get('name'), data.get('desc'), data.get('refill_item_list'), data.get('fieldImage'), data.get('isWorld'), data.get('isPvp'), data.get('isEvent'), data.get('fieldInfo'), data.get('is_account_share'))
    
    def __str__(self):
        return f"TimeZoneData(type={self.type}, field_id={self.field_id}, name={self.name}, desc={self.desc}, refill_item_list={self.refill_item_list}, fieldImage={self.fieldImage}, isWorld={self.isWorld}, isPvp={self.isPvp}, isEvent={self.isEvent}, fieldInfo={self.fieldInfo}, is_account_share={self.is_account_share})"



class TimeZoneData(object):

    def __init__(self, type, field_id, name, desc, refill_item_list, fieldImage, isWorld, isPvp, isEvent, fieldInfo, is_account_share):
        self.type = type
        self.field_id = field_id
        self.name = name
        self.desc = desc
        self.refill_item_list = refill_item_list
        self.fieldImage = fieldImage
        self.isWorld = isWorld
        self.isPvp = isPvp
        self.isEvent = isEvent
        self.fieldInfo = fieldInfo
        self.is_account_share = is_account_share

    @classmethod
    def from_string(self, line) -> 'TimeZoneData':
        split_params = line.split('\t')[1:-1]
        attributes = ['type', 'field_id', 'name', 'desc', 'refill_item_list', 'fieldImage', 'isWorld', 'isPvp', 'isEvent', 'fieldInfo', 'is_account_share']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('type'), data.get('field_id'), data.get('name'), data.get('desc'), data.get('refill_item_list'), data.get('fieldImage'), data.get('isWorld'), data.get('isPvp'), data.get('isEvent'), data.get('fieldInfo'), data.get('is_account_share'))
    
    def __str__(self):
        return f"TimeZoneData(type={self.type}, field_id={self.field_id}, name={self.name}, desc={self.desc}, refill_item_list={self.refill_item_list}, fieldImage={self.fieldImage}, isWorld={self.isWorld}, isPvp={self.isPvp}, isEvent={self.isEvent}, fieldInfo={self.fieldInfo}, is_account_share={self.is_account_share})"



class TransformData(object):

    def __init__(self, transform_id, gender, npc_id, weapon_id, transform_effect_name, return_effect_name, transform_type, character_scale, character_offset_x, character_offset_y, chatbox_skintype):
        self.transform_id = transform_id
        self.gender = gender
        self.npc_id = npc_id
        self.weapon_id = weapon_id
        self.transform_effect_name = transform_effect_name
        self.return_effect_name = return_effect_name
        self.transform_type = transform_type
        self.character_scale = character_scale
        self.character_offset_x = character_offset_x
        self.character_offset_y = character_offset_y
        self.chatbox_skintype = chatbox_skintype

    @classmethod
    def from_string(self, line) -> 'TransformData':
        split_params = line.split('\t')[1:-1]
        attributes = ['transform_id', 'gender', 'npc_id', 'weapon_id', 'transform_effect_name', 'return_effect_name', 'transform_type', 'character_scale', 'character_offset_x', 'character_offset_y', 'chatbox_skintype']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('transform_id'), data.get('gender'), data.get('npc_id'), data.get('weapon_id'), data.get('transform_effect_name'), data.get('return_effect_name'), data.get('transform_type'), data.get('character_scale'), data.get('character_offset_x'), data.get('character_offset_y'), data.get('chatbox_skintype'))
    
    def __str__(self):
        return f"TransformData(transform_id={self.transform_id}, gender={self.gender}, npc_id={self.npc_id}, weapon_id={self.weapon_id}, transform_effect_name={self.transform_effect_name}, return_effect_name={self.return_effect_name}, transform_type={self.transform_type}, character_scale={self.character_scale}, character_offset_x={self.character_offset_x}, character_offset_y={self.character_offset_y}, chatbox_skintype={self.chatbox_skintype})"



class TutorialName(object):

    def __init__(self, id, name, type, category, order_id, level, sub_name, resource, desc, display_type):
        self.id = id
        self.name = name
        self.type = type
        self.category = category
        self.order_id = order_id
        self.level = level
        self.sub_name = sub_name
        self.resource = resource
        self.desc = desc
        self.display_type = display_type

    @classmethod
    def from_string(self, line) -> 'TutorialName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'type', 'category', 'order_id', 'level', 'sub_name', 'resource', 'desc', 'display_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('type'), data.get('category'), data.get('order_id'), data.get('level'), data.get('sub_name'), data.get('resource'), data.get('desc'), data.get('display_type'))
    
    def __str__(self):
        return f"TutorialName(id={self.id}, name={self.name}, type={self.type}, category={self.category}, order_id={self.order_id}, level={self.level}, sub_name={self.sub_name}, resource={self.resource}, desc={self.desc}, display_type={self.display_type})"



class TutorialName(object):

    def __init__(self, id, name, type, category, order_id, level, sub_name, resource, desc, display_type):
        self.id = id
        self.name = name
        self.type = type
        self.category = category
        self.order_id = order_id
        self.level = level
        self.sub_name = sub_name
        self.resource = resource
        self.desc = desc
        self.display_type = display_type

    @classmethod
    def from_string(self, line) -> 'TutorialName':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'name', 'type', 'category', 'order_id', 'level', 'sub_name', 'resource', 'desc', 'display_type']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('id'), data.get('name'), data.get('type'), data.get('category'), data.get('order_id'), data.get('level'), data.get('sub_name'), data.get('resource'), data.get('desc'), data.get('display_type'))
    
    def __str__(self):
        return f"TutorialName(id={self.id}, name={self.name}, type={self.type}, category={self.category}, order_id={self.order_id}, level={self.level}, sub_name={self.sub_name}, resource={self.resource}, desc={self.desc}, display_type={self.display_type})"



class UpgradeSystem(object):

    def __init__(self, upgrade_id, upgrade_item, material_items, commission, result_item):
        self.upgrade_id = upgrade_id
        self.upgrade_item = upgrade_item
        self.material_items = material_items
        self.commission = commission
        self.result_item = result_item

    @classmethod
    def from_string(self, line) -> 'UpgradeSystem':
        split_params = line.split('\t')[1:-1]
        attributes = ['upgrade_id', 'upgrade_item', 'material_items', 'commission', 'result_item']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('upgrade_id'), data.get('upgrade_item'), data.get('material_items'), data.get('commission'), data.get('result_item'))
    
    def __str__(self):
        return f"UpgradeSystem(upgrade_id={self.upgrade_id}, upgrade_item={self.upgrade_item}, material_items={self.material_items}, commission={self.commission}, result_item={self.result_item})"



class UseCountItem(object):

    def __init__(self, item_id, reuse_delay, max_use_count, fixed_reward_order):
        self.item_id = item_id
        self.reuse_delay = reuse_delay
        self.max_use_count = max_use_count
        self.fixed_reward_order = fixed_reward_order

    @classmethod
    def from_string(self, line) -> 'UseCountItem':
        split_params = line.split('\t')[1:-1]
        attributes = ['item_id', 'reuse_delay', 'max_use_count', 'fixed_reward_order']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('item_id'), data.get('reuse_delay'), data.get('max_use_count'), data.get('fixed_reward_order'))
    
    def __str__(self):
        return f"UseCountItem(item_id={self.item_id}, reuse_delay={self.reuse_delay}, max_use_count={self.max_use_count}, fixed_reward_order={self.fixed_reward_order})"



class UsmMovieData(object):

    def __init__(self, MovieID, FileName, PosX, PosY, Width, Height, SkinType, SkipButtonType, targetAnchorPointType, clipAnchorPointType):
        self.MovieID = MovieID
        self.FileName = FileName
        self.PosX = PosX
        self.PosY = PosY
        self.Width = Width
        self.Height = Height
        self.SkinType = SkinType
        self.SkipButtonType = SkipButtonType
        self.targetAnchorPointType = targetAnchorPointType
        self.clipAnchorPointType = clipAnchorPointType

    @classmethod
    def from_string(self, line) -> 'UsmMovieData':
        split_params = line.split('\t')[1:-1]
        attributes = ['MovieID', 'FileName', 'PosX', 'PosY', 'Width', 'Height', 'SkinType', 'SkipButtonType', 'targetAnchorPointType', 'clipAnchorPointType']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('MovieID'), data.get('FileName'), data.get('PosX'), data.get('PosY'), data.get('Width'), data.get('Height'), data.get('SkinType'), data.get('SkipButtonType'), data.get('targetAnchorPointType'), data.get('clipAnchorPointType'))
    
    def __str__(self):
        return f"UsmMovieData(MovieID={self.MovieID}, FileName={self.FileName}, PosX={self.PosX}, PosY={self.PosY}, Width={self.Width}, Height={self.Height}, SkinType={self.SkinType}, SkipButtonType={self.SkipButtonType}, targetAnchorPointType={self.targetAnchorPointType}, clipAnchorPointType={self.clipAnchorPointType})"



class Variationarmoreffectgrp(AbstractItemInfo):

    def __init__(self, unk_1, unk_2, unk_3, effect_name):
        super().__init__(object_id)
        self.unk_1 = unk_1
        self.unk_2 = unk_2
        self.unk_3 = unk_3
        self.effect_name = effect_name

    @classmethod
    def from_string(cls, line) -> 'Variationarmoreffectgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['unk_1', 'unk_2', 'unk_3', 'effect_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('unk_1'), data.get('unk_2'), data.get('unk_3'), data.get('effect_name'))
    
    def __str__(self):
        return f"Variationarmoreffectgrp(unk_1={self.unk_1}, unk_2={self.unk_2}, unk_3={self.unk_3}, effect_name={self.effect_name})"



class Variationdata(object):

    def __init__(self, mineral_item_id, item_group_name, fee_item_id, fee_item_count, fee_adena, cancel_fee):
        self.mineral_item_id = mineral_item_id
        self.item_group_name = item_group_name
        self.fee_item_id = fee_item_id
        self.fee_item_count = fee_item_count
        self.fee_adena = fee_adena
        self.cancel_fee = cancel_fee

    @classmethod
    def from_string(self, line) -> 'Variationdata':
        split_params = line.split('\t')[1:-1]
        attributes = ['mineral_item_id', 'item_group_name', 'fee_item_id', 'fee_item_count', 'fee_adena', 'cancel_fee']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('mineral_item_id'), data.get('item_group_name'), data.get('fee_item_id'), data.get('fee_item_count'), data.get('fee_adena'), data.get('cancel_fee'))
    
    def __str__(self):
        return f"Variationdata(mineral_item_id={self.mineral_item_id}, item_group_name={self.item_group_name}, fee_item_id={self.fee_item_id}, fee_item_count={self.fee_item_count}, fee_adena={self.fee_adena}, cancel_fee={self.cancel_fee})"



class VariationdataFee(object):

    def __init__(self, mineral_item_id, item_group_name, fee_item_id, fee_item_count, fee_adena, cancel_fee):
        self.mineral_item_id = mineral_item_id
        self.item_group_name = item_group_name
        self.fee_item_id = fee_item_id
        self.fee_item_count = fee_item_count
        self.fee_adena = fee_adena
        self.cancel_fee = cancel_fee

    @classmethod
    def from_string(self, line) -> 'VariationdataFee':
        split_params = line.split('\t')[1:-1]
        attributes = ['mineral_item_id', 'item_group_name', 'fee_item_id', 'fee_item_count', 'fee_adena', 'cancel_fee']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('mineral_item_id'), data.get('item_group_name'), data.get('fee_item_id'), data.get('fee_item_count'), data.get('fee_adena'), data.get('cancel_fee'))
    
    def __str__(self):
        return f"VariationdataFee(mineral_item_id={self.mineral_item_id}, item_group_name={self.item_group_name}, fee_item_id={self.fee_item_id}, fee_item_count={self.fee_item_count}, fee_adena={self.fee_adena}, cancel_fee={self.cancel_fee})"



class VariationdataOption(object):

    def __init__(self, mineral_item_id, item_group_name, option_description1, option_description2, option_description3):
        self.mineral_item_id = mineral_item_id
        self.item_group_name = item_group_name
        self.option_description1 = option_description1
        self.option_description2 = option_description2
        self.option_description3 = option_description3

    @classmethod
    def from_string(self, line) -> 'VariationdataOption':
        split_params = line.split('\t')[1:-1]
        attributes = ['mineral_item_id', 'item_group_name', 'option_description1', 'option_description2', 'option_description3']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('mineral_item_id'), data.get('item_group_name'), data.get('option_description1'), data.get('option_description2'), data.get('option_description3'))
    
    def __str__(self):
        return f"VariationdataOption(mineral_item_id={self.mineral_item_id}, item_group_name={self.item_group_name}, option_description1={self.option_description1}, option_description2={self.option_description2}, option_description3={self.option_description3})"



class Variationeffectgrp(AbstractItemInfo):

    def __init__(self, quality1, quality2, enchant_min, enchant_max, effect_type, effect_name):
        super().__init__(object_id)
        self.quality1 = quality1
        self.quality2 = quality2
        self.enchant_min = enchant_min
        self.enchant_max = enchant_max
        self.effect_type = effect_type
        self.effect_name = effect_name

    @classmethod
    def from_string(cls, line) -> 'Variationeffectgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['quality1', 'quality2', 'enchant_min', 'enchant_max', 'effect_type', 'effect_name']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('quality1'), data.get('quality2'), data.get('enchant_min'), data.get('enchant_max'), data.get('effect_type'), data.get('effect_name'))
    
    def __str__(self):
        return f"Variationeffectgrp(quality1={self.quality1}, quality2={self.quality2}, enchant_min={self.enchant_min}, enchant_max={self.enchant_max}, effect_type={self.effect_type}, effect_name={self.effect_name})"



class Variationexeffectgrp(AbstractItemInfo):

    def __init__(self, unk_1, unk_2, unk_3, unk_4, unk_5):
        super().__init__(object_id)
        self.unk_1 = unk_1
        self.unk_2 = unk_2
        self.unk_3 = unk_3
        self.unk_4 = unk_4
        self.unk_5 = unk_5

    @classmethod
    def from_string(cls, line) -> 'Variationexeffectgrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['unk_1', 'unk_2', 'unk_3', 'unk_4', 'unk_5']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('unk_1'), data.get('unk_2'), data.get('unk_3'), data.get('unk_4'), data.get('unk_5'))
    
    def __str__(self):
        return f"Variationexeffectgrp(unk_1={self.unk_1}, unk_2={self.unk_2}, unk_3={self.unk_3}, unk_4={self.unk_4}, unk_5={self.unk_5})"



class VehiclePartsGrp(AbstractItemInfo):

    def __init__(self, id, actor_name, partlist, offsets, animation, serverobject, mesh, texture, spawn_sound, basic_sound, moveup_sound, movedown_sound, turn_sound, random_sound):
        super().__init__(object_id)
        self.id = id
        self.actor_name = actor_name
        self.partlist = partlist
        self.offsets = offsets
        self.animation = animation
        self.serverobject = serverobject
        self.mesh = mesh
        self.texture = texture
        self.spawn_sound = spawn_sound
        self.basic_sound = basic_sound
        self.moveup_sound = moveup_sound
        self.movedown_sound = movedown_sound
        self.turn_sound = turn_sound
        self.random_sound = random_sound

    @classmethod
    def from_string(cls, line) -> 'VehiclePartsGrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['id', 'actor_name', 'partlist', 'offsets', 'animation', 'serverobject', 'mesh', 'texture', 'spawn_sound', 'basic_sound', 'moveup_sound', 'movedown_sound', 'turn_sound', 'random_sound']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('id'), data.get('actor_name'), data.get('partlist'), data.get('offsets'), data.get('animation'), data.get('serverobject'), data.get('mesh'), data.get('texture'), data.get('spawn_sound'), data.get('basic_sound'), data.get('moveup_sound'), data.get('movedown_sound'), data.get('turn_sound'), data.get('random_sound'))
    
    def __str__(self):
        return f"VehiclePartsGrp(id={self.id}, actor_name={self.actor_name}, partlist={self.partlist}, offsets={self.offsets}, animation={self.animation}, serverobject={self.serverobject}, mesh={self.mesh}, texture={self.texture}, spawn_sound={self.spawn_sound}, basic_sound={self.basic_sound}, moveup_sound={self.moveup_sound}, movedown_sound={self.movedown_sound}, turn_sound={self.turn_sound}, random_sound={self.random_sound})"



class VirtualItemSystem(object):

    def __init__(self, index, body_part, itemlist):
        self.index = index
        self.body_part = body_part
        self.itemlist = itemlist

    @classmethod
    def from_string(self, line) -> 'VirtualItemSystem':
        split_params = line.split('\t')[1:-1]
        attributes = ['index', 'body_part', 'itemlist']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('index'), data.get('body_part'), data.get('itemlist'))
    
    def __str__(self):
        return f"VirtualItemSystem(index={self.index}, body_part={self.body_part}, itemlist={self.itemlist})"



class WeaponEnchantEffectData(object):

    def __init__(self, type, grade, group_name, radiance_effect_name, radiance_effect_show_value, radiance_effect_RGB_opacity_e1, radiance_effect_RGB_opacity_e2, radiance_effect_RGB_opacity_e3, radiance_effect_RGB_opacity_e4, radiance_effect_RGB_opacity_e5, radiance_effect_RGB_opacity_e6, radiance_effect_RGB_opacity_e7, radiance_effect_RGB_opacity_e8, radiance_effect_RGB_opacity_e9, radiance_effect_RGB_opacity_e10, radiance_effect_RGB_opacity_e11, radiance_effect_RGB_opacity_e12, radiance_effect_RGB_opacity_e13, radiance_effect_RGB_opacity_e14, radiance_effect_RGB_opacity_e15, radiance_effect_RGB_opacity_e16, radiance_effect_RGB_opacity_e17, radiance_effect_RGB_opacity_e18, radiance_effect_RGB_opacity_e19, radiance_effect_RGB_opacity_e20, radiance_effect_RGB_opacity_e21, radiance_effect_RGB_opacity_e22, radiance_effect_RGB_opacity_e23, radiance_effect_RGB_opacity_e24, radiance_effect_RGB_opacity_e25, radiance_effect_RGB_opacity_e26, radiance_effect_RGB_opacity_e27, radiance_effect_RGB_opacity_e28, radiance_effect_RGB_opacity_e29, radiance_effect_RGB_opacity_e30, sword_flow_effect_show_value, sword_flow_effect_max_particle_e1, sword_flow_effect_max_particle_e2, sword_flow_effect_max_particle_e3, sword_flow_effect_max_particle_e4, sword_flow_effect_max_particle_e5, sword_flow_effect_max_particle_e6, sword_flow_effect_max_particle_e7, sword_flow_effect_max_particle_e8, sword_flow_effect_max_particle_e9, sword_flow_effect_max_particle_e10, sword_flow_effect_max_particle_e11, sword_flow_effect_max_particle_e12, sword_flow_effect_max_particle_e13, sword_flow_effect_max_particle_e14, sword_flow_effect_max_particle_e15, sword_flow_effect_max_particle_e16, sword_flow_effect_max_particle_e17, sword_flow_effect_max_particle_e18, sword_flow_effect_max_particle_e19, sword_flow_effect_max_particle_e20, sword_flow_effect_max_particle_e21, sword_flow_effect_max_particle_e22, sword_flow_effect_max_particle_e23, sword_flow_effect_max_particle_e24, sword_flow_effect_max_particle_e25, sword_flow_effect_max_particle_e26, sword_flow_effect_max_particle_e27, sword_flow_effect_max_particle_e28, sword_flow_effect_max_particle_e29, sword_flow_effect_max_particle_e30, particle_effect_name, particle_effect_show_value):
        self.type = type
        self.grade = grade
        self.group_name = group_name
        self.radiance_effect_name = radiance_effect_name
        self.radiance_effect_show_value = radiance_effect_show_value
        self.radiance_effect_RGB_opacity_e1 = radiance_effect_RGB_opacity_e1
        self.radiance_effect_RGB_opacity_e2 = radiance_effect_RGB_opacity_e2
        self.radiance_effect_RGB_opacity_e3 = radiance_effect_RGB_opacity_e3
        self.radiance_effect_RGB_opacity_e4 = radiance_effect_RGB_opacity_e4
        self.radiance_effect_RGB_opacity_e5 = radiance_effect_RGB_opacity_e5
        self.radiance_effect_RGB_opacity_e6 = radiance_effect_RGB_opacity_e6
        self.radiance_effect_RGB_opacity_e7 = radiance_effect_RGB_opacity_e7
        self.radiance_effect_RGB_opacity_e8 = radiance_effect_RGB_opacity_e8
        self.radiance_effect_RGB_opacity_e9 = radiance_effect_RGB_opacity_e9
        self.radiance_effect_RGB_opacity_e10 = radiance_effect_RGB_opacity_e10
        self.radiance_effect_RGB_opacity_e11 = radiance_effect_RGB_opacity_e11
        self.radiance_effect_RGB_opacity_e12 = radiance_effect_RGB_opacity_e12
        self.radiance_effect_RGB_opacity_e13 = radiance_effect_RGB_opacity_e13
        self.radiance_effect_RGB_opacity_e14 = radiance_effect_RGB_opacity_e14
        self.radiance_effect_RGB_opacity_e15 = radiance_effect_RGB_opacity_e15
        self.radiance_effect_RGB_opacity_e16 = radiance_effect_RGB_opacity_e16
        self.radiance_effect_RGB_opacity_e17 = radiance_effect_RGB_opacity_e17
        self.radiance_effect_RGB_opacity_e18 = radiance_effect_RGB_opacity_e18
        self.radiance_effect_RGB_opacity_e19 = radiance_effect_RGB_opacity_e19
        self.radiance_effect_RGB_opacity_e20 = radiance_effect_RGB_opacity_e20
        self.radiance_effect_RGB_opacity_e21 = radiance_effect_RGB_opacity_e21
        self.radiance_effect_RGB_opacity_e22 = radiance_effect_RGB_opacity_e22
        self.radiance_effect_RGB_opacity_e23 = radiance_effect_RGB_opacity_e23
        self.radiance_effect_RGB_opacity_e24 = radiance_effect_RGB_opacity_e24
        self.radiance_effect_RGB_opacity_e25 = radiance_effect_RGB_opacity_e25
        self.radiance_effect_RGB_opacity_e26 = radiance_effect_RGB_opacity_e26
        self.radiance_effect_RGB_opacity_e27 = radiance_effect_RGB_opacity_e27
        self.radiance_effect_RGB_opacity_e28 = radiance_effect_RGB_opacity_e28
        self.radiance_effect_RGB_opacity_e29 = radiance_effect_RGB_opacity_e29
        self.radiance_effect_RGB_opacity_e30 = radiance_effect_RGB_opacity_e30
        self.sword_flow_effect_show_value = sword_flow_effect_show_value
        self.sword_flow_effect_max_particle_e1 = sword_flow_effect_max_particle_e1
        self.sword_flow_effect_max_particle_e2 = sword_flow_effect_max_particle_e2
        self.sword_flow_effect_max_particle_e3 = sword_flow_effect_max_particle_e3
        self.sword_flow_effect_max_particle_e4 = sword_flow_effect_max_particle_e4
        self.sword_flow_effect_max_particle_e5 = sword_flow_effect_max_particle_e5
        self.sword_flow_effect_max_particle_e6 = sword_flow_effect_max_particle_e6
        self.sword_flow_effect_max_particle_e7 = sword_flow_effect_max_particle_e7
        self.sword_flow_effect_max_particle_e8 = sword_flow_effect_max_particle_e8
        self.sword_flow_effect_max_particle_e9 = sword_flow_effect_max_particle_e9
        self.sword_flow_effect_max_particle_e10 = sword_flow_effect_max_particle_e10
        self.sword_flow_effect_max_particle_e11 = sword_flow_effect_max_particle_e11
        self.sword_flow_effect_max_particle_e12 = sword_flow_effect_max_particle_e12
        self.sword_flow_effect_max_particle_e13 = sword_flow_effect_max_particle_e13
        self.sword_flow_effect_max_particle_e14 = sword_flow_effect_max_particle_e14
        self.sword_flow_effect_max_particle_e15 = sword_flow_effect_max_particle_e15
        self.sword_flow_effect_max_particle_e16 = sword_flow_effect_max_particle_e16
        self.sword_flow_effect_max_particle_e17 = sword_flow_effect_max_particle_e17
        self.sword_flow_effect_max_particle_e18 = sword_flow_effect_max_particle_e18
        self.sword_flow_effect_max_particle_e19 = sword_flow_effect_max_particle_e19
        self.sword_flow_effect_max_particle_e20 = sword_flow_effect_max_particle_e20
        self.sword_flow_effect_max_particle_e21 = sword_flow_effect_max_particle_e21
        self.sword_flow_effect_max_particle_e22 = sword_flow_effect_max_particle_e22
        self.sword_flow_effect_max_particle_e23 = sword_flow_effect_max_particle_e23
        self.sword_flow_effect_max_particle_e24 = sword_flow_effect_max_particle_e24
        self.sword_flow_effect_max_particle_e25 = sword_flow_effect_max_particle_e25
        self.sword_flow_effect_max_particle_e26 = sword_flow_effect_max_particle_e26
        self.sword_flow_effect_max_particle_e27 = sword_flow_effect_max_particle_e27
        self.sword_flow_effect_max_particle_e28 = sword_flow_effect_max_particle_e28
        self.sword_flow_effect_max_particle_e29 = sword_flow_effect_max_particle_e29
        self.sword_flow_effect_max_particle_e30 = sword_flow_effect_max_particle_e30
        self.particle_effect_name = particle_effect_name
        self.particle_effect_show_value = particle_effect_show_value

    @classmethod
    def from_string(self, line) -> 'WeaponEnchantEffectData':
        split_params = line.split('\t')[1:-1]
        attributes = ['type', 'grade', 'group_name', 'radiance_effect_name', 'radiance_effect_show_value', 'radiance_effect_RGB_opacity_e1', 'radiance_effect_RGB_opacity_e2', 'radiance_effect_RGB_opacity_e3', 'radiance_effect_RGB_opacity_e4', 'radiance_effect_RGB_opacity_e5', 'radiance_effect_RGB_opacity_e6', 'radiance_effect_RGB_opacity_e7', 'radiance_effect_RGB_opacity_e8', 'radiance_effect_RGB_opacity_e9', 'radiance_effect_RGB_opacity_e10', 'radiance_effect_RGB_opacity_e11', 'radiance_effect_RGB_opacity_e12', 'radiance_effect_RGB_opacity_e13', 'radiance_effect_RGB_opacity_e14', 'radiance_effect_RGB_opacity_e15', 'radiance_effect_RGB_opacity_e16', 'radiance_effect_RGB_opacity_e17', 'radiance_effect_RGB_opacity_e18', 'radiance_effect_RGB_opacity_e19', 'radiance_effect_RGB_opacity_e20', 'radiance_effect_RGB_opacity_e21', 'radiance_effect_RGB_opacity_e22', 'radiance_effect_RGB_opacity_e23', 'radiance_effect_RGB_opacity_e24', 'radiance_effect_RGB_opacity_e25', 'radiance_effect_RGB_opacity_e26', 'radiance_effect_RGB_opacity_e27', 'radiance_effect_RGB_opacity_e28', 'radiance_effect_RGB_opacity_e29', 'radiance_effect_RGB_opacity_e30', 'sword_flow_effect_show_value', 'sword_flow_effect_max_particle_e1', 'sword_flow_effect_max_particle_e2', 'sword_flow_effect_max_particle_e3', 'sword_flow_effect_max_particle_e4', 'sword_flow_effect_max_particle_e5', 'sword_flow_effect_max_particle_e6', 'sword_flow_effect_max_particle_e7', 'sword_flow_effect_max_particle_e8', 'sword_flow_effect_max_particle_e9', 'sword_flow_effect_max_particle_e10', 'sword_flow_effect_max_particle_e11', 'sword_flow_effect_max_particle_e12', 'sword_flow_effect_max_particle_e13', 'sword_flow_effect_max_particle_e14', 'sword_flow_effect_max_particle_e15', 'sword_flow_effect_max_particle_e16', 'sword_flow_effect_max_particle_e17', 'sword_flow_effect_max_particle_e18', 'sword_flow_effect_max_particle_e19', 'sword_flow_effect_max_particle_e20', 'sword_flow_effect_max_particle_e21', 'sword_flow_effect_max_particle_e22', 'sword_flow_effect_max_particle_e23', 'sword_flow_effect_max_particle_e24', 'sword_flow_effect_max_particle_e25', 'sword_flow_effect_max_particle_e26', 'sword_flow_effect_max_particle_e27', 'sword_flow_effect_max_particle_e28', 'sword_flow_effect_max_particle_e29', 'sword_flow_effect_max_particle_e30', 'particle_effect_name', 'particle_effect_show_value']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('type'), data.get('grade'), data.get('group_name'), data.get('radiance_effect_name'), data.get('radiance_effect_show_value'), data.get('radiance_effect_RGB_opacity_e1'), data.get('radiance_effect_RGB_opacity_e2'), data.get('radiance_effect_RGB_opacity_e3'), data.get('radiance_effect_RGB_opacity_e4'), data.get('radiance_effect_RGB_opacity_e5'), data.get('radiance_effect_RGB_opacity_e6'), data.get('radiance_effect_RGB_opacity_e7'), data.get('radiance_effect_RGB_opacity_e8'), data.get('radiance_effect_RGB_opacity_e9'), data.get('radiance_effect_RGB_opacity_e10'), data.get('radiance_effect_RGB_opacity_e11'), data.get('radiance_effect_RGB_opacity_e12'), data.get('radiance_effect_RGB_opacity_e13'), data.get('radiance_effect_RGB_opacity_e14'), data.get('radiance_effect_RGB_opacity_e15'), data.get('radiance_effect_RGB_opacity_e16'), data.get('radiance_effect_RGB_opacity_e17'), data.get('radiance_effect_RGB_opacity_e18'), data.get('radiance_effect_RGB_opacity_e19'), data.get('radiance_effect_RGB_opacity_e20'), data.get('radiance_effect_RGB_opacity_e21'), data.get('radiance_effect_RGB_opacity_e22'), data.get('radiance_effect_RGB_opacity_e23'), data.get('radiance_effect_RGB_opacity_e24'), data.get('radiance_effect_RGB_opacity_e25'), data.get('radiance_effect_RGB_opacity_e26'), data.get('radiance_effect_RGB_opacity_e27'), data.get('radiance_effect_RGB_opacity_e28'), data.get('radiance_effect_RGB_opacity_e29'), data.get('radiance_effect_RGB_opacity_e30'), data.get('sword_flow_effect_show_value'), data.get('sword_flow_effect_max_particle_e1'), data.get('sword_flow_effect_max_particle_e2'), data.get('sword_flow_effect_max_particle_e3'), data.get('sword_flow_effect_max_particle_e4'), data.get('sword_flow_effect_max_particle_e5'), data.get('sword_flow_effect_max_particle_e6'), data.get('sword_flow_effect_max_particle_e7'), data.get('sword_flow_effect_max_particle_e8'), data.get('sword_flow_effect_max_particle_e9'), data.get('sword_flow_effect_max_particle_e10'), data.get('sword_flow_effect_max_particle_e11'), data.get('sword_flow_effect_max_particle_e12'), data.get('sword_flow_effect_max_particle_e13'), data.get('sword_flow_effect_max_particle_e14'), data.get('sword_flow_effect_max_particle_e15'), data.get('sword_flow_effect_max_particle_e16'), data.get('sword_flow_effect_max_particle_e17'), data.get('sword_flow_effect_max_particle_e18'), data.get('sword_flow_effect_max_particle_e19'), data.get('sword_flow_effect_max_particle_e20'), data.get('sword_flow_effect_max_particle_e21'), data.get('sword_flow_effect_max_particle_e22'), data.get('sword_flow_effect_max_particle_e23'), data.get('sword_flow_effect_max_particle_e24'), data.get('sword_flow_effect_max_particle_e25'), data.get('sword_flow_effect_max_particle_e26'), data.get('sword_flow_effect_max_particle_e27'), data.get('sword_flow_effect_max_particle_e28'), data.get('sword_flow_effect_max_particle_e29'), data.get('sword_flow_effect_max_particle_e30'), data.get('particle_effect_name'), data.get('particle_effect_show_value'))
    
    def __str__(self):
        return f"WeaponEnchantEffectData(type={self.type}, grade={self.grade}, group_name={self.group_name}, radiance_effect_name={self.radiance_effect_name}, radiance_effect_show_value={self.radiance_effect_show_value}, radiance_effect_RGB_opacity_e1={self.radiance_effect_RGB_opacity_e1}, radiance_effect_RGB_opacity_e2={self.radiance_effect_RGB_opacity_e2}, radiance_effect_RGB_opacity_e3={self.radiance_effect_RGB_opacity_e3}, radiance_effect_RGB_opacity_e4={self.radiance_effect_RGB_opacity_e4}, radiance_effect_RGB_opacity_e5={self.radiance_effect_RGB_opacity_e5}, radiance_effect_RGB_opacity_e6={self.radiance_effect_RGB_opacity_e6}, radiance_effect_RGB_opacity_e7={self.radiance_effect_RGB_opacity_e7}, radiance_effect_RGB_opacity_e8={self.radiance_effect_RGB_opacity_e8}, radiance_effect_RGB_opacity_e9={self.radiance_effect_RGB_opacity_e9}, radiance_effect_RGB_opacity_e10={self.radiance_effect_RGB_opacity_e10}, radiance_effect_RGB_opacity_e11={self.radiance_effect_RGB_opacity_e11}, radiance_effect_RGB_opacity_e12={self.radiance_effect_RGB_opacity_e12}, radiance_effect_RGB_opacity_e13={self.radiance_effect_RGB_opacity_e13}, radiance_effect_RGB_opacity_e14={self.radiance_effect_RGB_opacity_e14}, radiance_effect_RGB_opacity_e15={self.radiance_effect_RGB_opacity_e15}, radiance_effect_RGB_opacity_e16={self.radiance_effect_RGB_opacity_e16}, radiance_effect_RGB_opacity_e17={self.radiance_effect_RGB_opacity_e17}, radiance_effect_RGB_opacity_e18={self.radiance_effect_RGB_opacity_e18}, radiance_effect_RGB_opacity_e19={self.radiance_effect_RGB_opacity_e19}, radiance_effect_RGB_opacity_e20={self.radiance_effect_RGB_opacity_e20}, radiance_effect_RGB_opacity_e21={self.radiance_effect_RGB_opacity_e21}, radiance_effect_RGB_opacity_e22={self.radiance_effect_RGB_opacity_e22}, radiance_effect_RGB_opacity_e23={self.radiance_effect_RGB_opacity_e23}, radiance_effect_RGB_opacity_e24={self.radiance_effect_RGB_opacity_e24}, radiance_effect_RGB_opacity_e25={self.radiance_effect_RGB_opacity_e25}, radiance_effect_RGB_opacity_e26={self.radiance_effect_RGB_opacity_e26}, radiance_effect_RGB_opacity_e27={self.radiance_effect_RGB_opacity_e27}, radiance_effect_RGB_opacity_e28={self.radiance_effect_RGB_opacity_e28}, radiance_effect_RGB_opacity_e29={self.radiance_effect_RGB_opacity_e29}, radiance_effect_RGB_opacity_e30={self.radiance_effect_RGB_opacity_e30}, sword_flow_effect_show_value={self.sword_flow_effect_show_value}, sword_flow_effect_max_particle_e1={self.sword_flow_effect_max_particle_e1}, sword_flow_effect_max_particle_e2={self.sword_flow_effect_max_particle_e2}, sword_flow_effect_max_particle_e3={self.sword_flow_effect_max_particle_e3}, sword_flow_effect_max_particle_e4={self.sword_flow_effect_max_particle_e4}, sword_flow_effect_max_particle_e5={self.sword_flow_effect_max_particle_e5}, sword_flow_effect_max_particle_e6={self.sword_flow_effect_max_particle_e6}, sword_flow_effect_max_particle_e7={self.sword_flow_effect_max_particle_e7}, sword_flow_effect_max_particle_e8={self.sword_flow_effect_max_particle_e8}, sword_flow_effect_max_particle_e9={self.sword_flow_effect_max_particle_e9}, sword_flow_effect_max_particle_e10={self.sword_flow_effect_max_particle_e10}, sword_flow_effect_max_particle_e11={self.sword_flow_effect_max_particle_e11}, sword_flow_effect_max_particle_e12={self.sword_flow_effect_max_particle_e12}, sword_flow_effect_max_particle_e13={self.sword_flow_effect_max_particle_e13}, sword_flow_effect_max_particle_e14={self.sword_flow_effect_max_particle_e14}, sword_flow_effect_max_particle_e15={self.sword_flow_effect_max_particle_e15}, sword_flow_effect_max_particle_e16={self.sword_flow_effect_max_particle_e16}, sword_flow_effect_max_particle_e17={self.sword_flow_effect_max_particle_e17}, sword_flow_effect_max_particle_e18={self.sword_flow_effect_max_particle_e18}, sword_flow_effect_max_particle_e19={self.sword_flow_effect_max_particle_e19}, sword_flow_effect_max_particle_e20={self.sword_flow_effect_max_particle_e20}, sword_flow_effect_max_particle_e21={self.sword_flow_effect_max_particle_e21}, sword_flow_effect_max_particle_e22={self.sword_flow_effect_max_particle_e22}, sword_flow_effect_max_particle_e23={self.sword_flow_effect_max_particle_e23}, sword_flow_effect_max_particle_e24={self.sword_flow_effect_max_particle_e24}, sword_flow_effect_max_particle_e25={self.sword_flow_effect_max_particle_e25}, sword_flow_effect_max_particle_e26={self.sword_flow_effect_max_particle_e26}, sword_flow_effect_max_particle_e27={self.sword_flow_effect_max_particle_e27}, sword_flow_effect_max_particle_e28={self.sword_flow_effect_max_particle_e28}, sword_flow_effect_max_particle_e29={self.sword_flow_effect_max_particle_e29}, sword_flow_effect_max_particle_e30={self.sword_flow_effect_max_particle_e30}, particle_effect_name={self.particle_effect_name}, particle_effect_show_value={self.particle_effect_show_value})"



class WeaponGradeLookChange(object):

    def __init__(self, clazz, ChangeByWeaponID, ChangeByGrade):
        self.clazz = clazz
        self.ChangeByWeaponID = ChangeByWeaponID
        self.ChangeByGrade = ChangeByGrade

    @classmethod
    def from_string(self, line) -> 'WeaponGradeLookChange':
        split_params = line.split('\t')[1:-1]
        attributes = ['clazz', 'ChangeByWeaponID', 'ChangeByGrade']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('clazz'), data.get('ChangeByWeaponID'), data.get('ChangeByGrade'))
    
    def __str__(self):
        return f"WeaponGradeLookChange(clazz={self.clazz}, ChangeByWeaponID={self.ChangeByWeaponID}, ChangeByGrade={self.ChangeByGrade})"



class Weapongrp(AbstractItemInfo):

    def __init__(self, tag, object_id, drop_type, drop_anim_type, drop_radius, drop_height, drop_texture, icon, durability, weight, material_type, crystallizable, related_quest_id, color, is_attribution, icon_panel, complete_item_dropsound_type, inventory_type, body_part, handness, wp_mesh, texture, item_sound, drop_sound, equip_sound, effect, random_damage, weapon_type, crystal_type, mp_consume, soulshot_count, spiritshot_count, curvature, UNK_10, can_equip_hero, is_magic_weapon, ertheia_fist_scale, junk, Enchanted, variation_effect_type, variation_icon, ensoul_slot_count):
        super().__init__(object_id)
        self.tag = tag
        self.object_id = object_id
        self.drop_type = drop_type
        self.drop_anim_type = drop_anim_type
        self.drop_radius = drop_radius
        self.drop_height = drop_height
        self.drop_texture = drop_texture
        self.icon = icon
        self.durability = durability
        self.weight = weight
        self.material_type = material_type
        self.crystallizable = crystallizable
        self.related_quest_id = related_quest_id
        self.color = color
        self.is_attribution = is_attribution
        self.icon_panel = icon_panel
        self.complete_item_dropsound_type = complete_item_dropsound_type
        self.inventory_type = inventory_type
        self.body_part = body_part
        self.handness = handness
        self.wp_mesh = wp_mesh
        self.texture = texture
        self.item_sound = item_sound
        self.drop_sound = drop_sound
        self.equip_sound = equip_sound
        self.effect = effect
        self.random_damage = random_damage
        self.weapon_type = weapon_type
        self.crystal_type = crystal_type
        self.mp_consume = mp_consume
        self.soulshot_count = soulshot_count
        self.spiritshot_count = spiritshot_count
        self.curvature = curvature
        self.UNK_10 = UNK_10
        self.can_equip_hero = can_equip_hero
        self.is_magic_weapon = is_magic_weapon
        self.ertheia_fist_scale = ertheia_fist_scale
        self.junk = junk
        self.Enchanted = Enchanted
        self.variation_effect_type = variation_effect_type
        self.variation_icon = variation_icon
        self.ensoul_slot_count = ensoul_slot_count

    @classmethod
    def from_string(cls, line) -> 'Weapongrp':
        split_params = line.split('\t')[1:-1]
        attributes = ['tag', 'object_id', 'drop_type', 'drop_anim_type', 'drop_radius', 'drop_height', 'drop_texture', 'icon', 'durability', 'weight', 'material_type', 'crystallizable', 'related_quest_id', 'color', 'is_attribution', 'icon_panel', 'complete_item_dropsound_type', 'inventory_type', 'body_part', 'handness', 'wp_mesh', 'texture', 'item_sound', 'drop_sound', 'equip_sound', 'effect', 'random_damage', 'weapon_type', 'crystal_type', 'mp_consume', 'soulshot_count', 'spiritshot_count', 'curvature', 'UNK_10', 'can_equip_hero', 'is_magic_weapon', 'ertheia_fist_scale', 'junk', 'Enchanted', 'variation_effect_type', 'variation_icon', 'ensoul_slot_count']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return cls(data.get('tag'), data.get('object_id'), data.get('drop_type'), data.get('drop_anim_type'), data.get('drop_radius'), data.get('drop_height'), data.get('drop_texture'), data.get('icon'), data.get('durability'), data.get('weight'), data.get('material_type'), data.get('crystallizable'), data.get('related_quest_id'), data.get('color'), data.get('is_attribution'), data.get('icon_panel'), data.get('complete_item_dropsound_type'), data.get('inventory_type'), data.get('body_part'), data.get('handness'), data.get('wp_mesh'), data.get('texture'), data.get('item_sound'), data.get('drop_sound'), data.get('equip_sound'), data.get('effect'), data.get('random_damage'), data.get('weapon_type'), data.get('crystal_type'), data.get('mp_consume'), data.get('soulshot_count'), data.get('spiritshot_count'), data.get('curvature'), data.get('UNK_10'), data.get('can_equip_hero'), data.get('is_magic_weapon'), data.get('ertheia_fist_scale'), data.get('junk'), data.get('Enchanted'), data.get('variation_effect_type'), data.get('variation_icon'), data.get('ensoul_slot_count'))
    
    def __str__(self):
        return f"Weapongrp(tag={self.tag}, object_id={self.object_id}, drop_type={self.drop_type}, drop_anim_type={self.drop_anim_type}, drop_radius={self.drop_radius}, drop_height={self.drop_height}, drop_texture={self.drop_texture}, icon={self.icon}, durability={self.durability}, weight={self.weight}, material_type={self.material_type}, crystallizable={self.crystallizable}, related_quest_id={self.related_quest_id}, color={self.color}, is_attribution={self.is_attribution}, icon_panel={self.icon_panel}, complete_item_dropsound_type={self.complete_item_dropsound_type}, inventory_type={self.inventory_type}, body_part={self.body_part}, handness={self.handness}, wp_mesh={self.wp_mesh}, texture={self.texture}, item_sound={self.item_sound}, drop_sound={self.drop_sound}, equip_sound={self.equip_sound}, effect={self.effect}, random_damage={self.random_damage}, weapon_type={self.weapon_type}, crystal_type={self.crystal_type}, mp_consume={self.mp_consume}, soulshot_count={self.soulshot_count}, spiritshot_count={self.spiritshot_count}, curvature={self.curvature}, UNK_10={self.UNK_10}, can_equip_hero={self.can_equip_hero}, is_magic_weapon={self.is_magic_weapon}, ertheia_fist_scale={self.ertheia_fist_scale}, junk={self.junk}, Enchanted={self.Enchanted}, variation_effect_type={self.variation_effect_type}, variation_icon={self.variation_icon}, ensoul_slot_count={self.ensoul_slot_count})"

    def get_item_type(self):
        return self.weapon_type

    def get_material(self):
        return self.material_type

    def get_weight(self):
        return self.weight

    def get_consume_type(self):
        return "EQUIP"

    def get_icon(self):
        return self.icon

class WeaponLookChangeEffectGroup(object):

    def __init__(self, name, item_group):
        self.name = name
        self.item_group = item_group

    @classmethod
    def from_string(self, line) -> 'WeaponLookChangeEffectGroup':
        split_params = line.split('\t')[1:-1]
        attributes = ['name', 'item_group']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('name'), data.get('item_group'))
    
    def __str__(self):
        return f"WeaponLookChangeEffectGroup(name={self.name}, item_group={self.item_group})"



class WorldCastleWarMapData(object):

    def __init__(self, npc_type, class_id, tier, loc):
        self.npc_type = npc_type
        self.class_id = class_id
        self.tier = tier
        self.loc = loc

    @classmethod
    def from_string(self, line) -> 'WorldCastleWarMapData':
        split_params = line.split('\t')[1:-1]
        attributes = ['npc_type', 'class_id', 'tier', 'loc']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('npc_type'), data.get('class_id'), data.get('tier'), data.get('loc'))
    
    def __str__(self):
        return f"WorldCastleWarMapData(npc_type={self.npc_type}, class_id={self.class_id}, tier={self.tier}, loc={self.loc})"



class ZoneName(object):

    def __init__(self, ID, MapX, MapY, Top, Bottom, Name, TownBtnLocX, TownBtnLocY, TownMapX, TownMapY, TownMapWidth, TownMapHeight, TownMapScale, TownMapTex, Color, Continent, CurrentLayer, TotalLayers, TownCenterX, TownCenterY, radarhide):
        self.ID = ID
        self.MapX = MapX
        self.MapY = MapY
        self.Top = Top
        self.Bottom = Bottom
        self.Name = Name
        self.TownBtnLocX = TownBtnLocX
        self.TownBtnLocY = TownBtnLocY
        self.TownMapX = TownMapX
        self.TownMapY = TownMapY
        self.TownMapWidth = TownMapWidth
        self.TownMapHeight = TownMapHeight
        self.TownMapScale = TownMapScale
        self.TownMapTex = TownMapTex
        self.Color = Color
        self.Continent = Continent
        self.CurrentLayer = CurrentLayer
        self.TotalLayers = TotalLayers
        self.TownCenterX = TownCenterX
        self.TownCenterY = TownCenterY
        self.radarhide = radarhide

    @classmethod
    def from_string(self, line) -> 'ZoneName':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'MapX', 'MapY', 'Top', 'Bottom', 'Name', 'TownBtnLocX', 'TownBtnLocY', 'TownMapX', 'TownMapY', 'TownMapWidth', 'TownMapHeight', 'TownMapScale', 'TownMapTex', 'Color', 'Continent', 'CurrentLayer', 'TotalLayers', 'TownCenterX', 'TownCenterY', 'radarhide']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('MapX'), data.get('MapY'), data.get('Top'), data.get('Bottom'), data.get('Name'), data.get('TownBtnLocX'), data.get('TownBtnLocY'), data.get('TownMapX'), data.get('TownMapY'), data.get('TownMapWidth'), data.get('TownMapHeight'), data.get('TownMapScale'), data.get('TownMapTex'), data.get('Color'), data.get('Continent'), data.get('CurrentLayer'), data.get('TotalLayers'), data.get('TownCenterX'), data.get('TownCenterY'), data.get('radarhide'))
    
    def __str__(self):
        return f"ZoneName(ID={self.ID}, MapX={self.MapX}, MapY={self.MapY}, Top={self.Top}, Bottom={self.Bottom}, Name={self.Name}, TownBtnLocX={self.TownBtnLocX}, TownBtnLocY={self.TownBtnLocY}, TownMapX={self.TownMapX}, TownMapY={self.TownMapY}, TownMapWidth={self.TownMapWidth}, TownMapHeight={self.TownMapHeight}, TownMapScale={self.TownMapScale}, TownMapTex={self.TownMapTex}, Color={self.Color}, Continent={self.Continent}, CurrentLayer={self.CurrentLayer}, TotalLayers={self.TotalLayers}, TownCenterX={self.TownCenterX}, TownCenterY={self.TownCenterY}, radarhide={self.radarhide})"



class ZoneName(object):

    def __init__(self, ID, MapX, MapY, Top, Bottom, Name, TownBtnLocX, TownBtnLocY, TownMapX, TownMapY, TownMapWidth, TownMapHeight, TownMapScale, TownMapTex, Color, Continent, CurrentLayer, TotalLayers, TownCenterX, TownCenterY, radarhide):
        self.ID = ID
        self.MapX = MapX
        self.MapY = MapY
        self.Top = Top
        self.Bottom = Bottom
        self.Name = Name
        self.TownBtnLocX = TownBtnLocX
        self.TownBtnLocY = TownBtnLocY
        self.TownMapX = TownMapX
        self.TownMapY = TownMapY
        self.TownMapWidth = TownMapWidth
        self.TownMapHeight = TownMapHeight
        self.TownMapScale = TownMapScale
        self.TownMapTex = TownMapTex
        self.Color = Color
        self.Continent = Continent
        self.CurrentLayer = CurrentLayer
        self.TotalLayers = TotalLayers
        self.TownCenterX = TownCenterX
        self.TownCenterY = TownCenterY
        self.radarhide = radarhide

    @classmethod
    def from_string(self, line) -> 'ZoneName':
        split_params = line.split('\t')[1:-1]
        attributes = ['ID', 'MapX', 'MapY', 'Top', 'Bottom', 'Name', 'TownBtnLocX', 'TownBtnLocY', 'TownMapX', 'TownMapY', 'TownMapWidth', 'TownMapHeight', 'TownMapScale', 'TownMapTex', 'Color', 'Continent', 'CurrentLayer', 'TotalLayers', 'TownCenterX', 'TownCenterY', 'radarhide']
        data = {attr: split_params[index].split('=')[1] for index, attr in enumerate(attributes)}
        return self(data.get('ID'), data.get('MapX'), data.get('MapY'), data.get('Top'), data.get('Bottom'), data.get('Name'), data.get('TownBtnLocX'), data.get('TownBtnLocY'), data.get('TownMapX'), data.get('TownMapY'), data.get('TownMapWidth'), data.get('TownMapHeight'), data.get('TownMapScale'), data.get('TownMapTex'), data.get('Color'), data.get('Continent'), data.get('CurrentLayer'), data.get('TotalLayers'), data.get('TownCenterX'), data.get('TownCenterY'), data.get('radarhide'))
    
    def __str__(self):
        return f"ZoneName(ID={self.ID}, MapX={self.MapX}, MapY={self.MapY}, Top={self.Top}, Bottom={self.Bottom}, Name={self.Name}, TownBtnLocX={self.TownBtnLocX}, TownBtnLocY={self.TownBtnLocY}, TownMapX={self.TownMapX}, TownMapY={self.TownMapY}, TownMapWidth={self.TownMapWidth}, TownMapHeight={self.TownMapHeight}, TownMapScale={self.TownMapScale}, TownMapTex={self.TownMapTex}, Color={self.Color}, Continent={self.Continent}, CurrentLayer={self.CurrentLayer}, TotalLayers={self.TotalLayers}, TownCenterX={self.TownCenterX}, TownCenterY={self.TownCenterY}, radarhide={self.radarhide})"


