#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:59:09 2022

@author:  joseph wanyoike
"""

# sets; unordered collection with no duplicate elements and no indexing
# curly braces ae used

a = {1,2,2,2,5,5,9,9,6,6}
print(a)#duplicates are not printed
print(len(a))
a.add(10)
a.update([15,18,14])
print(a)
a.remove(18)#will through an exception if try to remove a nonexistence value
a.discard(17)#will not through an error in that case as above
print(a)
a.pop()#removes a random element 
#other function; del, clear
name = set(("joseph", "wanyoike", "njoroge"))#another way to create sets
print(name)
#mathematical sets
b = {10,20,30,40,50,60}
c = {50,60,70,80,90,100}
print (b|c) #union---all elements present in sets b or c
print (b.union(c))#similar as above

print (b&c)#intersection of b and c --elements in both sets
print(b.intersection(c))#similar as above

print (b-c)#difference --elements in b and not in c
print (c-b)#difference --elements in c and not in b

print(b.difference(c))#similar as above
print(c.difference(b))#similar as above

print(b^c)#symmetric difference---elements in b and not in c AND those in c and not in b
print(b.symmetric_difference(c))#same as above

#print(b[1]) will result to an error reason sets are not indexed