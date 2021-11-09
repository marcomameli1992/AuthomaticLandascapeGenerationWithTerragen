#%% import of the basic component
import random
import xml.etree.ElementTree as ET
import os
import json
from multiprocessing import cpu_count, Process
import datetime
import argparse
import logging
from sys import platform

isLinux = platform.startswith("linux")

input_args = argparse.ArgumentParser()
input_args.add_argument('--config_file', '-cf', type=str, required=True, help="The json configuration file")

args = input_args.parse_args()

def file_generatioin(etree: ET.ElementTree, number_of_file: int, save_path: str, global_values: dict, enabled_changes:dict):
    #%% Import section of customized function
    import basicComponent.terrain as TERRAIN
    import basicComponent.water as WATER
    import basicComponent.shader as SHADER
    import basicComponent.populator as POPULATOR
    import basicComponent.light as LIGHT
    #%% Setting logging for the function
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
    for element in etree_root.findall('power_fractal_shader_v3'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.findall('fractal_warp_shader'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    for element in etree_root.findall('distribution_shader_v4'):
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.findall('twist_and_shear_shader'):
        if 'Terrain' in element.attrib['name'] or 'terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
        if 'Colour' in element.attrib['name'] or 'colour' in element.attrib['name']:
            shader_list.append(element.attrib['name'])
    for element in etree_root.findall('strata_and_outcrops_shader_v2'):
        if 'Terrain' in element.attrib['name'] or 'Terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    for element in etree_root.findall('fake_stones_shader'):
        if 'Terrain' in element.attrib['name'] or 'Terrain' in element.attrib['name']:
            terrain_list.append(element.attrib['name'])
    #%% Not needed the changes to environmental for this reason it was deactivated
    '''
    for element in etree_root.findall('enviro_light'):
        if 'Light' in element.attrib['name'] or 'light' in element.attrib['name']:
            light_list.append(element.attrib['name'])
    '''
    for element in etree_root.findall('sunlight'):
        if 'Sun' in element.attrib['name'] or 'sun' in element.attrib['name']:
            light_list.append(element.attrib['name'])
        if 'Mid' in element.attrib['name'] or 'mid' in element.attrib['name']:
            light_list.append(element.attrib['name'])
    for element in etree_root.findall('populator_v4'):
        if 'Tree' in element.attrib['name'] or 'tree' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
        if 'Grass' in element.attrib['name'] or 'grass' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
        if 'Pop' in element.attrib['name'] or 'pop' in element.attrib['name']:
            populator_list.append(element.attrib['name'])
    for element in etree_root.findall('lake'):
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
    for n in list(range(0, number_of_file)):
        for element_name in terrain_list:
            if 'Fractal' in element_name or 'fractal' in element_name and enabled_changes['terrain']:
                etree_root = TERRAIN.change_fractal_terrain(etree_root, global_values, element_name)
                #TODO check the possibility to abilitate only one terrain or two a time
            if 'Stone' in element_name or 'stone' in element_name and enabled_changes['terrain']:
                etree_root = TERRAIN.change_stone(etree_root, global_values, element_name)
            # if 'Strata' in element_name or 'strata' in element_name:
            #     etree_root = TERRAIN.change_strata(etree_root, global_values, element_name)
            if 'Twist' in element_name or 'twist' in element_name and enabled_changes['terrain']:
                etree_root = TERRAIN.change_twist_terrain(etree_root, global_values, element_name)
            if 'Warp' in element_name or 'warp' in element_name and enabled_changes['terrain']:
                etree_root = TERRAIN.change_fractal_warp(etree_root, global_values, element_name)

        for element_name in shader_list:
            if 'Surface' in element_name or 'surface' in element_name and enabled_changes['shader']:
                etree_root = SHADER.change_surface_shader(etree_root, global_values, element_name)
            if 'Fractal' in element_name or 'fractal' in element_name and enabled_changes['shader']:
                etree_root = SHADER.change_fractal_shader(etree_root, global_values, element_name)
            if 'Distribution' in element_name or 'distribution' in element_name and enabled_changes['shader']:
                etree_root = SHADER.change_distribution_shader(etree_root, global_values, element_name)
            if 'Twist' in element_name or 'twist' in element_name and enabled_changes['shader']:
                etree_root = SHADER.change_twist_shader(etree_root, global_values, element_name)
        #%% Change light randomly
        '''
        for element_name in light_list:
            if 'Sun' in element_name or 'sun' in element_name and 'set' not in element_name and 'rise' not in element_name and and enabled_changes['light']:
                etree_root = LIGHT.change_sunlight(etree_root, global_values, element_name)
            if 'Light' in element_name or 'light' in element_name and and enabled_changes['light']:
                etree_root = LIGHT.change_environmental(etree_root, global_values, element_name)
        '''
        #%% Choose from predefined light
        if enabled_changes['light']:
            etree_root = LIGHT.choose_sunlight(etree_root, global_values, light_list)

        for element_name in water_list:
            if 'Lake' in element_name or 'lake' in element_name and enabled_changes['water']:
                etree_root = WATER.change_fractal_water(etree_root, global_values, element_name)

        for element_name in populator_list:
            if 'Tree' in element_name or 'tree' in element_name or 'Pine' in element_name or 'pine' in element_name and enabled_changes['populator']:
                etree_root = POPULATOR.change_trees_population(tags_root=etree_root, attribute=element_name, global_values=global_values)
            if 'Grass' in element_name or 'grass' in element_name and enabled_changes['populator']:
                etree_root = POPULATOR.change_grass_population(tags_root=etree_root, attribute=element_name, global_values=global_values)
        LOGGER.info(' Changes finished. Saving the file')
        file_name = 'Generation_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(os.getpid()) + f'_{n}_' + '.tgd'
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, file_name), 'wb') as tgd_file:
            etree.write(tgd_file)
        LOGGER.info(' File Saved with name {} '.format(file_name))

