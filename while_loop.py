#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:29:45 2022

@author: wanyoike joseph
"""

i = 0
while i < 3:
    print("the value if i is: ", i)
    i+=1
print("end of loop")

num = 1
sum = 0

print("enter a number: enter 0 to exit: ")
while num != 0:
    num = float(input("number ? "))
    sum += num
    print (sum)

else:
    print("end")