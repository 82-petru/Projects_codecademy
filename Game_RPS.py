# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
print("Prompt the user Rock, Paper, Scissor, instruct computer randomnly select either rock, paper, scissor compare the result between user and computer choice and finalize to determine who's the winner")
from random import randint 
option = ["ROCK", "PAPER", "SCISSORS"]
message ={"tie" : "Yawn is a tie", "won" : "Yay you won", "lost" : "Aww you lost"}
def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer choice: %s" % computer_choice)
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == option[0] and computer_choice == option[2]:
    print(message["won"])
  elif user_choice == option[1] and computer_choice == option[0]:
    print(message["won"])
  elif user_choice == option[2] and computer_choice == option[1]:
    print(message["won"])
    
  else:
    print(message["lost"])
def play_RPS():
  print("Rock, Paper, or Scissors")
  user_choice = input("Enter rock, paper or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = option[randint(0,2)]
  decide_winner(user_choice, computer_choice)
play_RPS()