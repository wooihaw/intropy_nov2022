# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:24:16 2022

@author: wooih
"""
#%% Examples of using Lambda function with sorted

alist = ['ID12', 'ID3', 'ID43', 'ID112', 'ID57']

print(sorted(alist))

print(sorted(alist, key=lambda x: int(x[2:])))

#%% Example of using lambda function with max()

paper_size = ['A1', 'A2', 'A3', 'A4', 'A5']

print(max(paper_size))

print(max(paper_size, key=lambda x: -int(x[1:])))

#%% Using lambda function with map()
sqr1 = [i*i for i in range(1, 11)]
sqr2 = list(map(lambda i:i*i, range(1, 11)))

print(sqr1)
print(sqr2)

names = ['ali', 'bala', 'chan', 'david']
cap_names1 = [i.capitalize() for i in names]
cap_names2 = list(map(lambda i: i.capitalize(), names))
print(cap_names1)
print(cap_names2)

#%% Using lambda function with filter()
odd1 = [i for i in range(10) if i%2]
odd2 = list(filter(lambda j:j%2, range(10)))
print(odd1, odd2, sep='\n')

words = ['bell', 'ant', 'cat', 'eggs', 'fish']
vowel1 = [w for w in words if w[0] in 'aeiou']
vowel2 = list(filter(lambda y: y[0] in 'aeiou', words))
print(vowel1, vowel2, sep='\n')

#%% Import module
from math import sin, cos, pi

print(sin(pi/2))
print(cos(pi/2))