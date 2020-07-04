# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:27:06 2019

@author: petru
"""
from random import randint
board = []
#use build in print function to make grid for "ocean"
#use for loop to create 5 rows and inside the loop use function append to create a list and multiply by 5 
for loop in range(0, 5):
    board.append(["O"] *5)
#create a function with one argument and below a for loop to'iterate each row' = repeta fiecare rand
def print_board(board_in):
    for row in board:
#use join method to combain strings into the list function = .join(list) " " to remove quotes 
     print(" " .join(row))
     
print_board(board)

#hide the battleship in a random location, we have two battleship so we must use two variables
#to store ship location
#The random module is  able to generate random numbers, which is randint(start, end).

def random_row(board_in):
    return randint(0, len(board_in)- 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

#store the coordonate for the ship in two variables 
ship_row = random_row(board)
ship_col = random_col(board)
#debugging share the coordonate location of battleship
print(ship_row)
print(ship_col)
#to repeat the guess four times
for turn in range(4):
 print("Turn", turn + 1)
 guess_row = int(input("Guess Raw: "))
 guess_col = int(input("Guess Col: "))

#check if the usser guess it right 
 if guess_row == ship_row and guess_col == ship_col:
  print("Congratulation! you sank my battleship")
  break
#in case of fail to receive mesage and also to mark the place on "ocean"
 else:   
#guess out of the board,to check if it is outside the board
  if guess_row not in range(5) or guess_col not in range(5):
   print("Ops, that's not even in the ocean")
  elif board[guess_col] [guess_row] == "X":
   print("You already guess it")
  else:
   print("You missed my battleship")
   board [guess_row] [guess_col] = "X"
  if turn == 3:
    print("Game Over")
print_board(board)
    



