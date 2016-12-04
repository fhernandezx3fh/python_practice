'''The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6.'''
from random import randint


header_txt = "Dice Rolling Simulator"
prompt_txt = "Would you like to roll again? (y/n)\n> "
print header_txt.center(50, "*")

def roll():
  return "You rolled a: {}".format(randint(1, 6))

def roll_dice():
  
  print roll()
  while (raw_input(prompt_txt).capitalize() == "Y"):
    print roll()
  print ("Exiting " + header_txt).center(50, "*")

roll_dice()
