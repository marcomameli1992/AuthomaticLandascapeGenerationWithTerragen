import xml.etree.ElementTree as ET

# TODO define the range for all the parameters

def change_basic_terrain(tags_root: ET.Element, attribute='Strata'):
    tag = tags_root.find(".//*[@name='Strata']")
    tag.attrib['name'] = "StrataChanged" # changing the name It is usefull only to have a note of teh method to access to an attribute
    return tags_root