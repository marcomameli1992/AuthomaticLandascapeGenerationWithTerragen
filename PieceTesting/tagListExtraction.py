# import section
import xml.etree.ElementTree as ET
import os

# opening the file
file_path = os.path.join('..', 'TerragenOriginalFile', 'Base.tgd')
tree = ET.parse(file_path)

for element in tree.iter():
    with open(os.path.join('..', 'basicTag', element.tag + '.xml'), 'wb') as element_file:
        
