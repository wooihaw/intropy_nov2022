# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:05:58 2022

@author: wooih
"""

s = '''Peter Piper picked a peck of pickled peppers. 
A peck of pickled peppers Peter Piper picked. 
If Peter Piper picked a peck of pickled peppers, 
where is the peck of pickled peppers Peter Piper picked?'''

# Normalize text to all lower case and remove punctuation
t = [c.lower() if c.isalpha() else " " for c in s]

# Join the characters back to form words
u = ''.join(t)
print(u)

# Split words into individual items in a list
w = u.split()
print(w)

wf = {}  # dictionary to store word frequency
for i in sorted(set(w)):
    wf[i] = w.count(i)

print(wf)