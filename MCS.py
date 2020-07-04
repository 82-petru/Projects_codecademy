# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:20:56 2019

@author: petru
"""
import numpy as np
from matplotlib import pyplot as plt

conn_mouth_opening = float(input("Insert connector mouth opening F: "))
foil_widith = float(input("Insert foil widith A: "))
tol_mouth_opening = float(input("Insert conn tolerance: "))
tol_widith_foil = float(input("Insert foil tolerance: "))
total_pitch = float(input("Insert Total pitch C and H: "))
tol_total_pitch = float(input("Insert tolerance for Total pitch C and H: "))
foil_decentration = float(input("Insert foil decentration B: "))
tol_foil_decentration = float(input("Insert tolerance for foil decentration: "))
conn_middle_first_pin = float(input("Insert conn middle to first pi G: "))
tol_middle_first_pin = float(input("Insert tolerance for middle to first pin: "))
conn_pin_width = float(input("Insert connector pin width I: "))
tol_pin_width = float(input("Insert tolerance pin width: "))
foil_pad_width = float(input("Insert foil pad width D: "))
tol_pad_width = float(input("Insert tolerance pad width: "))

print("")

def mounting_slot():
    gap = conn_mouth_opening - foil_widith
    sigma = (2 * (tol_mouth_opening + tol_widith_foil)) / 5
    USL = gap + sigma
    LSL = gap - sigma
    N = 10000
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
