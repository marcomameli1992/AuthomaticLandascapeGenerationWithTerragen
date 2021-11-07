import xml.etree.ElementTree as ET
import logging
import os

#%% define logging
LOGGER = logging.getLogger("POPULATOR_CHANGES")

def change_populator_path(tags_root: ET.Element, populator_object='tgo_reader') -> ET.Element:
    LOGGER.info(' called populator object paths')
    for element in tags_root.findall(populator_object):
        print(element.attrib['filename'])
        element.attrib['filename'] = element.attrib['filename'].replace('\\', os.sep)

    return tags_root