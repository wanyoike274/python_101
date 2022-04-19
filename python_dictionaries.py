#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:23:05 2022

@author: wanyoike joseph
"""

#dictionaries ...list of pairs
a = {"name": "joseph", "age": 27, "language": "python"}
#name, age, language are keys...keys can be of any type
#joseph, 27, python are values
print(a["name"])
print(len(a))
print(a.get("age"))

print(a.keys())#lista all keys
print(a.items())
#other function ...pop, del, update