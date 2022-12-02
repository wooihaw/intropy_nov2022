# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:47:25 2022

@author: wooih
"""

# Rabbits -> r
# Chickens -> c
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits")