# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:41:16 2019

@author: petru
"""
print("""Project to find mode, mean and median cost of one bedroom 
apartment in three of five New York boroughs, 
check cost living between places
""")
# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# Add mean calculations below 
print(brooklyn_one_bed)
