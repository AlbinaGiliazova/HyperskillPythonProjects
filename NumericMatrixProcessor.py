# -*- coding: utf-8 -*-
"""
A numeric processor which can add matrices, multiply a matrix by a constant or
by another matrix, transpose a matrix in four different ways, calculate
a determinant and inverse a matrix.

A project for hyperskill.org

@author: Giliazova
"""
# functions in an alphabetical order
def calculate_determinant_menu():
    A = read_matrix("", flag_float=True, flag_string=True)
    if not check_square_matrix(A):
        print("You need to enter a square matrix.")
    else:    
        print("The result is:")
        print(determinant(A))

def check_equal_dimensions(A, B):
    if len(A) != len(B):
        return False
    if len(A[0]) != len(B[0]):
        return False
    return True

def check_int_matrix(A):
    for row in A:
        for a in row:
            if int(a) != a:
                return False
    return True  

def check_multiply_dimensions(A, B):
    if len(A[0]) != len(B):
        return False
    return True   

def check_square_matrix(A):
    return len(A) == len(A[0])      

def convert_to_int(A):
    res = []
    for i, row in enumerate(A):
        res.append([])
        for a in row:
            res[i].append(int(a))
    return res    

def determinant(A):
    if len(A) == 1:
        if not isinstance(A[0], list):
            return A[0]
        else:
            return A[0][0]
    res = 0
    for j, a in enumerate(A[0]):  
        res += (-1) ** j * a * determinant(minor(A, 0, j))    
    return res    

def inverse_matrix(A):
    res = []
    for i, row in enumerate(A):
        res.append([])
        for j, a in enumerate(row):  
            res[i].append((-1) ** (i + j) * determinant(minor(A, i, j)))    
    res = transpose_matrix(res, "1")
    return multiply_by_const(res, 1 / determinant(A))

def inverse_matrix_menu():
    A = read_matrix("", flag_float=True, flag_string=True)
    print("The result is:")
    if determinant(A) == 0:
        print("This matrix doesn't have an inverse.")
    else:    
        print_matrix(inverse_matrix(A))
        print()

def main_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")       
    option = input("Your choice: ")
    if option == "1":
        sum_matrices_menu()
    elif option == "2":
        multiply_by_const_menu()
    elif option == "3":
        multiply_matrices_menu()
    elif option == "4":
        transpose_matrix_menu()
    elif option == "5":
        calculate_determinant_menu()
    elif option == "6":
        inverse_matrix_menu()
    return option

def minor(A, i, j):  
    res = []
    ind_m = -1
    for m, row in enumerate(A):
        if m == i:
            continue
        res.append([])
        ind_m += 1
        for n, a in enumerate(row):
            if n == j:
                continue
            res[ind_m].append(a)
    return res        

def multiply_by_const(A, c):
    res = []
    for i, row in enumerate(A):
        res.append([])
        for a in row:
            res[i].append(a * c)
    return res  

def multiply_by_const_menu():
    A = read_matrix("", flag_float=True)
    if check_int_matrix(A):  # checked twice
        c = int(input())
    else:    
        c = float(input())
    print("The result is:")        
    print_matrix(multiply_by_const(A, c))
    print()
       
def multiply_matrices(A, B):
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(len(B[0])):
            s = 0
            for k in range(len(A[0])):               
                s += A[i][k] * B[k][j]
            res[i].append(s)    
    return res        
    
def multiply_matrices_menu():
    A = read_matrix("first ", flag_float=True)   
    B = read_matrix("second ", flag_float=True)
    if not check_multiply_dimensions(A, B):
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        print_matrix(multiply_matrices(A, B)) 
    print()          

def print_matrix(A, num_digits=0):
    if num_digits:
        if isinstance(A[0], list):
            for i, row in enumerate(A):
                for j, a in enumerate(row):
                    print(f"{a:.{num_digits}f}", end = " ")
                print()    
        else:
            for i, row in enumerate(A):       
                print(f"{a:.{num_digits}f}", end = " ")
                print()    
    else:
        for row in A:
            print(*row)                 
        
def read_matrix(string, flag_float=False, flag_string=False):
    if flag_string:
        s = "Enter matrix size: "
    else:    
        s = f"Enter size of {string}matrix: "
    num_rows, num_cols = (int(i) for i in input(s).split())
    s = f"Enter {string}matrix:" 
    res = []
    for _ in range(num_rows):
        if flag_float:
            res.append([float(i) for i in input().split()])
        else:    
            res.append([int(i) for i in input().split()])
    if flag_float:
        if check_int_matrix(res):
            res = convert_to_int(res)        
    return res 

def sum_matrices(A, B):
    res = []
    for i, row in enumerate(A):
        res.append([])
        for j, a in enumerate(row):
            res[i].append(a + B[i][j])
    return res  

def sum_matrices_menu():
    A = read_matrix("first ", flag_float=True)   
    B = read_matrix("second ", flag_float=True)
    if not check_equal_dimensions(A, B):
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        print_matrix(sum_matrices(A, B))
    print()    

def transpose_matrix(A, option):
    res = []
    if option == "1":  # main diagonal
        for i, row in enumerate(A):
            for j, a in enumerate(row):
                res.append([])
                res[j].append(a)
    elif option == "2":  # side diagonal
        for i, row in enumerate(A[::-1]):
            for j, a in enumerate(row[::-1]):
                res.append([])
                res[j].append(a)
    elif option == "3":  # vertical line
        for i, row in enumerate(A):
            res.append([])
            for j, a in enumerate(row[::-1]):
                res[i].append(a)
    elif option == "4":  # horizontal line
        for i, row in enumerate(A[::-1]):
            res.append([])
            for a in row:
                res[i].append(a)
    return res        
            
def transpose_matrix_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    option = input("Your choice: ")
    A = read_matrix("", flag_float=True)
    print("The result is:")
    print_matrix(transpose_matrix(A, option))
    print()
            
# main
while True:
    option = main_menu()
    if option == "0":
        break