import xml.etree.ElementTree as ET

def change_sunllight(tags_root: ET.Element, attribute="Sun") -> ET.Element:
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['enable'] = "0"
    tag.attrib['colour'] = '1 5 0'
    tag.attrib['light_surfaces'] = '0'  # or 1
    tag.attrib['light_atmosphere'] = '0'  # or 1
    tag.attrib['heading'] = '4' # degrees 0 for North 90 for Est
    tag.attrib['elevation'] = '0' # 0 is the horizon and 90 is the overhead
    tag.attrib['strength'] = '1'  # the power of the sunlight maximum is 5 ( better integer value step)
    tag.attrib['cast_shadow'] = '1' # or 0 to activate or not
    tag.attrib['shadow_onSurfaces'] = '1' # or 0 to activate or not
    tag.attrib['shadow_of_atmosphere'] = '1'
    tag.attrib['soft_shadow'] = '1'
    tag.attrib['soft_shadow_diameter'] = '0'  # degrees
    tag.attrib['soft_shadow_samples'] = '4'
    tag.attrib['soft_shadow_samples_jitter'] = '0'
    tag.attrib['glow_in_atmosphere'] = '1'
    tag.attrib['specular_highlights'] = '1' # or 0 to activate or not
    tag.attrib['visible_disc'] = '1' # or 0 to activate or not
    tag.attrib['angular_diameter'] = '1' # the size of the disk
    return tags_root

def change_environmental(tags_root: ET.Element, attribute="Enviro light") -> ET.Element:
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['global_strength_on_surfaces'] = '1'
    tag.attrib['global_strength_in_atmosphere'] = '1'
    return tags_root