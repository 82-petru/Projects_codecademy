# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
"Build a program that rolls a pair of dice and then ask the usser for input to guess the sum. If the sum is equal to the total value of the dice roll, user wins otherwise computer wins  "
#import randint from random #from module import function
#import sleep from time 
"Build a program that rolls a pair of dice and then ask the usser for input to guess the sum. If the sum is equal to the total value of the dice roll, user wins otherwise computer wins  "
from random import randint #from module import function
from time import sleep

def get_user_guess():
  guess = int(input("Guess a value: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value for number of sides: %s" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("your number is invalid")
  else:
    print("Rolling....")
    sleep(2)
    print("First Roll is: %s" % first_roll)
    sleep(1)
    print("Second roll is: %d" % second_roll)
    total_roll = first_roll + second_roll 
    print("The total dice roll is: %d" % total_roll)
    print("Result....")
    sleep(1)
    if guess == total_roll:
      print("You won buddy...")
    else:
      print("You lost :)")
roll_dice(6)