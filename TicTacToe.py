# -*- coding: utf-8 -*-
"""
Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place.
 One of the players plays as 'X', and the other player is 'O'. 'X' plays first, 
 then the 'O' side plays, and so on.

The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) 
wins.

@author: Tigrisha
"""
# functions in an alphabetical order
def check_col(field, i, win_x, win_o):
    if field[0][i] == "X" and field[1][i] == "X" and field[2][i] == "X":
        win_x = True
    elif field[0][i] == "O" and field[1][i] == "O" and field[2][i] == "O":
        win_o = True
    return win_x, win_o 

def check_diag(field, win_x, win_o):
    if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        win_x = True
    elif field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        win_o = True
    if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
        win_x = True
    elif field[0][2] == "O" and field[1][1] == "O" and field[2][0] == "O":
        win_o = True        
    return win_x, win_o        

def check_row(row, win_x, win_o):
    if row[0] == "X" and row[1] == "X" and row[2] == "X":
        win_x = True
    elif row[0] == "O" and row[1] == "O" and row[2] == "O":
        win_o = True
    return win_x, win_o     

def count_symbols(cell, num_x, num_o, num__):
    if cell == "X":
        num_x += 1
    elif cell == "O":
        num_o += 1
    elif cell == "_" or cell == " ":
        num__ += 1
    else:
        num__ += 1
    return num_x, num_o, num__

def evaluate_field(num_x, num_o, num__, win_x, win_o):
    if win_x and win_o:
        print("Impossible")
        return True
    elif num_x - num_o >= 2 or num_o - num_x >= 2:
        print("Impossible")
        return True
    elif not win_x and not win_o and num__:
        # print("Game not finished")
        return False
    elif not win_x and not win_o and not num__:  
        print("Draw")
        return True
    elif win_x:
        print("X wins")
        return True
    elif win_o:
        print("O wins")
        return True
    return True

def print_field(field):
    print("---------")
    print("|", " ".join(field[0]), "|")
    print("|", " ".join(field[1]), "|")
    print("|", " ".join(field[2]), "|")
    print("---------") 
    
def process_coords(coords, field):
    try:
        coords = [int(i) for i in coords.split()]
    except ValueError:
        print("You should enter numbers!")
        return None
    if len(coords) != 2:
        print("You should enter 2 numbers!")
        return None
    if coords[0] not in [1, 2, 3] or coords[1] not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
        return None
    coords = translate_coords(coords)
    if field[coords[0]][coords[1]] == "X" or field[coords[0]][coords[1]] == "O":
        print("This cell is occupied! Choose another one!")
        return None
    return coords
    
def process_field(field):
    num_x, num_o, num__ = 0, 0, 0
    win_x, win_o = False, False
    for j, row in enumerate(field):
        win_x, win_o = check_row(row, win_x, win_o)  
        for i, cell in enumerate(row):        
            num_x, num_o, num__ = count_symbols(cell, num_x, num_o, num__)
            if j == 0:
                win_x, win_o = check_col(field, i, win_x, win_o)
            if j == 1 and i == 1:
                win_x, win_o = check_diag(field, win_x, win_o)
    return evaluate_field(num_x, num_o, num__, win_x, win_o)    

def start():
    field = "         "
    field = [list(field[:3]), list(field[3:6]), list(field[6:])]
    print_field(field)    
    return field

def translate_coords(coords):
    return 3 - coords[1], coords[0] - 1

def update_field(field, coords, player):
    field[coords[0]][coords[1]] = player
    player = "X" if player == "O" else "O"
    return field, player

# main
field = start()
player = "X"
while True:
    coords = None
    while not coords:
        coords = process_coords(input("Enter the coordinates: "), field)
    field, player = update_field(field, coords, player)
    print_field(field)
    game_end = process_field(field)
    if game_end:
        break
    