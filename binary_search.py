#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 00:05:06 2021

@author: diegotoledano
"""
l = []
entry  = input('Ingresa los numeros que quieres calcular: ')
    
x = entry.split(',')
    
for i in x:
    l.append(int(i))
        
    
    
target = int(input('Target: '))

l.sort()
print(l)
print(target)



def binary_search(l, target, low=None, high = None):

    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1
    
    
    midpoint = (high + low)//2
    

    if l[midpoint] == target:
        
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low=None, high = midpoint-1)
    else:
        return binary_search(l, target, low = midpoint+1, high=None)
    
    
print(binary_search(l,target,low=None, high = None))

