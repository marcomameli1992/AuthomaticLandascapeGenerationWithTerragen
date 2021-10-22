import os.path
import xml.etree.ElementTree as ET
import logging

#%% define logging
LOGGER = logging.getLogger("RENDER")

def get_render_node(tags_root: ET.Element) -> list:
    #%% find all render node
    LOGGER.info(' Search for alla render node in the file')
    render_elments: list = []
    for element in tags_root.findall('render'):
        render_elments.append(element.attrib['name'])

    return render_elments

def change_render_paths(tags_root: ET.Element, attribute:str, output_image_path:str, extra_output_image_path:str) -> ET.Element:
    LOGGER.info(' search for the render node')
    tag = tags_root.find(f".//*[@name='{attribute}']")
    LOGGER.info(f' change the file name and path for the render node {attribute}')
    output_image_filename = os.path.join(output_image_path, attribute + '_${TGDNAME}.%04d.tiff')
    extra_output_image_file_name = os.path.join(extra_output_image_path, attribute + '_$IMAGETYPE.%04d.exr')
    tag.attrib['output_image_filename'] = output_image_filename
    tag.attrib['extra_output_image_filename'] = extra_output_image_file_name
    return tags_root

def change_micro_render_path(tags_root: ET.Element, output_mesh_path:str, render_node_name:str, attribute:str = 'MicroRender') -> ET.Element:
    LOGGER.info(' changing the mesh exporter save path')
    tag = tags_root.find(f".//*[@name='{attribute}']")
    output_mesh_filename = os.path.join(output_mesh_path, render_node_name + '_${TGDNAME}.%04d.obj')
    tag.attrib['filename'] = output_mesh_filename
    return tags_root