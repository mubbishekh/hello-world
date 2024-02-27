# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:25:33 2022

@author: Mubashshirahbanu
"""

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
#print(curried_pow(2)(3))
def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

print(map_to_range(0, 5, curried_pow(2)))