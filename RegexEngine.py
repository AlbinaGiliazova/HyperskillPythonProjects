# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 01:54:52 2020
Regex engine project for hyperskill.org
Supports .$\?*+^
. matches any single char
$ matches only in the end of the string
\\ is the escape sequence
? means that preceding char is repeated zero or one times
* means that preceding char is repeated zero or more times 
+ means that preceding char is repeated one or more times 
^ matches only in the beginning of the string 
In Spider IDE the input string "\" doesn't need to be escaped like "\\".
@author: Giliazova
"""
import sys
sys.setrecursionlimit(10000)

def single_char_regex(regex, char):
    # . matches any single char
    return True if regex == "" or regex == "." or regex == char else False

def compare_dot(regex, char):
    return True if char == "." else False

def compare(regex, string, match_dot=False, match_end=True):
    if len(regex) == 0:
        return True      
    # $ matches only in the end of the string
    if len(string) == 0 and regex == "$" and match_end:
        return True
    if len(string) == 0:
        return False
    # \\ is escape sequence
    if regex.startswith("\\"):
        return escape(regex, string) 
    if len(regex) >= 2 and regex[1] in "?*+":  # checked twice
        return repetition(regex, string)       
    if match_dot == False and single_char_regex(regex[0], string[0]) == False: 
        return False
    if match_dot == True and compare_dot(regex[0], string[0]) == False:
        return False
    return compare(regex[1:], string[1:])

def repetition(regex, string):
    # ? means that preceding char is repeated zero or one times
    if regex[1] == "?":
        return compare(regex[2:], string) or\
            compare(regex[0] + regex[2:], string)
    # * means that preceding char is repeated zero or more times    
    if regex[1] == "*":
        return compare(regex[2:], string) or\
            compare(regex, string[1:])    
    # + means that preceding char is repeated one or more times    
    if regex[1] == "+":
        return compare(regex[0] + regex[2:], string) or\
            compare(regex, string[1:])    

def escape(regex, string):
    if regex == "\\":
        return string.startswith("\\")
    if regex[1] in "?*+":
        return compare(regex[1:], string)
    if regex[1] == ".":  
        return compare(regex[1:], string, match_dot=True)  
    if regex[1] == "$":
        return compare(regex[1:], string, match_end=False)
    if regex.startswith("\\\\"):
        if regex == "\\\\":
            return string.startswith("\\")        
        if regex[2] in "?*+":
            return repetition(regex[1:], string)
        return string.startswith("\\") and compare(regex[2:], string[1:])
    return string.startswith("\\") and compare(regex[1:], string[1:])     
           
def regex_engine(regex, string):
    # ^ matches only in the beginning of the string - no escape
    if regex.startswith("^"):
        return compare(regex[1:], string)    
    if compare(regex, string):
        return True
    if len(string) == 0:
        return False
    return regex_engine(regex, string[1:])
    
regex, string = input().split("|")
print(regex_engine(regex, string))