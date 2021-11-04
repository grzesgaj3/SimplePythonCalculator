import time
import os
from math import *


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def discriminant(a,b,c):
    return b**2-4*a*c

def funkcja_1():
    global a,b,c
    a = int(input("Give a"))
    b = int(input("Give b"))
    c = int(input("Give c"))
    input("Press any button to go back")
    menu()
def funckja_2():
    print("The value of discriminant is: ")
    print(discriminant(a,b,c))
    input("Press any button to go back")
    menu()
def funkcja_3():
    clearConsole()
    if discriminant(a,b,c)>0:
        print(-b-sqrt(discriminant(a,b,c))/2*a)
        print(-b+sqrt(discriminant(a,b,c))/2*a)
    elif discriminant(a,b,c)==0:
        print(-b/2*a)
    else:
        print("There are no zero's of that function")
    input("Press any button to go back")
    menu()
def funckja_4():
    clearConsole()
    print("Test1")
    menu()
def menu():
    interaction = 0
    clearConsole()
    print("""Quadrantic Function  Calculator program ax²+bx+c)
4.11.2021 v0.0.1
""")
    print("Menu")
    print("1-Define variables")
    print("2-Calculate discriminant")
    print("3-Calculate zero's of a function")
    print("4-Check how many solutions requested function has")
    interaction = int(input(" "))
    if interaction == 1:
        funkcja_1()
    elif interaction==2:
        funckja_2()
    elif interaction==3:
        funkcja_3()
    elif interaction==4:
        funkcja_4()
    else:
        menu()

menu()