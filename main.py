#%% Import section of customized function
from basicComponent.values import set_use_seed, set_seed, set_ranges_folder_path, \
    set_light_value_path, set_water_value_path, set_shader_value_path, set_populator_value_path, \
    set_terrain_value_path
from basicComponent.terrain import *
from basicComponent.water import *
from basicComponent.shader import *
from basicComponent.populator import *
from basicComponent.light import *
from basicComponent.opening import *

#%% import of the basic component
import xml.etree.ElementTree as ET
import os
import json
from multiprocessing import cpu_count, Process
import datetime
import argparse
import logging

input_args = argparse.ArgumentParser()
input_args.add_argument('--config_file', type=str, required=True, help="The json configuration file")

args = input_args.parse_args()

def file_generatioin(etree: ET.ElementTree, number_of_file: int, save_path: str):
    import logging
    import os
    LOGGER = logging.getLogger('Process PID: ' + str(os.getpid()))
    LOGGER.info(' Generation start')
    #%%  Nodes list
    terrain_list: list = []
    water_list: list = []
    shader_list: list = []
    light_list: list = []
    populator_list: list = []
    #%% get the etree_root from the etree element
    etree_root = etree.getroot()
    #%% Nodes list filling
    for element in etree_root.find('power_fractal_shader_v3'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.find('fractal_warp_shader'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    for element in etree_root.find('distribution_shader_v4'):
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.find('twist_and_shear_shader'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.find('strata_and_outcrops_shader_v2'):
        if 'Terrain' in element.attrib['name'] or 'Terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    for element in etree_root.find('fake_stones_shader'):
        if 'Terrain' in element.attrib['name'] or 'Terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    for element in etree_root.find('enviro_light'):
        if 'Light' in element.attrib['name'] or 'light' in element.attrib['name']:
            light_list.append(element.attrib['name'])
    for element in etree_root.find('sunlight'):
        if 'Sun' in element.attrib['name'] or 'sun' in element.attrib['name']:
            light_list.append(element.attrib['name'])
    for element in etree_root.find('populator_v4'):
        if 'Tree' in element.attrib['name'] or 'tree' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
        if 'Grass' in element.attrib['name'] or 'grass' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
        if 'Pop' in element.attrib['name'] or 'pop' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
    for element in etree_root.find('lake'):
        if 'Lake' in element.attrib['name'] or 'lake' in element.attrib['name']:
            water_list.append(element.attrib['name'])

    #%% Logging teh generation
    LOGGER.info(' Lists filled:')
    LOGGER.info(' \tTerrain list has {} values'.format(len(terrain_list)))
    LOGGER.info(' \tShader list has {} values'.format(len(shader_list)))
    LOGGER.info(' \tPopulation list has {} values'.format(len(populator_list)))
    LOGGER.info(' \tLight list has {} values'.format(len(light_list)))
    LOGGER.info(' \tWater list has {} values'.format(len(water_list)))

    #%% File generation
    for n in range(number_of_file):
        for element_name in terrain_list:
            if 'Fractal' in element_name or 'fractal' in element_name:
                etree_root = change_fractal_terrain(etree_root, element_name)
            if 'Stone' in element_name or 'stone' in element_name:
                etree_root = change_stone(etree_root, element_name)
            if 'Strata' in element_name or 'strata' in element_name:
                etree_root = change_strata(etree_root, element_name)
            if 'Twist' in element_name or 'twist' in element_name:
                etree_root = change_twist_terrain(etree_root, element_name)
            if 'Warp' in element_name or 'warp' in element_name:
                etree_root = change_fractal_warp(etree_root, element_name)

        for element_name in shader_list:
            if 'Surface' in element_name or 'surface' in element_name:
                etree_root = change_surface_shader(etree_root, element_name)
            if 'Fractal' in element_name or 'fractal' in element_name:
                etree_root = change_fractal_shader(etree_root, element_name)
            if 'Distribution' in element_name or 'distribution' in element_name:
                etree_root = change_distribution_shader(etree_root, element_name)
            if 'Twist' in element_name or 'twist' in element_name:
                etree_root = change_twist_shader(etree_root, element_name)

        for element_name in light_list:
            if 'Sun' in element_name or 'sun' in element_name:
                etree_root = change_sunllight(etree_root, element_name)
            if 'Light' in element_name or 'light' in element_name:
                etree_root = change_environmental(etree_root, element_name)

        for element_name in water_list:
            if 'Lake' in element_name or 'lake' in element_name:
                etree_root = change_fractal_water(etree_root, element_name)

        for element_name in populator_list:
            if 'Tree' in element_name or 'tree' in element_name:
                etree_root = change_trees_population(etree_root, element_name)
            if 'Grass' in element_name or 'grass' in element_name:
                etree_root = change_grass_population(etree_root, element_name)
        LOGGER.info(' Changes finished. Saving the file')
        file_name = 'Generation_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.tgd'
        with open(os.path.join(save_path, file_name), 'wb') as tgd_file:
            etree.write(tgd_file)
        LOGGER.info(' File Saved with name {} '.format(file_name))


#%% read the configurations
config_file_path = args.config_file
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)

#%% define the logger
logging.basicConfig(filename=config['logging_file_path'],level=logging.INFO)
LOGGER = logging.getLogger("main")

if config['use_seed']:
    set_use_seed(config['use_seed'])
    set_seed(config['seed'])
    LOGGER.info(' seed {} applied to the execution'.format(config['seed']))
else:
    LOGGER.info(' fixed seed deactivated')

#%% opening the basic file
basic_file_path = config['base_file_path']
etree, etree_root = tgd_opening(basic_file_path)
LOGGER.info(' opened the {} file'.format(config['base_file_path'].split('/')[-1]))

#%% setting ranges path
set_ranges_folder_path(config['ranges_folder_path'])
set_light_value_path(config['light_ranges_name'])
set_terrain_value_path(config['terrain_ranges_name'])
set_shader_value_path(config['shader_ranges_name'])
set_populator_value_path(config['popultor_ranges_name'])
set_water_value_path(config['water_ranges_name'])
LOGGER.info(' set the ranges files path for each node')

#%% prepraring multiprocessing execution
n_cpu = cpu_count()
proc_list : list = []

n_file_per_proc = int(config['n_files'] / n_cpu)

if int(config['n_files']) == 1:
    LOGGER.info(' Required only un processor for the generation of one file')
    file_generatioin(etree, config['n_files'], config['save_path'])
else:
    LOGGER.info(' Required the multiprocessor generation')
    LOGGER.info(' The number of processor available is {}'.format(n_cpu))
    LOGGER.info(' Required {} files to be generated, each process generate {} files'.format(config['n_files'], n_file_per_proc))
    for p in range(n_cpu):
        LOGGER.info(' Generated process')
        proc = Process(target=file_generatioin, args=(etree, n_file_per_proc, config['save_path']))
        proc_list.append(proc)
        proc.start()
    LOGGER.info(' All process generated. Waiting the termination')
    for p in proc_list:
        p.join()