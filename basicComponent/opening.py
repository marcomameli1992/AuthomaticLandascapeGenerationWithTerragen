import xml.etree.ElementTree as ET

def tgd_opening(path)-> ET.Element:
    tree = ET.parse(path)
    root = tree.getroot()

    return tree, root