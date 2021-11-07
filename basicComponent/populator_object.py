import xml.etree.ElementTree as ET
import logging
import os

#%% define logging
LOGGER = logging.getLogger("POPULATOR_CHANGES")

def change_populator_path(tags_root: ET.Element, populator_tag='populator_v4', populator_reader='tgo_reader') -> ET.Element:
    LOGGER.info(' called populator object paths')
    for element in tags_root.findall(populator_tag):
        for reader in element.findall(populator_reader):
            print('Old path', reader.attrib['filename'])
            new_path = reader.attrib['filename'].replace('\\', os.sep)
            print('New path', new_path)
            reader.attrib['filename'] = new_path#reader.attrib['filename'].replace('\\', os.sep)

    return tags_root