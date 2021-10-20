import xml.etree.ElementTree as ET
import random
import json
import basicComponent.values as common_values

def change_fractal_water(tags_root: ET.Element, attribute='Lake') -> ET.Element:
    if common_values.use_seed:
        random.seed(common_values.seed, version=2)
    # Opening the range file
    with open(common_values.ranges_water_path, 'r') as range_file:
        ranges = json.load(range_file)
    lake_ranges = ranges['lake']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = '1'  # at least one fractal power shader has to be active for the terrain generation
    level = str(random.randint(lake_ranges['water_level_minimum'], lake_ranges['water_level_maximum']))
    tag.attrib['water_level'] = level
    tag.attrib['centre'] = str(random.randint(0, 1)) + level + str(random.randint(0, 1))
    tag.attrib['max_radius'] = '10000'
    return tags_root