def render(folder_path:str, output_path:str, n_file:int = None):
    #%% import specific package for the function
    import logging
    import os
    import platform
    import subprocess
    import glob
    import basicComponent.opening as O
    import basicComponent.render as R
    import basicComponent.populator as P
    #%% Setting logging for the function
    LOGGER = logging.getLogger('RENDERING FUNCTION')
    LOGGER.info(' rendering function called')
    #%% creation of the file list
    files = glob.glob(folder_path + '/*.tgd')
    LOGGER.info(f' founded {len(files)} TGD files to be rendered')
    #%% check if the Terragen cli are configured or not
    if 'windows' in platform.system().lower():
        if os.getenv('TERRAGEN_PATH'):
            LOGGER.info(' the Terragen command line tool environmental variable exist')
        else:
            if os.path.exists('C:\Program Files\Planetside Software\Terragen 4'):
                os.environ['TERRAGEN_PATH'] = 'C:\Program Files\Planetside Software\Terragen 4'
                LOGGER.info(' Terragen 4 founded and the environmental variable was created')
            else:
                LOGGER.info(
                    ' the Terragen command line tool environmental variable does not exist. Please create it or check the installation of the software ')
    elif 'linux' in platform.system().lower():
        if os.getenv('TERRAGEN_PATH'):
            LOGGER.info(' the Terragen command line tool environmental variable exist')
        else:
            LOGGER.info(' Terragen not found, please install it')
            print(f'Please export the path for terragen software')

    #%% working on file
    for index, path in enumerate(files):
        #%% opening the file
        LOGGER.info(' opening the tgd file for render node configuration')
        etree, eroot = O.tgd_opening(path)
        render_node_list = R.get_render_node(eroot)
        for render_node_name in render_node_list:
            LOGGER.info(f' configuring the output path for rendered image, extras and mesh based on the {render_node_name}')
            #%% Rendering folder creation
            render_path = os.path.join(output_path, path.split(os.sep)[-1].split('.')[0], render_node_name)
            render_extra_path = os.path.join(render_path, 'extras')
            render_mesh_path = os.path.join(render_path, 'mesh')
            os.makedirs(render_path, exist_ok=True)
            os.makedirs(render_extra_path, exist_ok=True)
            os.makedirs(render_mesh_path, exist_ok=True)
            #%% configure the rendering
            LOGGER.info(f' configuring the {render_node_name}')
            eroot = R.change_render_paths(eroot, render_node_name, output_image_path=os.path.abspath(render_path), extra_output_image_path=os.path.abspath(render_extra_path))
            eroot = R.change_micro_render_path(eroot, output_mesh_path=os.path.abspath(render_mesh_path), render_node_name=render_node_name, attribute='MeshExporter')
            eroot = P.update_populator_position(eroot, render_node_name)
            with open(path, 'wb') as tgd_file:
                etree.write(tgd_file)
            LOGGER.info(f' update the file with the new paths for the {render_node_name}')
            LOGGER.info(f' start rendering at: {datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S")}')
            if 'windows' in platform.system().lower():
                #%% start the rendering with cmd window
                #command = f'"%TERRAGEN_PATH%/tgdcli" -p {path} -hide -exit -r -rendernode {render_node_name} -o {output_image_filename} -ox {extra_output_image_file_name}'
                command = f'"%TERRAGEN_PATH%/tgdcli" -p {path} -hide -exit -r -rendernode {render_node_name}'
                os.system(f'start /wait cmd /c "{command}"')
            elif 'linux' in platform.system().lower():
                tgp = folder_path.replace('files', 'terragen')#'./terragen' #os.getenv('TERRAGEN_PATH')
                command = f'{tgp} -p {path} -hide -exit -r -rendernode {render_node_name}'
                os.system(command)


        if n_file != 0 and index == (n_file - 1):
            break

