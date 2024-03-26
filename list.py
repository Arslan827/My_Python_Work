import statistics
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:23:31 2024

@author: saifi
"""
lst=[]
n=int(input("Enter the number of element for the list = "))
for i in range(0,n):
    ele=int(input("Enter the element of the list"))
    lst.append(ele)
print("Given list is ",lst)

def mode_calculate(lst):
    m=statistics.mode(lst)
    print("Mode of the given list is",m)    
mode_calculate(lst)

def mean_calculate(lst):
    m=statistics.mean(lst)
    print("Mean of the given list is",m)
mean_calculate(lst)

def median_calculator(lst):
    m=statistics.median(lst)
    print("Median of the given list is",m)
median_calculator(lst)