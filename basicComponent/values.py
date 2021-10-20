#%% import section
import os

#%% random globals value
global use_seed
global seed
use_seed: bool
seed: int

#%% base ranges folder path
ranges_folder_path: str

#%% individual ranges file name
global ranges_populator_path
global ranges_terrain_path
global ranges_shader_path
global ranges_light_path
global ranges_water_path
ranges_populator_path: str
ranges_terrain_path: str
ranges_shader_path: str
ranges_light_path: str
ranges_water_path: str

#%% random settings
def set_seed(iseed:int):
    global seed
    seed = iseed

def set_use_seed(iuse_seed:bool):
    global use_seed
    use_seed = iuse_seed

#%% ranges settings
def set_ranges_folder_path(path: str):
    global ranges_folder_path
    ranges_folder_path = path

def set_light_value_path(name:str):
    global ranges_light_path
    ranges_light_path = os.path.join(ranges_folder_path, name)

def set_water_value_path(name:str):
    global ranges_water_path
    ranges_water_path = os.path.join(ranges_folder_path, name)

def set_shader_value_path(name:str):
    global ranges_shader_path
    ranges_shader_path = os.path.join(ranges_folder_path, name)

def set_terrain_value_path(name:str):
    global ranges_terrain_path
    ranges_terrain_path = os.path.join(ranges_folder_path, name)

def set_populator_value_path(name:str):
    global ranges_populator_path
    ranges_populator_path = os.path.join(ranges_folder_path, name)
