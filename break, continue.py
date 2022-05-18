#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:11:31 2022

@author: wanyoike joseph
"""

a = range(0, 10)
for x in a:
    if x == 3:
        break
    print(x)

print("-------------------------------")
    
i = 0
while i < 5:
    if i ==3:
        break
    print(i)
    i += 1

print("continue")
    
a = range(0, 10)
for t in a:
    if t == 3:
        continue
    print(t)

print("-------------------------------")
    
b = 0
while b < 5:
    b += 1
    if b ==3:
        continue
    print(b)