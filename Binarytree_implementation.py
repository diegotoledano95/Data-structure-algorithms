#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:56:28 2021

@author: diegotoledano
"""

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        
        if self.data:
            
            if data < self.data:
                
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def Printing(self):
        
        if self.left:
            self.left.Printing()
        
        print(self.data)
        
        if self.right:
            self.right.Printing()
        
       
        


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(11)
root.insert(4)


root.Printing()