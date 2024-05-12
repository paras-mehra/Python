# <================ Python Function ================>

# In Python, function is a group of related statements that performs a specific task
# Functions help break our program into smaller and modular chunks. As our Program grows larger and 
# larger, function make it more organized and manageable.
# Category of Function
# Built-in
# Modules
# User-defined

# ==================================================================================

# -----------------
# Built-in Function
# -----------------
# int() / float() / eval()
# input()
# min() / max()
# abs()
# type()
# len()
# round()
# range()

# ==================================================================================

# ---------------
# Python Modules
# ---------------
# A modules is a file containing functions and variables defined in separate files. A Module is simply a file that contains Python code. When we break a program into modules, each module should contain functions that perform related tasks.

# Important modules
# math
# random
# string

# import math as m
# print(dir(m))
# print(m.pi)

# from math import cos, pi
# from math import *
# print(cos(11))
# print(pi)

# ==================================================================================

# ---------------------- 
# User-defined functions
# ---------------------- 

# def greet(name, hwz="how are you?"):
#     print("Hello", name, hwz)
# greet("Paras", "What are you doing?")


def greet(names):
    for name in names:
        print("Hello", name)
list = ["Karan","Paras","Bishu","Mukul"]
greet(list)




