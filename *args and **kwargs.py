#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:40:22 2022

@author: wanyoike
"""

#default arguments, *args and **kwargs 
#(variable-length arguments

def student (name="jose", age=28):
    print("name: ", name)
    print("age", age)
    
student("wanyoike")
print("--------------------------------------")

def student (name, age, *marks):#if we dont put that 
#asteriks it will throw an error like
#student() takes 3 positional arguments but 8 were
    print("name: ", name)
    print("age", age)
    print("marks", marks)
    
    
student("njoroge", 28, 98,89,96,98,78,99)
print("---------------------------------------------")

def student (name, age, **marks):#if we dont put that 
#asteriks it will throw an error like
#student() takes 3 positional arguments but 8 were
    print("name: ", name)
    print("age", age)
    print("marks", marks)
    for key, value in marks.items():
        print(key, " ", value)
    
    
student("njoroge", 28, maths=98,computer=99,eng=96)