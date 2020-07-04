# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
import numpy as np
from matplotlib import pyplot as plt
conn_mouth_opening = 20.53
foil_widith = 20.5
tol_mouth_opening = 0.05
tol_widith_foil = 0.07
total_pitch = 19.5
tol_total_pitch = 0.05
foil_decentration = 0.5
tol_foil_decentration = 0.1
conn_middle_first_pin = 0.535
tol_middle_first_pin = 0.12
conn_pin_width = 0.18
tol_pin_width = 0.015
foil_pad_width = 0.3
tol_pad_width = 0.05

def mounting_slot():
    gap = conn_mouth_opening - foil_widith
    sigma = (2 * (tol_mouth_opening + tol_widith_foil)) / 5
    USL = gap + sigma
    LSL = gap - sigma
    N = 100000
    gap_data = np.random.normal(gap, sigma, N)
    Limit = 0
    print("Number of samples are : %s" % N)
    print("The average value is: %.3f" % gap)
    print("Standard deviation: %.3f" % sigma)
    print("The low limit is: %.3f" % LSL)
    plt.hist(gap_data, density = True, bins = 100, edgecolor = "black")
    plt.axvline(USL, color ='red', linestyle = 'solid', linewidth = 2, label = "USL")
    plt.axvline(LSL, color ='orange', linestyle = 'solid', linewidth = 2, label = "LSL")
    plt.axvline(Limit, color ='red', linestyle = 'dashed', linewidth = 2, label = "Limit")
    plt.axvline(gap, color ='black', linestyle = 'solid', linewidth = 3, label = "Mean")
    plt.legend()
    plt.show()
    total = []
    if LSL <= 0:
      for rest in gap_data:
        if rest > 0:
            continue
        total.append(rest)
        x = np.array(total, dtype=np.float64)
      print("The total is : " ,x.size)
mounting_slot()