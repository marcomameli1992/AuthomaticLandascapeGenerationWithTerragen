import xml.etree.ElementTree as ET
import random
import json
import numpy as np

import logging

#%% define logging
LOGGER = logging.getLogger("SHADER")

def change_fractal_shader(tags_root: ET.Element, global_values: dict, attribute='BaseColours') -> ET.Element:
    '''

    :param tags_root:
    :param attribute:
    :return:
    '''
    LOGGER.info(' change_fractal_shader function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_shader_path'], 'r') as range_file:
        ranges = json.load(range_file)
    fractal_colour_ranges = ranges['fractal_colours']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = "1"  # One shader has to be activated
    tag.attrib['seed'] = str(int(random.random()))
    # SCALE changes
    # tag.attrib['feature_scale'] = '1250'
    # tag.attrib['lead-in_scale'] = '120'
    # tag.attrib['smallest_scale'] = '25'
    # SCALE-NOISE changes
    # tag.attrib['noise_octaves'] = '4'
    # tag.attrib['obey_smoothing_filter'] = '1'
    # tag.attrib[
    #     'noise_stretch_XYZ'] = '3 0 2'
    # COLOR changes
    tag.attrib['apply_high_colour'] = '1'
    high_colour1 = str(fractal_colour_ranges['high_colour_R_1']) + " " + str(fractal_colour_ranges['high_colour_G_1']) + " " + str(fractal_colour_ranges['high_colour_B_1'])
    high_colour2 = str(fractal_colour_ranges['high_colour_R_2']) + " " + str(fractal_colour_ranges['high_colour_G_2']) + " " + str(fractal_colour_ranges['high_colour_B_2'])
    high_colour3 = str(fractal_colour_ranges['high_colour_R_3']) + " " + str(fractal_colour_ranges['high_colour_G_3']) + " " + str(fractal_colour_ranges['high_colour_B_3'])
    high_colours = [high_colour1, high_colour2, high_colour3]
    tag.attrib['high_colour'] = random.choice(high_colours)
    low_colour1 = str(fractal_colour_ranges['low_colour_R_1']) + " " + str(
        fractal_colour_ranges['low_colour_G_1']) + " " + str(fractal_colour_ranges['low_colour_B_1'])
    low_colour2 = str(fractal_colour_ranges['low_colour_R_2']) + " " + str(
        fractal_colour_ranges['low_colour_G_2']) + " " + str(fractal_colour_ranges['low_colour_B_2'])
    low_colours = [low_colour1, low_colour2]
    tag.attrib['apply_low_colour'] = '1'
    tag.attrib['low_colour'] = random.choice(high_colours)
    tag.attrib['colour_contrast'] = str(random.uniform(fractal_colour_ranges['colour_contrast_minimum'], fractal_colour_ranges['colour_contrast_maximum']))
    tag.attrib['colour_roughness'] = str(random.uniform(fractal_colour_ranges['colour_roughness_minimum'], fractal_colour_ranges['colour_roughness_maximum']))
    tag.attrib['clamp_high_colour'] = str(random.randint(0, 1))
    tag.attrib['clamp_low_colour'] = str(random.randint(0, 1))
    LOGGER.info(' change_fractal_shader high_colour value: ' + tag.attrib['high_colour'])
    LOGGER.info(' change_fractal_shader low_colour value: ' + tag.attrib['low_colour'])
    LOGGER.info(' change_fractal_shader colour_contrast value: ' + tag.attrib['colour_contrast'])
    LOGGER.info(' change_fractal_shader clamp_low_colour value: ' + tag.attrib['clamp_low_colour'])
    return tags_root

