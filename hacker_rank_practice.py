# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:43:33 2023

@author: saifi
"""

n=int(input("Enter the number"))
rem=n%2
if(rem==0):
    if(2<=n<5):
        print("Not weird")
    elif(6<=n<20):
        print("Weird")
    elif(n>20):
        print("Weird")
        
else:
    print("Weird Odd")