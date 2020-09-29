# -*- coding: utf-8 -*-
"""
Rock, paper, scissors is a well-known hand game. Each one of two players 
simultaneously forms one of three shapes with their hands, and then, 
depending on the chosen shapes, the winner is determined: rock beats scissors, 
paper wins over rock, scissors beat paper.
The game is widely used to make a fair decision between equal options.
This game supports custom number of playable options to choose from.
The player can enter them like this: 
rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Print !exit to exit the game.

@author: Giliazova
"""
import random

player = input("Enter your name: ")
print("Hello,", player)

try:
    file = open("rating.txt")  
except FileNotFoundError:
    file = open("rating.txt", "w+")
    
rating = 0 
for line in file:
    line = line.split()
    if line[0] == player:
        rating = int(line[1])
        break   
file.close() 

options = input()
if not options:
   options = ["rock", "paper", "scissors"] 
else:
   options = [i for i in options.split(",")]
   if len(options) == 1:
       options = options.split()
    
d = {}
for i, opt in enumerate(options):
    lst = []
    if i != len(options) - 1:
        lst.extend(options[i + 1:])
    if i != 0:
        lst.extend(options[:i])
    if len(lst) % 2 == 0:    
        d[opt] = [lst[:int(len(lst) / 2)], lst[int(len(lst) / 2):]]  # is beated, beats  
    else:
        d[opt] = [lst[:int(len(lst) / 2)], lst[int(len(lst) / 2):]]

print("Okay, let's start")

while True:
    comp_choice = random.choice(options)
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    if user_input == "!rating":
        print(rating)
        continue
    elif user_input not in options:
        print("Invalid input")
        continue

    if user_input == comp_choice:
        print(f"There is a draw ({comp_choice})")
        rating += 50
    elif comp_choice in d[user_input][1]:
        print(f"Well done. The computer chose {comp_choice} and failed")
        rating += 100
    else:
        print(f"Sorry, but the computer chose {comp_choice}")   

flag = False
with open("rating.txt", "r") as f:
    lines = f.readlines()
with open("rating.txt", "w") as f:
    for line in lines:
        if line.split()[0] != player:
            f.write(line) 
        else:
            f.write(player + " " + str(rating) + "\n")
            flag = True
    if not flag:
        f.write(player + " " + str(rating) + "\n")        
            