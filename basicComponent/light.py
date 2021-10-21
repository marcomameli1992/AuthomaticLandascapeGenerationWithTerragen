import xml.etree.ElementTree as ET
import random
import json
import basicComponent.global_value as common_values
import logging

#%% define logging
LOGGER = logging.getLogger("LIGHT")

def change_sunlight(tags_root: ET.Element, global_values: dict, attribute="Sun") -> ET.Element:
    LOGGER.info(' change_sunlight function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_light_path'], 'r') as range_file:
        ranges = json.load(range_file)
    sunlight_ranges = ranges['sunlight']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = "1" # the sunlight has to be active otherwise the render is dark
    #tag.attrib['colour'] = '1 5 0'
    tag.attrib['light_surfaces'] = '1'  # or 1
    tag.attrib['light_atmosphere'] = '1'  # or 1
    tag.attrib['heading'] = str(random.uniform(sunlight_ranges['heading_minimum'], sunlight_ranges['heading_maximum'])) # degrees 0 for North 90 for Est
    tag.attrib['elevation'] = str(random.uniform(sunlight_ranges['elevation_minimum'], sunlight_ranges['elevation_maximum'])) # 0 is the horizon and 90 is the overhead
    tag.attrib['strength'] = str(random.uniform(sunlight_ranges['strenght_minimum'], sunlight_ranges['strenght_maximum']))  # the power of the sunlight maximum is 5 ( better integer value step)
    tag.attrib['cast_shadow'] = '1' # or 0 to activate or not
    tag.attrib['shadow_onSurfaces'] = '1' # or 0 to activate or not
    tag.attrib['shadow_of_atmosphere'] = '1'
    tag.attrib['soft_shadow'] = '1'
    tag.attrib['soft_shadow_diameter'] = '0'  # TBD degrees
    tag.attrib['soft_shadow_samples'] = '4'
    tag.attrib['soft_shadow_samples_jitter'] = '0'
    tag.attrib['glow_in_atmosphere'] = '1'
    tag.attrib['specular_highlights'] = '0' # or 0 to activate or not
    tag.attrib['visible_disc'] = '1' # or 0 to activate or not
    tag.attrib['angular_diameter'] = '1' # the size of the disk
    LOGGER.info(' change_sunlight heading value: ' + tag.attrib['heading'])
    LOGGER.info(' change_sunlight elevation value: ' + tag.attrib['elevation'])
    LOGGER.info(' change_sunlight strength value: ' + tag.attrib['strength'])
    return tags_root

def change_environmental(tags_root: ET.Element,  global_values: dict, attribute="Enviro light") -> ET.Element:
    LOGGER.info(' change_environmental function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_light_path'], 'r') as range_file:
        ranges = json.load(range_file)
    environmental_ranges = ranges['environmental_light']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['global_strength_on_surfaces'] = str(random.uniform(environmental_ranges['global_strength_on_surfaces_minimum'], environmental_ranges['global_strength_on_surfaces_minimum']))
    tag.attrib['global_strength_in_atmosphere'] = str(random.uniform(environmental_ranges['global_strength_in_atmosphere_minimum'], environmental_ranges['global_strength_in_atmosphere_maximum']))
    LOGGER.info(' change_environmental global_strength_on_surfaces value: ' + tag.attrib['global_strength_on_surfaces'])
    LOGGER.info(' change_environmental global_strength_in_atmosphere value: ' + tag.attrib['global_strength_in_atmosphere'])
    return tags_root