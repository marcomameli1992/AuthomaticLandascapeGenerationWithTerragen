import xml.etree.ElementTree as ET

# TODO define the range for all the parameters

def change_fractal_shader(tags_root: ET.Element, attribute='BaseColours') -> ET.Element:
    '''

    :param tags_root:
    :param attribute:
    :return:
    '''
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
    tag.attrib['obey_smoothing_filter'] = '1'  # TODO random generate between 0 and 1 (INTEGER)
    tag.attrib[
        'noise_stretch_XYZ'] = '3 0 2'  # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    # COLOR changes
    tag.attrib['apply_high_colour'] = '1'  # TODO random generate between 0 and 1
    # tag.attrib['high_colour'] = '0 0 0' # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    tag.attrib['apply_low_colour'] = '1'  # TODO random generate between 0 and 1
    # tag.attrib['low_colour'] = '0 0 0' # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    tag.attrib['colour_contrast'] = '0'
    tag.attrib['colour_roughness'] = '2.5'
    tag.attrib['clamp_high_colour'] = '1'
    tag.attrib['clamp_low_colour'] = '0'
    # DISPLACEMENT changes
    tag.attrib['displacement_direction'] = '1'  # TODO random generate between 0 and 1
    tag.attrib['displacement_amplitude'] = '23456'
    tag.attrib['displacement_offset'] = '1000'
    tag.attrib['displacement_roughness'] = '8'
    tag.attrib['displacement_spike_limit'] = '10'
    tag.attrib['continue_spike_limit'] = '1'
    tag.attrib['adjust_coastline'] = '1'
    tag.attrib['coastline_altitude'] = '90'
    tag.attrib['coastline_smoothing'] = '50'
    # NOISE changes
    tag.attrib['noise_flavour'] = '0'  # TODO random generate between 0 and 6 (INTEGER)
    tag.attrib['ridge_smoothing'] = '65'
    tag.attrib['gully_smoothing'] = '25'
    tag.attrib[
        'noise_variation'] = '35'  # TODO random generation of a FLOAT value with the idea that 0 is the maximum value
    tag.attrib['variation_method'] = '1'  # TODO random generate between 0 and 3 (INTEGER)
    tag.attrib['buoyancy_from_variation'] = '0.65'
    tag.attrib['clumping_of_variation'] = '0.25'
    tag.attrib['better_colour_continuity'] = '1'
    tag.attrib['better_displacement_continuity'] = '0'
    # DISTORTION changes
    tag.attrib['distort_by_normal'] = '1'
    tag.attrib['distortion_by_normal'] = '2'
    tag.attrib['lead-in_warp_effect'] = '0'
    tag.attrib['lead-in_warp_ammount'] = '32'
    tag.attrib['less_warp_at_feature_scale'] = '1'  # TODO random generate between 0 and 1
    tag.attrib['allow_vertical_warp'] = '0'  # TODO random generate between 0 and 1

    return tags_root

def change_surface_shader(tags_root: ET.Element, attribute="Grass") -> ET.Element:
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = "0"  # TODO random generate between 0 and 1 (INTEGER)
    tag.attrib['apply_colour'] = '1'  # TODO random generate between 0 and 1 (INTEGER)
    # TODO From here become important define the range for the random generation
    tag.attrib['diffuse_colour'] = '1 5 0'
    tag.attrib['displacement_direction'] = '0' # or 1
    tag.attrib['displacement_multiplier'] = '25'
    tag.attrib['smoothing_effect'] = '4'
    tag.attrib['smoothing_ammount'] = '5'
    tag.attrib['coverage'] = '3'
    tag.attrib['limit_maximum_altitude'] = '1'  # TODO random generate between 0 and 1
    tag.attrib['maximum_altitude'] = '100'
    tag.attrib['max_alt_fuzzy_zone'] = '85'
    tag.attrib['limit_minimum_altitude'] = '1'  # TODO random generate between 0 and 1
    tag.attrib['minimum_altitude'] = '100'
    tag.attrib['min_alt_fuzzy_zone'] = '85'
    tag.attrib['limit_maximum_slope'] = '1' # TODO random generate between 0 and 1
    tag.attrib['maximum_slpoe_angle'] = '200' # TODO it is in degree
    tag.attrib['max_slope_fuzzy_zone'] = '52'
    tag.attrib['limit_minimum_slope'] = '1'  # TODO random generate between 0 and 1
    tag.attrib['minimum_slpoe_angle'] = '200'  # TODO it is in degree
    tag.attrib['min_slope_fuzzy_zone'] = '52'
    tag.attrib['slope_key'] = '1'  # TODO random generate between 0 and 2 INTEGERS
    tag.attrib['use_y_for_slope'] = '0' # TODO random generate between 0 and 1
    tag.attrib['intersection_underlying'] = '1' # TODO random generate between 0 and 1
    tag.attrib['intersect_mode'] = '1' # TODO random generate between 0 and 2 INTEGERS
    tag.attrib['intersection_zone'] = '10' # Range in meters
    tag.attrib['intersection_shift'] = '154'
    tag.attrib['min_intersection_shift'] = '100'
    return tags_root