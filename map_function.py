# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:12:18 2024

@author: saifi
"""
from lambda_function import cube
'''We can simply find the cube of item which is present in the given list by using the map function'''
   
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
newl=list(map(cube,l))
print(newl)