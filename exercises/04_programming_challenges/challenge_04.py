# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:50:46 2022

@author: wooih
"""

d = {}
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    age = input(f"Enter age {i+1}: ")
    d[name] = age  # store name & age in dictionary as key-value pair
    
n = input("Enter name to search: ")
print(f"{n}'s age is {d.get(n, 'unknown')}")