# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:48:54 2022

@author: wooih
"""
while True:
    try:
        investment = float(input("Enter the initial investment: "))
        rate = float(input("Enter the annual rate: "))
        years = int(input("Enter the years of years of investment: "))
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Initial investment: ${investment}, annual rate: {rate}%, years of investment: {years}")
        for y in range(years):
            investment = investment + investment*rate/100
            print(f"Year {y+1:>2}: ${investment:>10.2f}")
        break