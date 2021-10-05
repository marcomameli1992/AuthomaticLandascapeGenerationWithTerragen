import xml.etree.ElementTree as ET
import os

file_path = os.path.join('..', 'TerragenGeneratedFile', 'MountainPython.tgd')

tree = ET.parse(file_path)

root = tree.getroot()

print(root)