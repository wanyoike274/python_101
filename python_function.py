#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:25:45 2022

@author: wanyoike
"""

def sum(a,b):
    if type(a) != type(b):
        print("give arguments of same type")
        return 
    print(a+b)

sum(10, 20)
sum("hello ", "world")
sum(4023.32, 4589663.2)   
sum("joseph ", 100 )