def main():
    #%% import personalized function
    import basicComponent.global_value as G
    import basicComponent.opening as O
    #%% read the configurations
    config_file_path = args.config_file
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    #%% define the logger
    os.makedirs('./logging', exist_ok=True)
    logging.basicConfig(filename=config['logging_file_path'],level=logging.INFO)
    LOGGER = logging.getLogger("MAIN")

    if config['use_seed']:
        G.use_seed = config['use_seed']
        G.seed = config['seed']
        LOGGER.info(' seed {} applied to the execution'.format(config['seed']))
    else:
        G.use_seed = config['use_seed']
        G.seed = None
        LOGGER.info(' fixed seed deactivated')
        LOGGER.info(' random seed from sistem: ' + str(random.getstate()))

    #%% opening the basic file
    basic_file_path = config['base_file_path']
    etree, etree_root = O.tgd_opening(basic_file_path)
    LOGGER.info(' opened the {} file'.format(config['base_file_path'].split('/')[-1]))

    #%% setting ranges path
    G.ranges_terrain_path = os.path.join(config['ranges_folder_path'], config['terrain_ranges_name'])
    G.ranges_shader_path = os.path.join(config['ranges_folder_path'], config['shader_ranges_name'])
    G.ranges_populator_path = os.path.join(config['ranges_folder_path'], config['popultor_ranges_name'])
    G.ranges_light_path = os.path.join(config['ranges_folder_path'], config['light_ranges_name'])
    G.ranges_water_path = os.path.join(config['ranges_folder_path'], config['water_ranges_name'])

    #%% check enabled changes
    enable_change: dict = {
        "light": config['enable_light_change'],
        "terrain": config['enable_terrain_change'],
        "shader": config['enable_shader_change'],
        "populator": config['enable_populator_change'],
        "water": config['enable_water_change'],
    }


    LOGGER.info(' set the ranges files path for each node')

    #%% prepraring multiprocessing execution
    n_cpu = cpu_count()
    proc_list : list = []
    if config['n_files'] > int(n_cpu):
        n_file_per_proc = int(config['n_files'] / n_cpu)
    else:
        n_cpu = config['n_files']
        n_file_per_proc = 1

    if not config['use_multiprocess'] or config['n_files'] == 1:
        LOGGER.info(' Required only un processor for the generation of one file')
        file_generatioin(etree, config['n_files'], config['save_path'], global_values=G.globals_to_dict(), enabled_changes=enable_change)
    else:
        LOGGER.info(' Required the multiprocessor generation')
        LOGGER.info(' The number of processor available is {}'.format(n_cpu))
        LOGGER.info(' Required {} files to be generated, each process generate {} files'.format(config['n_files'], n_file_per_proc))
        for p in range(n_cpu):
            proc = Process(target=file_generatioin, args=(etree, n_file_per_proc, config['save_path'], G.globals_to_dict(), enable_change))
            proc_list.append(proc)
            proc.start()
        LOGGER.info(' All process generated. Waiting the termination')
        for p in proc_list:
            p.join()
    if config['activate_render']:
        render(config['save_path'], output_path=config['render_path'], n_file=config['n_render_file'])

if __name__ == '__main__':
    main()
