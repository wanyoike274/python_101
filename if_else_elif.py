#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:23:35 2022

@author: joseph wanyoike
"""

year = int(input("input year: "))
age = year-1994
if year%4 == 0:
    print("THAT YEAR IS A LEAP YEAR")
else:
    print("THATS NOT A LEAP YEAR")
        