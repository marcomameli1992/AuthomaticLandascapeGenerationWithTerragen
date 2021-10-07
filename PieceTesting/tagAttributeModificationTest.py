# import section
import xml.etree.ElementTree as ET
import os
from basicComponent.terrain import change_fractal_terrain
import filecmp

# opening the file
file_path = os.path.join('..', 'TerragenOriginalFile', 'Base_0001.tgd')
tree = ET.parse(file_path)
root = tree.getroot()

changes = change_fractal_terrain(root)

# saving changes
with open('../TerragenGeneratedFile/MountainPython.tgd', 'wb') as tgd_file:
    tree.write(tgd_file)

assert filecmp.cmp(file_path, file_path)
assert not(filecmp.cmp(file_path, '../TerragenGeneratedFile/MountainPython.tgd', shallow=True)) # CHECK if the file generated are the same or not