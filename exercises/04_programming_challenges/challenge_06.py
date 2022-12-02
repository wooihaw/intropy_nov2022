# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:19:16 2022

@author: wooih
"""

def mean(data: list) -> float:
    return sum(data) / len(data)

def median(data: list) -> float:
    sdata = sorted(data)
    if len(sdata)%2:
        return sdata[len(sdata)//2]
    else:
        return (sdata[len(sdata)//2 - 1] + sdata[len(sdata)//2]) / 2

filename = 'data/Heathrow.txt'

with open(filename, 'r', encoding='utf-8') as f:
    rawdata = f.readlines()
    
    print(rawdata)
    
    numeric_data = [float(i.strip()) for i in rawdata]
    print(numeric_data)
    
    print(f"Minimum = {min(numeric_data)}")
    print(f"Maximum = {max(numeric_data)}")
    print(f"Mean = {mean(numeric_data)}")
    print(f"Median = {median(numeric_data)}")
    
    