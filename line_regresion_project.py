# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:46:16 2020

@author: petru
"""
#http://localhost:8888/notebooks/Reggie_Linear_Regression_Skeleton.ipynb#Part-1:-Calculating-Error
# m is the slope of the line and b is the intercept, where the line crosses the y-axis
#linear regresion formula 
def get_y(m,b,x):
    y = m*x + b
    return y
#point argument is intersection of [x,y]
#this funct calculate distance from observation and line 
def calculate_error(m, b, point):
    x_point, y_point = point
    y_value = get_y(m,b,x_point) 
    distance = abs(y_point - y_value)
    return distance

#next function is to compare the impact of different data on X axis 
"""the function will take slope interception point and set of datapoints for point which 
describes the best fit line """
def calculate_all_error(m, b, points):
    total_error = 0 
    for point in points:
        error_pointline = calculate_error(m, b, point)
        total_error += error_pointline
    return total_error
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print(calculate_all_error(0.6, 1.7, datapoints))

#Try a bunch of slopes and intercepts which one produces the smallest error create a list of values
possible_ms = [m_slope * 0.1 for m_slope in range(-100, 101)]
possible_bs = [0.1 * bs for bs in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float('inf')
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error_calculate = calculate_all_error(m, b, datapoints)
        if error_calculate< smallest_error:
            smallest_error = error_calculate
            best_m = m
            best_b = b 
print("Rounded values: {:5.3f}, {:5.3f}, {:5.3f} ".format(smallest_error, best_m, best_b))



    