def change_surface_shader(tags_root: ET.Element, global_values: dict, attribute="Grass") -> ET.Element:
    LOGGER.info(' change_surface_shader function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_shader_path'], 'r') as range_file:
        ranges = json.load(range_file)
    surface_colour_ranges = ranges['surface_colours']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['apply_colour'] = '1'
    surface_colour1 = str(surface_colour_ranges['diffuse_colour_R_1']) + " " + str(
        surface_colour_ranges['diffuse_colour_G_1']) + " " + str(surface_colour_ranges['diffuse_colour_B_1'])
    surface_colour2 = str(surface_colour_ranges['diffuse_colour_R_2']) + " " + str(
        surface_colour_ranges['diffuse_colour_G_2']) + " " + str(surface_colour_ranges['diffuse_colour_B_2'])
    surface_colour3 = str(surface_colour_ranges['diffuse_colour_R_3']) + " " + str(
        surface_colour_ranges['diffuse_colour_G_2']) + " " + str(surface_colour_ranges['diffuse_colour_B_3'])
    high_colours = [surface_colour1, surface_colour2, surface_colour3]
    tag.attrib['diffuse_colour'] = random.choice(high_colours)
    tag.attrib['displacement_direction'] = str(random.randint(0, 1))
    # tag.attrib['displacement_multiplier'] = '25'
    # tag.attrib['smoothing_effect'] = '4'
    # tag.attrib['smoothing_ammount'] = '5'
    # tag.attrib['coverage'] = '3'
    tag.attrib['limit_maximum_altitude'] = '1'
    tag.attrib['maximum_altitude'] = str(random.uniform(surface_colour_ranges['maximum_altitude_minimum'], surface_colour_ranges['maximum_altitude_maximum']))
    tag.attrib['max_alt_fuzzy_zone'] = str(random.uniform(surface_colour_ranges['max_alt_fuzzy_zone_minimum'], surface_colour_ranges['max_alt_fuzzi_zone_maximum']))
    tag.attrib['limit_minimum_altitude'] = str(random.randint(0, 1))
    tag.attrib['minimum_altitude'] = str(random.uniform(surface_colour_ranges['minimum_altitude_minimum'], surface_colour_ranges['minimum_altitude_maximum']))
    tag.attrib['min_alt_fuzzy_zone'] = str(random.uniform(surface_colour_ranges['min_alt_fuzzy_zone_mimum'], surface_colour_ranges['min_alt_fuzzy_zone_maximum']))
    tag.attrib['limit_maximum_slope'] = str(random.randint(0, 1))
    tag.attrib['maximum_slpoe_angle'] = str(random.uniform(surface_colour_ranges['maximum_slope_angle_minimum'], surface_colour_ranges['maximum_slope_angle_maximum']))
    tag.attrib['max_slope_fuzzy_zone'] = str(random.uniform(surface_colour_ranges['max_slope_fuzzy_zone_minimum'], surface_colour_ranges['max_slope_fuzzy_zone_maximum']))
    tag.attrib['limit_minimum_slope'] = str(random.randint(0, 1))
    tag.attrib['minimum_slpoe_angle'] = str(random.uniform(surface_colour_ranges['minimum_slope_angle_minimum'], surface_colour_ranges['minimum_slope_angle_maximum']))
    tag.attrib['min_slope_fuzzy_zone'] = str(random.uniform(surface_colour_ranges['min_slope_fuzzy_zone_minimum'], surface_colour_ranges['min_slope_fuzzy_zone_maximum']))
    tag.attrib['slope_key'] = str(random.randint(0, 2)) # it has three values
    tag.attrib['use_y_for_slope'] = str(random.randint(0, 1))
    tag.attrib['intersection_underlying'] = str(random.randint(0, 1))
    tag.attrib['intersect_mode'] = str(random.randint(0, 2))
    tag.attrib['intersection_zone'] = str(random.uniform(surface_colour_ranges['intersection_zone_minimum'], surface_colour_ranges['intersection_zone_maximum']))
    tag.attrib['intersection_shift'] = str(random.uniform(surface_colour_ranges['intersection_shift_minimum'], surface_colour_ranges['intersection_shift_maximum']))
    tag.attrib['min_intersection_shift'] = str(random.uniform(surface_colour_ranges['min_intersection_shift_minimum'], surface_colour_ranges['min_intersection_shift_minimum']))
    LOGGER.info(' change_surface_shader diffuse_colour value: ' + tag.attrib['diffuse_colour'])
    LOGGER.info(' change_surface_shader maximum_altitude value: ' + tag.attrib['maximum_altitude'])
    LOGGER.info(' change_surface_shader max_alt_fuzzy_zone value: ' + tag.attrib['max_alt_fuzzy_zone'])
    LOGGER.info(' change_surface_shader minimum_altitude value: ' + tag.attrib['minimum_altitude'])
    LOGGER.info(' change_surface_shader min_alt_fuzzy_zone value: ' + tag.attrib['min_alt_fuzzy_zone'])
    LOGGER.info(' change_surface_shader limit_maximum_slope value: ' + tag.attrib['limit_maximum_slope'])
    LOGGER.info(' change_surface_shader max_slope_fuzzy_zone value: ' + tag.attrib['max_slope_fuzzy_zone'])
    LOGGER.info(' change_surface_shader limit_minimum_slope value: ' + tag.attrib['limit_minimum_slope'])
    LOGGER.info(' change_surface_shader minimum_slpoe_angle value: ' + tag.attrib['minimum_slpoe_angle'])
    LOGGER.info(' change_surface_shader min_slope_fuzzy_zone value: ' + tag.attrib['min_slope_fuzzy_zone'])
    LOGGER.info(' change_surface_shader max_alt_fuzzy_zone value: ' + tag.attrib['max_alt_fuzzy_zone'])
    LOGGER.info(' change_surface_shader intersection_zone value: ' + tag.attrib['intersection_zone'])
    LOGGER.info(' change_surface_shader intersection_shift value: ' + tag.attrib['intersection_shift'])
    LOGGER.info(' change_surface_shader min_intersection_shift value: ' + tag.attrib['min_intersection_shift'])
    return tags_root

