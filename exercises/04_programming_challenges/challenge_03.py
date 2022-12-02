# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:44:45 2022

@author: wooih
"""

s1 = set(range(1, 101))
s2 = set(range(5, 101, 5))
s3 = set(range(7, 101, 7))

result = s1 - (s2 | s3)
print(sorted(result))