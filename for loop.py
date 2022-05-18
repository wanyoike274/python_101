#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:58:32 2022

@author: wanyoike
"""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list
b = (0,10,20,30,40,50,60,70,80,90,)#tuple
c = {0,100,200,300,400,500,600,700,800,900}
e = {"name": "wanyoike", "age":28}

for x in a:
    print(x)

for x in b:
    print(x)
    
for y in e.keys():
    print(y)
for keys, value in e.items():
    print(keys, "", value)
print(0 in a)

for x in range(6):
    print(x)
#remember you can use else with for loop