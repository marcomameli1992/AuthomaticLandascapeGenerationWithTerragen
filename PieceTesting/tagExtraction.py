import xml.etree.ElementTree as ET
import os

file_path = os.path.join('..', 'TerragenGeneratedFile', 'MountainPython.tgd')

tree = ET.parse(file_path)

tags_set = {elem.tag for elem in tree.iter()}

for tag in

print(tags_set)