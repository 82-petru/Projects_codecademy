# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:45:27 2019

@author: petru
"""
import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
june_mean = np.mean(june)
july_mean = np.mean(july)
june_std_deviation = np.std(june)
july_std_deviation = np.std(july)
print(june_std_deviation)

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month" + str(i) + "is" + str(np.mean(month)))
  print("The standard deviation of temperature in month" + str(i) "is" + str(np.std(month)) + "\n")