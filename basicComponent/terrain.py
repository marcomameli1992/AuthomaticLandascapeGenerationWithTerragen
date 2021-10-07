import xml.etree.ElementTree as ET
import random
import os
import json
import numpy as np

range_value_path = os.path.join('..', 'basicComponent', 'ranges', 'terrain.json')

def change_fractal_terrain(tags_root: ET.Element, attribute='BasicTerrain') -> ET.Element:
    '''

    :param tags_root:
    :param attribute:
    :return:
    '''
    # Opening the range file
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    fractal_terrain_ranges = ranges['fractal_terrain']

    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = '1' # at least one fractal power shader has to be active for the terrain generation
    tag.attrib['seed'] = str(int(random.random()))
    # SCALE changes
    tag.attrib['feature_scale'] = str(random.uniform(fractal_terrain_ranges['feature_scale_minimum'], fractal_terrain_ranges['feature_scale_maximum']))
    tag.attrib['lead-in_scale'] = str(random.uniform(fractal_terrain_ranges['lead-in_scale_minimum'], fractal_terrain_ranges['lead-in_scale_maximum']))
    tag.attrib['smallest_scale'] = str(random.uniform(fractal_terrain_ranges['smallest_scale_minimum'], fractal_terrain_ranges['smallest_scale_maximum']))
    # SCALE-NOISE changes
    tag.attrib['noise_octaves'] = str(random.randint(fractal_terrain_ranges['noise_octaves_minimum'], fractal_terrain_ranges['noise_octaves_macimum']))
    tag.attrib['obey_smoothing_filter'] = str(random.randint(0, 1))
    tag.attrib[
        'noise_stretch_XYZ'] = ' '.join(map(str, list(np.random.randint(low=0, high=1e+5, size=3))))
    # COLOR changes # NOT USED
    # tag.attrib['apply_high_colour'] = '1'
    # # tag.attrib['high_colour'] = '0 0 0'
    # tag.attrib['apply_low_colour'] = '1'
    # # tag.attrib['low_colour'] = '0 0 0'
    # tag.attrib['colour_contrast'] = '0'
    # tag.attrib['colour_roughness'] = '2.5'
    # tag.attrib['clamp_high_colour'] = '1'
    # tag.attrib['clamp_low_colour'] = '0'
    # DISPLACEMENT changes
    tag.attrib['displacement_direction'] = '1'
    tag.attrib['displacement_amplitude'] = str(random.uniform(fractal_terrain_ranges['displacement_altitude_minimum'], fractal_terrain_ranges['displacement_altitude_maximum']))
    tag.attrib['displacement_offset'] = str(random.uniform(fractal_terrain_ranges['didplacement_offset_minimum'], fractal_terrain_ranges['displacement_offset_maximum']))
    tag.attrib['displacement_roughness'] = str(random.uniform(fractal_terrain_ranges['displacement_roughness_minimum'], fractal_terrain_ranges['displacement_roughness_maximum']))
    tag.attrib['displacement_spike_limit'] = str(random.uniform(fractal_terrain_ranges['displacement_spike_limit_minimum'], fractal_terrain_ranges['displacement_spike_limit_maximum']))
    tag.attrib['continue_spike_limit'] = '1'
    tag.attrib['adjust_coastline'] = '1'
    tag.attrib['coastline_altitude'] = str(random.uniform(fractal_terrain_ranges['coastline_altitude_minimum'], fractal_terrain_ranges['coastline_altitute_maximum']))
    tag.attrib['coastline_smoothing'] = str(random.uniform(fractal_terrain_ranges['coastline_smoothing_minimum'], fractal_terrain_ranges['coastline_smoothing_maximum']))
    # NOISE changes
    tag.attrib['noise_flavour'] = str(random.randint(0, 5))
    tag.attrib['ridge_smoothing'] = str(random.uniform(fractal_terrain_ranges['ridge_smoothing_minimum'], fractal_terrain_ranges['ridge_smoothing_maximum']))
    tag.attrib['gully_smoothing'] = str(random.uniform(fractal_terrain_ranges['gully_smoothing_minimum'], fractal_terrain_ranges['gully_smoothing_maximum']))
    tag.attrib['noise_variation'] = str(random.uniform(fractal_terrain_ranges['noise_variation_minimum'], fractal_terrain_ranges['noise_variation_maximum']))
    tag.attrib['variation_method'] = str(random.randint(0, 3))
    #tag.attrib['buoyancy_from_variation'] = '0.65'
    #tag.attrib['clumping_of_variation'] = '0.25'
    tag.attrib['better_colour_continuity'] = str(random.randint(0, 1))
    tag.attrib['better_displacement_continuity'] = str(random.randint(0, 1))
    # DISTORTION changes
    # tag.attrib['distort_by_normal'] = '1'
    # tag.attrib['distortion_by_normal'] = '2'
    # tag.attrib['lead-in_warp_effect'] = '0'
    # tag.attrib['lead-in_warp_ammount'] = '32'
    # tag.attrib['less_warp_at_feature_scale'] = '1'
    # tag.attrib['allow_vertical_warp'] = '0'
    return tags_root

