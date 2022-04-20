#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:14:13 2022

@author: wanyoike joseph
"""
a = [0,1,2,3,4,5,6,7,8,9]
b = (10,20,30,40,50,60,70,80,90)
c = "123456789"

x = slice(0,5)
print(a[x])

print(a[0:5])
print(b[4:])
print(b[:6])
print(c[:])
print(c[0:5])#works on strings also
print(a[0:9:2])
print(a[::3])

print(c[-1])#last letter
print(c[-3])#third last item

print(a[::-1])#displays the items in reverse order
print(a[-3::-1])#from 3rd last element in reverse order