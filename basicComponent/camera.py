import xml.etree.ElementTree as ET

def change_camera(tags_root: ET.Element, attribute="Sun") -> ET.Element:
    #TODO check if it is better to create one camera and changes the position or more than 1 and do not use this script
    return tags_root