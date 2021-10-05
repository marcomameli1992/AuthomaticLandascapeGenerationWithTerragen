# import section
import xml.etree.ElementTree as ET
import os

def change_basic_terrain(tags_root: ET.Element, attribute='Strata'):
    tag = tags_root.find(f".//*[@name='{attribute}']")
    tag.attrib['name'] = "StrataChanged"
    return tags_root

# opening the file
file_path = os.path.join('..', 'TerragenOriginalFile', 'Base.tgd')
tree = ET.parse(file_path)
root = tree.getroot()
# Terrain extraction
tag = root.find(".//*[@name='Strata']") # Search query for the XML by the name in the TAG

changed = change_basic_terrain(root)