# import section
import xml.etree.ElementTree as ET
import os

def change_basic_terrain(tags_root: ET.Element, name='BasicTerrain'):
    tag = tags_root.find(f".//*[@name='{name}']")
    tag.attrib['enable'] = "0" # TODO random generate between 0 and 1 (INTEGER)
    tag.attrib['seed'] = '525' # TODO random generate the SEED
    # TODO From here become important define the range for the random generation
    # SCALE changes
    tag.attrib['feature_scale'] = '1250'
    tag.attrib['lead-in_scale'] = '120'
    tag.attrib['smallest_scale'] = '25'
    # SCALE-NOISE changes
    tag.attrib['noise_octaves'] = '4'
    tag.attrib['obey_smoothing_filter'] = '1' # TODO random generate between 0 and 1 (INTEGER)
    tag.attrib['noise_stretch_XYZ'] = '3 0 2' # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    # COLOR changes
    tag.attrib['apply_high_colour'] = '1' # TODO random generate between 0 and 1
    # tag.attrib['high_colour'] = '0 0 0' # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    tag.attrib['apply_low_colour'] = '1'  # TODO random generate between 0 and 1
    # tag.attrib['low_colour'] = '0 0 0' # TODO create a function for the generation of space separated string that generate 3 random FLOAT values
    tag.attrib['colour_contrast'] = '0'
    tag.attrib['colour_roughness'] = '2.5'
    tag.attrib['clamp_high_colour'] = '1'
    tag.attrib['clamp_low_colour'] = '0'
    # DISPLACEMENT changes
    tag.attrib['displacement_direction'] = '1' # TODO random generate between 0 and 1
    tag.attrib['displacement_amplitude'] = '23456'
    tag.attrib['displacement_offset'] = '1000'
    tag.attrib['displacement_roughness'] = '8'
    tag.attrib['displacement_spike_limit'] = '10'
    tag.attrib['continue_spike_limit'] = '1'
    tag.attrib['adjust_coastline'] = '1'
    tag.attrib['coastline_altitude'] = '90'
    tag.attrib['coastline_smoothing'] = '50'
    # NOISE changes
    tag.attrib['noise_flavour'] = '0' # TODO random generate between 0 and 6 (INTEGER)
    tag.attrib['ridge_smoothing'] = '65'
    tag.attrib['gully_smoothing'] = '25'
    tag.attrib['noise_variation'] = '35' # TODO random generation of a FLOAT value with the idea that 0 is the maximum value
    tag.attrib['variation_method'] = '1' # TODO random generate between 0 and 3 (INTEGER)
    tag.attrib['buoyancy_from_variation'] = '0.65'
    tag.attrib['clumping_of_variation'] = '0.25'
    tag.attrib['better_colour_continuity'] = '1'
    tag.attrib['better_displacement_continuity'] = '0'
    # DISTORTION changes
    tag.attrib['distort_by_normal'] = '1'
    tag.attrib['distortion_by_normal'] = '2'
    tag.attrib['lead-in_warp_effect'] = '0'
    tag.attrib['lead-in_warp_ammount'] = '32'
    tag.attrib['less_warp_at_feature_scale'] = '1' # TODO random generate between 0 and 1
    tag.attrib['allow_vertical_warp'] = '0' # TODO random generate between 0 and 1

    return tags_root

# opening the file
file_path = os.path.join('..', 'TerragenOriginalFile', 'Base.tgd')
tree = ET.parse(file_path)
root = tree.getroot()
# Terrain extraction
tag = root.find(".//*[@name='Strata']") # Search query for the XML by the name in the TAG

changed = change_basic_terrain(root)