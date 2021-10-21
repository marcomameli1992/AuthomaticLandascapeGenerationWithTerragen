import xml.etree.ElementTree as ET
import random
import json
import basicComponent.global_value as common_values
import logging

#%% define logging
LOGGER = logging.getLogger("WATER")

def change_fractal_water(tags_root: ET.Element, global_values: dict, attribute='Lake') -> ET.Element:
    LOGGER.info(' change_fractal_water function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_water_path'], 'r') as range_file:
        ranges = json.load(range_file)
    lake_ranges = ranges['lake']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))  # at least one fractal power shader has to be active for the terrain generation
    level = str(random.randint(lake_ranges['water_level_minimum'], lake_ranges['water_level_maximum']))
    tag.attrib['water_level'] = level
    tag.attrib['centre'] = str(random.randint(0, 1)) + level + str(random.randint(0, 1))
    tag.attrib['max_radius'] = '10000'
    LOGGER.info(' change_fractal_water water_level value: ' + tag.attrib['water_level'])
    LOGGER.info(' change_fractal_water centre value: ' + tag.attrib['centre'])
    LOGGER.info(' change_fractal_water max_radius value: ' + tag.attrib['max_radius'])
    return tags_root