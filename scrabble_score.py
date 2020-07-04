# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:07:23 2019

@author: petru
"""
#first game with python 2
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, }

def scrabble_score(word):
    word = word.lower()
    total = 0 
    for loop in word:
         total += score[loop] 
    return total
print(scrabble_score("tataia"))

#second game with python 3

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {k : v for k, v in zip(letters, points)}
#print(letter_to_points)
letter_to_points.update({" " : 0})

def score_word(word):
  word = word.upper()
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
  return point_total
#print(score_word('BROWNIE'))   

player_to_words = {"player1" : ["blue", "tennis", "exit"], "wordNerd" : ["earth", "eyes", "machine"], "Lexi Con" : ["eraser", "belly", "husky"], "Prof Reader" : ["zap", "coma", "period"]}
#print(player_to_words)

def play_word(player, word):
  player_to_words.update({player : word})
  return player_to_words 
print(play_word("jonny", ["xenia", "vera", "petru", "codacademy"]))

print("")

def update_point_totals(players_list):
  player_to_points = {}
  for player, words in players_list.items():
    player_points = 0
    for word in words:
      calculate_letter = score_word(word)
      player_points += calculate_letter
      player_to_points[player] = player_points
  return player_to_points
print(update_point_totals(player_to_words))
