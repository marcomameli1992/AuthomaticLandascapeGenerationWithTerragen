import xml.etree.ElementTree as ET
import random
import json
import numpy as np

import logging

#%% define logging
LOGGER = logging.getLogger("SHADER2")

def change_fractal_shader(tags_root: ET.Element, global_values: dict, colour_attribute:str='BaseColours',
                          terrain_attribute:str='') -> ET.Element:
    LOGGER.info(' change_fractal_shader function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_shader_path'], 'r') as range_file:
        ranges = json.load(range_file)
    fractal_colour_ranges = ranges['fractal_colours']
    tag = tags_root.find(f".//*[@name='{colour_attribute}']")
    tag.attrib['seed'] = str(int(random.random()))
    LOGGER.info(' change_fractal_shader high_colour value: ' + tag.attrib['high_colour'])
    LOGGER.info(' change_fractal_shader low_colour value: ' + tag.attrib['low_colour'])
    LOGGER.info(' change_fractal_shader colour_contrast value: ' + tag.attrib['colour_contrast'])
    LOGGER.info(' change_fractal_shader clamp_low_colour value: ' + tag.attrib['clamp_low_colour'])
    return tags_root