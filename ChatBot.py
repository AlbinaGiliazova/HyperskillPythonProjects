# -*- coding: utf-8 -*-
"""
A simple chat bot that asks name, guesses age, counts to a specified number and
asks a question about programming.
A project for hyperskill.org

@author: Giliazova
"""
# introduction
print("Hello! My name is Aid.")
print("I was created in 2020.")

# remind name
name = input("Please, remind me your name.\n")
print(f"What a great name you have, {name}!")

# guess age
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

# count
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
for i in range(number + 1):
    print(str(i) + " !")
    
# ask a question   
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
while True:
    s = input()
    if s == "2":
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")
        
# bye        
print("Congratulations, have a nice day!")        
    
    