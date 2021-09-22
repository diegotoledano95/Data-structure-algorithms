#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:57:18 2021

@author: diegotoledano
"""
def countingSort():
    arr = [89,37,29,73,68,82,58,45,84,17,88,46,69,60,20,24,34,49,52,80,43,72,92,55,10,49,14,88,77,47,64,43,23,66,64,86,27,63,38,62,75,25,58,13,79,30,26,12,94,96,29,92,59,15,98,39,32,81,78,13,15,86,72,45,82,46,42,66,97,85,42,46,56,57,40,54,63,27,32,68,2,64,29,22,38,18,36,60,82,20,75,18,79,70,17,56,6,15,11,15,40,17,5,96,84,7,78,28,74,51,67,3,48,53,30,46,9,89,40,65,16,61,98,33,3,19,57,84,32,27,42,83,60,80,27,17,98,61,7,14,76,74,65,37,2,97,52,12,77,40,41,99,90,29,55,76,71,62,63,46,27,46,51,3,11,89,75,52,78,23,96,17,65,85,63,19,16,50,42,4,92,67,51,96,53,7,37,97,45,5,70,73,80,73,39,19,15,43,39,34,4,31,72,26,96,98,17,84,8,76,21,5,86,23,30,95,88,92,44,33,7,10,32,1,69,88,10,19,29,8,82,86,25,91,60,47,18,7,36,53,88,40,25,29,69,99,82,93,47,92,25,33,26,8,88,83,16,87,31,95,9,0,28,52,20,39,20,81,71,39,10,85,63,22,8,98,67,26,99,96,71,19,64,75,54,35,58,26,40,89,46,67,23,53,61,17,69,41,62,64,19,74,48,61,81,38,49,38,69,74,61,20,2,84,48,35,63,91,82,75,98,87,16,35,26,53,9,0,84,75,41,28,25,48,11,0,99,11,10,71,79,58,96,88,94,0,74,75,84,52,92,53,93,13,21,91,64,46,16,6,82,57,19,53,95,29,1,46,52,58,99,78,37,23,60,24,47,10,97,34,38,6,35,49,53,98,84,62,51,66,78,30,58,48,60,34,51,30,95,16,36,55,53,99,54,3,53,57,43,55,98,92,53,98,73,70,86,7,50,58,75,32,67,36,84,56,37,81,6,73,90,5,8,69,92,18,3,76,59,42,88,87,64,48,45,95,33,40,5,51,58,5,30,20,87,33,37,61,14,36,95,32,44,33,74,93,23,23,28,4,90,75,58,93,20,60,57,64,79,56,69,35,45,37,14,6,47,16,36,90,18,29,4,82,19,77,8,22,54,2,65,37,86,5,67,58,33,86,43,15,4,97,62,39,7,12,60,75,17,66,97,76,57,86,75,7,78,49,74,81,50,26,69,82,75,40,17,34,24,15,37,8,18,35,24,19,86,47,0,14,30,22,20,3,97,56,93,55,28,11,98,78,19,5,70,71,42,62,91,0,84,36,24,21,26,59,20,46,65,26,82,50,34,40,98,30,63,60,2,91,83,94,18,69,12,37,22,97,53,78,17,85,66,27,55,0,96,89,73,85,42,21,81,5,38,37,62,14,77,60,57,17,45,43,25,53,82,72,30,2,85,25,8,29,18,21,96,51,4,55,23,79,9,40,35,10,96,24,96,18,11,81,55,27,72,8,28,67,40,32,77,76,26,17,63,47,99,22,37,64,42,32,3,41,15,83,86,58,5,74,93,47,44,18,1,32,27,41,10,74,67,42,81,70,17,57,26,92,33,29,23,42,90,9,40,11,20,85,79,67,26,62,19,81,45,17,92,20,34,52,79,39,90,58,92,56,12,66,69,20,53,0,14,5,1,44,34,49,47,68,53,62,13,21,37,36,66,25,55,87,88,4,31,2,54,64,71,62,97,95,45,46,23,94,37,45,45,49,50,54,24,10,29,44,91,93,12,71,9,73,45,46,63,94,10,50,94,64,22,96,54,53,89,67,98,2,42,15,31,82,82,18,72,41,20,8,21,57,54,78,37,47,37,75,26,32,17,64,79,46,88,46,57,63,62,63,30,86,99,57,32,58,48,67,27,7,0,6,9,50,82,55,72,5,48,20,45,62,67,32,45,94,18,81,92,33,78,9,97,76,25,29,74,86,0,59,60,45,25,6,25,14,4,20,10,45,34,4,64,6,21,42,87,0,81,16,77,16,79,46,24,33,83,62,95,52,52,51,92,47,57,97,47,53,12,62,24,41,74,35,3,95,70,13,13,99,50,19,2,63,4,70,42,78,95,8,69,56,98,54,42,73,22,45,73,22,7,32,58,6,90,13,50,74,26,37,44,9,60,54,45,87,30,8,24,81,23,91,90,97,29,49,31,47,93,88,6,29,48,11,43,28,28,2,9,73,37,48,72,56,62,13,48,19,83,21,29,19,24,76,60,35,89,76,18,65,2,32,45,91]
    
    print(arr)
    n = len(arr)
    
    print(len(arr))
    
    arr2 = [0 for i in range(0,100)]
    
  
    
    arr3 = [0 for i in range(n)]
    
   

     
    for i in arr:
        arr2[i] = arr2[i] + 1

  
    print(arr2)

    for i in range(1,len(arr2)):
        arr2[i] += arr2[i-1]
        
    print(arr2)
    
    
        
    i = n - 1
    
    while i >= 0:
        arr3[arr2[arr[i]]-1] = arr[i]
        arr2[arr[i]] -= 1
        i -= 1
        
    return arr3
print(countingSort())
