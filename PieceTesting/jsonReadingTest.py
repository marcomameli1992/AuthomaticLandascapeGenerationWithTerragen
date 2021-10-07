import os
import json
import random

range_value_path = os.path.join('..', 'basicComponent', 'ranges', 'terrain.json')

with open(range_value_path, 'r') as range_file:
    ranges = json.load(range_file)

print(ranges['fractal_terrain']['enable'])

print(random.uniform(ranges['fractal_terrain']['feature_scale_minimum'], ranges['fractal_terrain']['feature_scale_maximum']))