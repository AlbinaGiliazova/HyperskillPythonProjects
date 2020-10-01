# -*- coding: utf-8 -*-
"""
Hangman is a popular yet grim intellectual game. A cruel computer hides a word 
from you. Letter by letter you try to guess it. If you fail, you'll be hanged, 
if you win, you'll survive.

A project for hyperskill.org

@author: Giliazova
"""
import random

words = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(words)
unknown = set(answer)
guessed = set()
attempts = 8

print("H A N G M A N")
while True:
    user_input = input('Type "play" to play the game, "exit" to quit: ')
    if user_input == "exit":
        break
    if user_input != "play":
        continue
    win = False
    while attempts:
        print()
        hint = ["-" if i in unknown else i for i in answer]
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue    
        if letter != letter.lower():
            print("It is not an ASCII lowercase letter")
            continue
        if not letter.isalpha():
            print("It is not an ASCII lowercase letter")
            continue        
        if letter in guessed:
            print("You already typed this letter")
        elif letter not in unknown:
            print("No such letter in the word")
            attempts -= 1    
        guessed.add(letter)    
        unknown.discard(letter)    
        if not unknown:
            print("You guessed the word!")
            print("You survived!")
            win = True

    if not attempts and not win:
        print("You lost!")