# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:55:10 2019

@author: petru
"""

print("Start the program")

option = input("Enter C for circle and T for Triangle: ")

if option == 'C':
  radius = float(input("Enter radius: "))
  area = 3.14159 * radius ** 2
  print(" For radius %s the area of the circle is: %s" % (radius, area))
  
elif option == 'T':
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  area = 0.5 * base * height
  print(" For triangle %s and %S the area is: %s" % (base, height, area))
  
else:
  print("Program do not recognize input")

  
print("Program is closed")