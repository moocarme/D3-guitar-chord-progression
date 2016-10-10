#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 20:19:22 2016

@author: matt-666
"""

import pandas as pd
import json
import numpy as np

data = pd.read_csv('GuitarChordProgCount_2.csv')

prog_dict = {'nodes':[], 
             'links':[]}

data = data.drop(data.index[data.group == 'H'])
chord_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7, 'o':8}
chord_dict2 = {'A':1,'Em':2,'C':3,'Dm':4,'E':5,'D':6,'G':7, 'F':8, 
               'Bm':9, 'F#':10, 'Am':11, 'other':12, 'B':13, 'F#m':14, 'Bb':15}

for chord in data.has.unique():
    prog_dict['nodes'].append({'id':chord, 'group':chord_dict[chord[0]]})
    
for index, row in data.iterrows():
    if (np.log(row['count'])/3) > 0:
        prog_dict['links'].append({'source':row['has'], 
                                   'target':row['prefers'], 
                                   'value':(np.log(row['count'])/3)})
with open('chord_prog_links_3.json', 'wb') as fp:
    json.dump(prog_dict, fp)            