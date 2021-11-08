import xml.etree.ElementTree as ET
import random
import json
import numpy as np
import logging

#%% define logging
LOGGER = logging.getLogger("TERRAIN2")

def change_fractal_terrain(tags_root: ET.Element, global_values: dict, attribute='BasicTerrain') -> ET.Element:
    LOGGER.info(' change_fractal_terrain function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_terrain_path'], 'r') as range_file:
        ranges = json.load(range_file)
    fractal_terrain_ranges = ranges['fractal_terrain']

    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = '1'
    tag.attrib['seed'] = str(int(random.random()))

    tag.attrib['displacement_direction'] = '1'
    tag.attrib['displacement_amplitude'] = str(random.uniform(fractal_terrain_ranges['displacement_altitude_minimum'],
                                                              fractal_terrain_ranges['displacement_altitude_maximum']))
    tag.attrib[
        'displacement_offset'] = "0"
    tag.attrib['displacement_roughness'] = str(random.uniform(fractal_terrain_ranges['displacement_roughness_minimum'],
                                                              fractal_terrain_ranges['displacement_roughness_maximum']))
    tag.attrib['displacement_spike_limit'] = str(
        random.uniform(fractal_terrain_ranges['displacement_spike_limit_minimum'],
                       fractal_terrain_ranges['displacement_spike_limit_maximum']))
    tag.attrib['continue_spike_limit'] = '1'
    tag.attrib['adjust_coastline'] = '1'
    tag.attrib['coastline_altitude'] = str(random.uniform(fractal_terrain_ranges['coastline_altitude_minimum'],
                                                          fractal_terrain_ranges['coastline_altitute_maximum']))
    tag.attrib['coastline_smoothing'] = str(random.uniform(fractal_terrain_ranges['coastline_smoothing_minimum'],
                                                           fractal_terrain_ranges['coastline_smoothing_maximum']))

    LOGGER.info(' change_fractal_terrain displacement_amplitude value: ' + tag.attrib['displacement_amplitude'])
    LOGGER.info(' change_fractal_terrain displacement_offset value: ' + tag.attrib['displacement_offset'])
    LOGGER.info(' change_fractal_terrain displacement_roughness value: ' + tag.attrib['displacement_roughness'])
    LOGGER.info(' change_fractal_terrain displacement_spike_limit value: ' + tag.attrib['displacement_spike_limit'])
    LOGGER.info(' change_fractal_terrain coastline_altitude value: ' + tag.attrib['coastline_altitude'])
    LOGGER.info(' change_fractal_terrain noise_flavour value: ' + tag.attrib['noise_flavour'])
    LOGGER.info(' change_fractal_terrain ridge_smoothing value: ' + tag.attrib['ridge_smoothing'])
    LOGGER.info(' change_fractal_terrain gully_smoothing value: ' + tag.attrib['gully_smoothing'])
    LOGGER.info(' change_fractal_terrain noise_variation value: ' + tag.attrib['noise_variation'])
    LOGGER.info(' change_fractal_terrain variation_method value: ' + tag.attrib['variation_method'])
    LOGGER.info(' change_fractal_terrain better_colour_continuity value: ' + tag.attrib['better_colour_continuity'])
    LOGGER.info(
        ' change_fractal_terrain better_displacement_continuity value: ' + tag.attrib['better_displacement_continuity'])
    return tags_root