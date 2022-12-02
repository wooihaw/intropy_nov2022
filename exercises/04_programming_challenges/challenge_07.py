# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:41:24 2022

@author: wooih
"""

filename = 'data/scores.csv'

with open(filename, 'r', encoding='utf-8') as f:
    rawdata = f.readlines()
    
    print(rawdata)
    
    rawdata.pop(0)
    
    data = [i.strip().split(',') for i in rawdata]
    
    print(data)
    
    names = [i[0] for i in data]
    scores = [i[1] for i in data]
    
    players = sorted(set(names))
    
    d = {p:[] for p in players}
    
    for i, j in zip(names, scores):
        for k in d:
            if i == k:
                d[k].append(j)
    
    output = 'name,high_score\n'
    for k in d:
        output = output + f"{k},{max(d[k])}\n"
        
    print(output)
    
    with open('data/high_scores.csv', 'w') as g:
        g.write(output)
        
    