# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:23:04 2023

@author: saifi
"""
year=int(input("Enter the Year"))
if(year%400==0)and(year%100==0):
    print("Given Year is Leap Year")
    
elif(year%4==0)and(year%100!=0):
    print("Given Year is Leap Year")
else:
    print("Given Year is not leap year")
    