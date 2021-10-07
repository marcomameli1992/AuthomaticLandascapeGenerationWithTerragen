import xml.etree.ElementTree as ET
import random
import os
import json
import numpy as np

range_value_path = os.path.join('..', 'basicComponent', 'ranges', 'water.json')

def change_fractal_terrain(tags_root: ET.Element, attribute='Lake') -> ET.Element:
    # Opening the range file
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    lake_ranges = ranges['lake']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = '1'  # at least one fractal power shader has to be active for the terrain generation
    level = str(random.randint(lake_ranges['water_level_minimum'], lake_ranges['water_level_maximum']))
    tag.attrib['water_level'] = level
    tag.attrib['centre'] = str(random.randint(0, 1)) + level + str(random.randint(0, 1))
    tag.attrib['max_radius'] = '10000'
    return tags_root