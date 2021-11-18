import xml.etree.ElementTree as ET
import random
import json
import numpy as np
import logging

#%% define logging
LOGGER = logging.getLogger("POPULATOR")

def change_trees_population(tags_root: ET.Element, global_values: dict, attribute="TreesOBJ") -> ET.Element:
    LOGGER.info(' change_treese_populator function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    with open(global_values['ranges_populator_path'], 'r') as range_file:
        ranges = json.load(range_file)
    populator_ranges = ranges['trees']

    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['area_length_a'] = str(random.uniform(populator_ranges['area_length_a_minimum'],
                                                     populator_ranges['area_length_a_maximum']))
    tag.attrib['area_length_b'] = str(random.uniform(populator_ranges['area_length_b_minimum'],
                                                     populator_ranges['area_length_b_maximum']))
    tag.attrib['object_spacing_xz'] = ' '.join(map(str, list(np.random.uniform(
        low=populator_ranges['object_spacing_xz_minimum'],
        high=populator_ranges['object_spacing_xz_maximum'], size=3))))
    tag.attrib['minimum_scale'] = str(random.uniform(populator_ranges['minimum_scale_minimum'],
                                                     populator_ranges['minimum_scale_maximum']))
    tag.attrib['maximum_scale'] = str(random.uniform(populator_ranges['maximum_scale_minimum'],
                                                     populator_ranges['maximum_scale_maximum']))
    tag.attrib['diffuse_colour_multiplier'] = str(random.uniform(populator_ranges['diffuse_colour_multiplier_minimum'],
                                                                 populator_ranges['diffuse_colour_multiplier_maximum']))
    tag.attrib['luminosity_multiplier'] = str(random.uniform(populator_ranges['luminosity_multiplier_minimum'],
                                                             populator_ranges['luminosity_multiplier_maximum']))
    LOGGER.info(' change_treese_populator area_length_a value: ' + tag.attrib['area_length_a'])
    LOGGER.info(' change_treese_populator area_length_b value: ' + tag.attrib['area_length_b'])
    LOGGER.info(' change_treese_populator object_spacing_xz value: ' + tag.attrib['object_spacing_xz'])
    LOGGER.info(' change_treese_populator minimum_scale value: ' + tag.attrib['minimum_scale'])
    LOGGER.info(' change_treese_populator diffuse_colour_multiplier value: ' + tag.attrib['diffuse_colour_multiplier'])
    LOGGER.info(' change_treese_populator luminosity_multiplier value: ' + tag.attrib['luminosity_multiplier'])
    return tags_root

def change_grass_population(tags_root: ET.Element, global_values: dict, attribute="GrassOBJ") -> ET.Element:
    LOGGER.info(' change_grass_population function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    with open(global_values['ranges_populator_path'], 'r') as range_file:
        ranges = json.load(range_file)
    populator_ranges = ranges['grass']

    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['area_length_a'] = str(random.uniform(populator_ranges['area_length_a_minimum'],
                                                     populator_ranges['area_length_a_maximum']))
    tag.attrib['area_length_b'] = str(random.uniform(populator_ranges['area_length_b_minimum'],
                                                     populator_ranges['area_length_b_maximum']))
    tag.attrib['object_spacing_xz'] = ' '.join(map(str, list(np.random.uniform(
        low=populator_ranges['object_spacing_xz_minimum'],
        high=populator_ranges['object_spacing_xz_maximum'], size=3))))
    tag.attrib['minimum_scale'] = str(random.uniform(populator_ranges['minimum_scale_minimum'],
                                                     populator_ranges['minimum_scale_maximum']))
    tag.attrib['maximum_scale'] = str(random.uniform(populator_ranges['maximum_scale_minimum'],
                                                     populator_ranges['maximum_scale_maximum']))
    tag.attrib['diffuse_colour_multiplier'] = str(random.uniform(populator_ranges['diffuse_colour_multiplier_minimum'],
                                                     populator_ranges['diffuse_colour_multiplier_maximum']))
    tag.attrib['luminosity_multiplier'] = str(random.uniform(populator_ranges['luminosity_multiplier_minimum'],
                                                                 populator_ranges['luminosity_multiplier_maximum']))
    LOGGER.info(' change_grass_population area_length_a value: ' + tag.attrib['area_length_a'])
    LOGGER.info(' change_grass_population area_length_b value: ' + tag.attrib['area_length_b'])
    LOGGER.info(' change_grass_population object_spacing_xz value: ' + tag.attrib['object_spacing_xz'])
    LOGGER.info(' change_grass_population minimum_scale value: ' + tag.attrib['minimum_scale'])
    LOGGER.info(' change_grass_population diffuse_colour_multiplier value: ' + tag.attrib['diffuse_colour_multiplier'])
    LOGGER.info(' change_grass_population luminosity_multiplier value: ' + tag.attrib['luminosity_multiplier'])
    return tags_root

def update_populator_position(tags_root: ET.Element, render_node:str) -> ET.Element:
    LOGGER.info(' change_populator_position function called')
    populator_tag_list = tags_root.findall(f"populator_v4")
    render_camera_name = tags_root.find(f".//*[@name='{render_node}']").attrib['camera']
    camera_tag = tags_root.find(f".//*[@name='{render_camera_name}']")

    for populator_tag in populator_tag_list:

        populator_position_list = []
        for pos, val in enumerate(camera_tag.attrib['position'].split(' ')):
            if pos == 0:
                populator_position_list.insert(pos, str(float(val) + float(populator_tag.attrib['area_length_a'])))
            if pos == 1:
                populator_position_list.insert(pos, str(float(val) + float(populator_tag.attrib['area_length_b'])))
            else:
                populator_position_list.insert(pos, val)
        populator_position = ' '.join(populator_position_list)

        populator_tag.attrib['area_centre'] = populator_position
    return tags_root
