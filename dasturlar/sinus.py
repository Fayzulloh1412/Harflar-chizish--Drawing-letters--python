"""Berilgan sonni sin, cos, tg, yoki ctg sini qaytaradigan dastur"""

import math

n = input("sin, cos, tg or ctg:  ")

while True:
    if n == "sin":
        x = int(input("Son kiriting:  "))
        print(math.sin(x))
    elif n == "cos":
        x = int(input("Son kiriting:  "))
        print(math.cos(x))
    elif n == "tg":
        x = int(input("Son kiriting:  "))
        print(math.tg(x))
    elif n == "ctg":
        x = int(input("Son kiriting:  "))
        print(math.ctg(x))
    
    kok = input("Davom ettirishni xohlaysizmi (Yes/No)::  ")
    if kok == "Yes":
        break
    