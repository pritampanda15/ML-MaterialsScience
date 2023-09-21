import pickle
import csv
import functools as f
import numpy as np
import pandas as pd
from pymatgen import MPRester
from copy import deepcopy

API_KEY = "API_Key"
mpr = MPRester(API_KEY)

print('Querying MP database...')
entries = mpr.query({
    "elements": {
        '$in': [
            u'Sc', u'Ti', u'V', u'Cr', u'Mn', u'Y', u'Zr', u'Nb', u'Mo', u'Mo', u'Hf', u'Ta', u'W', u'C', u'N'
        ]
    }
}, ['material_id', 'pretty_formula', 'spacegroup', 'nelements','formation_energy_per_atom', 'e_above_hull', 'volume', 'density', 'nsites', 'energy', 'energy_per_atom','total_magnetization','elasticity','band_gap'])
print(len(entries))
data = np.array(entries)
data
df=pd.DataFrame(data=data)
df.to_csv('dataset.csv', index = False)
