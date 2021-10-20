import xml.etree.ElementTree as ET
import random
import json
import numpy as np
import logging

def change_trees_population(tags_root: ET.Element, global_values: dict, attribute="TreesOBJ") -> ET.Element:
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
    tag.attrib['object_spacing_xz_minimum'] = ' '.join(map(str, list(np.random.uniform(
        low=populator_ranges['object_spacing_xz_minimum'],
        high=populator_ranges['randomness_xz_maximum'], size=3))))
    tag.attrib['minimum_scale'] = str(random.uniform(populator_ranges['minimum_scale_minimum'],
                                                     populator_ranges['minimum_scale_maximum']))
    tag.attrib['maximum_scale'] = str(random.uniform(populator_ranges['maximum_scale_minimum'],
                                                     populator_ranges['maximum_scale_maximum']))
    tag.attrib['diffuse_colour_multiplier'] = str(random.uniform(populator_ranges['diffuse_colour_multiplier_minimum'],
                                                                 populator_ranges['diffuse_colour_multiplier_maximum']))
    tag.attrib['luminosity_multiplier'] = str(random.uniform(populator_ranges['luminosity_multiplier_minimum'],
                                                             populator_ranges['luminosity_multiplier_maximum']))
    return tags_root

def change_grass_population(tags_root: ET.Element, global_values: dict, attribute="GrassOBJ") -> ET.Element:
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
    tag.attrib['object_spacing_xz_minimum'] = ' '.join(map(str, list(np.random.uniform(
        low=populator_ranges['object_spacing_xz_minimum'],
        high=populator_ranges['randomness_xz_maximum'], size=3))))
    tag.attrib['minimum_scale'] = str(random.uniform(populator_ranges['minimum_scale_minimum'],
                                                     populator_ranges['minimum_scale_maximum']))
    tag.attrib['maximum_scale'] = str(random.uniform(populator_ranges['maximum_scale_minimum'],
                                                     populator_ranges['maximum_scale_maximum']))
    tag.attrib['diffuse_colour_multiplier'] = str(random.uniform(populator_ranges['diffuse_colour_multiplier_minimum'],
                                                     populator_ranges['diffuse_colour_multiplier_maximum']))
    tag.attrib['luminosity_multiplier'] = str(random.uniform(populator_ranges['luminosity_multiplier_minimum'],
                                                                 populator_ranges['luminosity_multiplier_maximum']))
    return tags_root