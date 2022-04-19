#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:51:53 2022

@author: wanyoike
"""

day = int(input("enter day of birthday: "))
month = int(input("enter month of birth: "))
year = int(input("enter year of birth: "))

if day == 27 and month == 4 and year == 1994:
    print("{0} {1} {2} ".format(day, month, year),"is my birthday")
else:
    print("{0} {1} {2} ".format(day, month, year),"is not my birthday")
    
#dir (__builtins__)   is used to list all 
#dir(math) displays functions in the math module