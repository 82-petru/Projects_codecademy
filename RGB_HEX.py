# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
print("Build a calculator to convert RGB in Hexadecimal using Bitwise. Program should do the following: prompt the user, ask the user to input RGB or Hex values, use Bitwise operators and shifting in order to convert the values ")
def rgb_hex():
  invalid_msg = "The values entered are not valid"
  red = int(input("Enter the red value(R): "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(input("Enter the green value(G): "))
  if green < 0 or green > 255:
    print(invalid_msg)
    return 
  blue = int(input("Enter the blue value(B): "))
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return 
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())
def hex_rgb():
  hex_val = input("Enter a color six hexadecimal digits: ")
  if len(hex_val) != 6:
    print("Invalid digits")
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits 
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8 
  red = hex_val % two_hex_digits 
  print("rgb(%s, %s, %s)" % (red, green, blue))
def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print("RGB to Hex....")
      rgb_hex()
    elif option == "2":
      print("Hex to RGB...")
      hex_rgb()
    elif option == "X" or option == "x":
      break 
    else:
      print("Error.")
convert()