def change_twist_shader(tags_root: ET.Element, global_values: dict, attribute="TwistShear") -> ET.Element:
    LOGGER.info(' change_twist_shader function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_shader_path'], 'r') as range_file:
        ranges = json.load(range_file)
    twist_ranges = ranges['twist_share']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['lean_factor'] = str(random.uniform(twist_ranges['lean_factor_minimum'], twist_ranges['lean_factor_maximum']))
    tag.attrib['lean_direction'] = ' '.join(map(str, list(np.random.randint(low=0, high=1e+5, size=3))))
    tag.attrib['base_altitude'] = str(random.uniform(twist_ranges['lean_factor_minimum'], twist_ranges['lean_factor_maximum']))
    LOGGER.info(' change_twist_shader lean_factor value: ' + tag.attrib['lean_factor'])
    LOGGER.info(' change_twist_shader lean_direction value: ' + tag.attrib['lean_direction'])
    LOGGER.info(' change_twist_shader base_altitude value: ' + tag.attrib['base_altitude'])
    return tags_root

def change_distribution_shader(tags_root: ET.Element, global_values: dict, attribute="DistributionColour") -> ET.Element:
    LOGGER.info(' change_distribution_shader function called')
    if global_values['use_seed']:
        random.seed(global_values['seed'], version=2)
    # Opening the range file
    with open(global_values['ranges_shader_path'], 'r') as range_file:
        ranges = json.load(range_file)
    distribution_ranges = ranges['distribution_colour']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['colour'] = '255 255 255'
    tag.attrib['limit_minimum_altitude'] = str(random.randint(0, 1))
    tag.attrib['minimum_altitude'] = '100'
    tag.attrib['min_alt_fuzzy_zone'] = str(random.uniform(distribution_ranges['min_alt_fuzzy_zone_minimum'], distribution_ranges['min_alt_fuzzy_Zone_maximum']))
    tag.attrib['altitude_key'] = str(random.randint(0, 1))
    tag.attrib['limit_maximum_slope'] = str(random.randint(0, 1))
    tag.attrib['maximum_slpoe_angle'] = str(random.uniform(distribution_ranges['maximum_slope_angle_minimum'], distribution_ranges['maximum_slope_angle_maximum']))
    tag.attrib['max_slope_fuzzy_zone'] = str(random.uniform(distribution_ranges['max_slope_fuzzy_zone_minimum'], distribution_ranges['max_slope_fuzzy_zone_maximum']))
    # tag.attrib['limit_minimum_slope'] = '1'  # TODO random generate between 0 and 1
    # tag.attrib['minimum_slpoe_angle'] = '200'  # TODO it is in degree
    # tag.attrib['min_slope_fuzzy_zone'] = '52'
    tag.attrib['slope_key'] = str(random.randint(0, 2))
    LOGGER.info(' change_distribution_shader min_alt_fuzzy_zone value: ' + tag.attrib['min_alt_fuzzy_zone'])
    LOGGER.info(' change_distribution_shader maximum_slpoe_angle value: ' + tag.attrib['maximum_slpoe_angle'])
    LOGGER.info(' change_distribution_shader maximum_slpoe_angle value: ' + tag.attrib['maximum_slpoe_angle'])
    LOGGER.info(' change_distribution_shader max_slope_fuzzy_zone value: ' + tag.attrib['max_slope_fuzzy_zone'])
    return tags_root