def change_stone(tags_root: ET.Element, attribute = 'FakeStone') -> ET.Element:
    # Opening the range file
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    stone_ranges = ranges['stone']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['stone_scale'] = str(random.uniform(stone_ranges['stone_scale_minimum'], stone_ranges['stone_scale_maximum']))
    tag.attrib['stone_density'] = str(random.uniform(stone_ranges['stone_density_minimum'], stone_ranges['stone_density_maximum']))
    tag.attrib['vary_density'] = str(random.randint(0, 1))
    tag.attrib['density_seed'] = str(int(random.random()))
    tag.attrib['density_variation_scale'] = str(random.uniform(stone_ranges['density_variation_scale_minimum'], stone_ranges['density_variation_scale_maximum']))
    tag.attrib['stone_tallness'] = str(random.uniform(stone_ranges['stone_tallness_minimum'], stone_ranges['stone_tallness_maximum']))
    tag.attrib['pancake_effect'] = str(random.uniform(stone_ranges['pancake_effect_minimum'], stone_ranges['pancake_effect_maximum']))
    tag.attrib['only_displace_upwards'] = str(random.randint(0, 1))
    # tag.attrib['apply_colour'] = '3'
    # tag.attrib['diffuse_colour'] = '3'
    # tag.attrib['colour_variatioin'] = '1'
    # tag.attrib['variatioin_in_red'] = '3'
    # tag.attrib['variatioin_in_green'] = '3'
    # tag.attrib['variatioin_in_blue'] = '3'
    return tags_root

def change_strata(tags_root: ET.Element, attribute="Strata") -> ET.Element:
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    strata_ranges = ranges['strata']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['hard_layer_altitude'] = str(random.uniform(strata_ranges['hard_layer_altitude_minimum'], strata_ranges['hard_layer_altitude_maximum']))
    tag.attrib['hard_layer_depth'] = str(random.uniform(strata_ranges['hard_layer_depth_minimum'], strata_ranges['hard_layer_depth_maximum']))
    tag.attrib['hard_layer_steepness'] = str(random.uniform(strata_ranges['hard_layer_steepness_minimum'], strata_ranges['hard_layer_steepness_maximum']))
    tag.attrib['plateau_buildup'] = str(random.uniform(strata_ranges['plateau_buildup_minimum'], strata_ranges['plateau_buildup_maximum']))
    #tag.attrib['num_octaves'] = '25'
    tag.attrib['strata_tilt_direction'] = str(random.uniform(strata_ranges['strata_tilt_direction_minimum'], strata_ranges['strata_tilt_direction_maximum']))
    tag.attrib['strata_tilt_angle'] = str(random.uniform(strata_ranges['strata_tilt_angle_minimum'], strata_ranges['strata_tilt_angle_maximum']))
    return tags_root

def change_twist(tags_root: ET.Element, attribute="Twist") -> ET.Element:
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    twist_ranges = ranges['twist']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['lean_factor'] = str(random.uniform(twist_ranges['lean_factor_minimum'], twist_ranges['lean_factor_maximum']))
    if random.randint(0, 5000) > 2500:
        tag.attrib['lean_direction'] = ' '.join(map(str, list(np.random.randint(low=0, high=1e+5, size=3))))
    else:
        tag.attrib['lean_direction'] = '0 0 0'
    tag.attrib['base_altitude'] = str(random.uniform(twist_ranges['base_altitude_minum'], twist_ranges['base_altitude_maximum']))
    return tags_root

def change_fractal_warp(tags_root: ET.Element, attribute="BasicWarp") -> ET.Element:
    with open(range_value_path, 'r') as range_file:
        ranges = json.load(range_file)
    warp_ranges = ranges['warp']
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = str(random.randint(0, 1))
    tag.attrib['scale'] = str(random.uniform(warp_ranges['scale_minimum'], warp_ranges['scale_maximum']))
    tag.attrib['warp_ammount'] = str(random.uniform(warp_ranges['warp_ammount_minimum'], warp_ranges['warp_ammount_maximum']))
    tag.attrib['variation'] = str(random.uniform(warp_ranges['variation_minimum'], warp_ranges['variation_maximum']))
    tag.attrib['roughness'] = str(random.uniform(warp_ranges['roughness_minimum'], warp_ranges['roughness_maximum']))
    tag.attrib['obey_smoothing_filter'] = str(random.randint(0, 1))
    return tags_root

def change_fractal_alpine(tags_root: ET.Element, attribute="AlpineTerrain") -> ET.Element:
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = "0"  # TODO random generate between 0 and 1 (INTEGER)
    tag.attrib['seed'] = '525'  # TODO random generate the SEED
    # TODO From here become important define the range for the random generation
    # SCALE changes
    tag.attrib['feature_scale'] = '1250'
    tag.attrib['lead-in_scale'] = '120'
    tag.attrib['smallest_scale'] = '25'
    # SCALE-NOISE changes
    tag.attrib['noise_octaves'] = '4'
    # DISPLACEMENT changes
    tag.attrib['apply_displacement'] = '1'
    tag.attrib['displacement_amplitude'] = '23456'
    tag.attrib['displacement_offset'] = '1000'
    tag.attrib['displacement_roughness'] = '8'
    # NOISE changes
    tag.attrib['scale_step'] = '65'
    tag.attrib['stretch_factor'] = '25'
    tag.attrib['late_deposition'] = '35'  # TODO random generation of a FLOAT value with the idea that 0 is the maximum value
    tag.attrib['early_deposition'] = '1'  # TODO random generate between 0 and 3 (INTEGER)
    tag.attrib['early_deposition_rate'] = '0.65'
    tag.attrib['warp_ammount'] = '0.25'
    return tags_root