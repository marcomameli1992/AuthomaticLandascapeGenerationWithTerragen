#%% seed variables
use_seed: bool
seed: int

#%% base ranges folder path
ranges_folder_path: str

ranges_populator_path: str
ranges_terrain_path: str
ranges_shader_path: str
ranges_light_path: str
ranges_water_path: str

# normalization factor for the colour
colour_normalization_factor: int = 255

def globals_to_dict() -> dict:
    dictionary : dict = {
        'use_seed': use_seed,
        'seed': seed,
        'ranges_populator_path': ranges_populator_path,
        'ranges_terrain_path': ranges_terrain_path,
        'ranges_shader_path': ranges_shader_path,
        'ranges_light_path': ranges_light_path,
        'ranges_water_path': ranges_water_path,
        'colour_normalization_factor': colour_normalization_factor
    }

    return dictionary