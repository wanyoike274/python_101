#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:39:31 2022

@author: wanyoike
"""

#ordered set of values
#define using square brackets
x = [3,4,5,6,7,8,9,9]
y = ["joseph", 27, [780,330]]#can store any data type
print(x)
print(x[5])#index 5
print(y[2])
print(len(y))
print (y.insert(2, "data science"), y)#insert "data... on" index 2
#insert accepts 2 arguments ,index and value to insert
#print (x.remove(9))#removes 9
print(x.pop())
#other functions ...del, sort, clear, reverse, append(add a value)
#copy, count,