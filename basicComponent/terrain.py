import xml.etree.ElementTree as ET

def change_basic_terrain(tags_root: ET.Element, attribute='Strata'):
    tag = tags_root.find(".//*[@name='Strata']")
    tag.attrib['name'] = "StrataChanged"
    return tags_root