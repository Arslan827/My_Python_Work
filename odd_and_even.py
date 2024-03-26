# -*- coding: utf-8 -*-
import math
"""
Created on Mon Jan 15 13:32:48 2024

@author: saifi
"""

'''n=int(input("Enter The Number"))
if(n==0):
    print("Please enter positive number")
elif(n%2==0):
    print("Number is even",n)
else:
    print("Number is odd",n)'''
    
'''x=int(input("Enter the age"))
if(x>=18):
    print("Eligible for vote")
else:
    print("Not eligible for vote")'''
    
a=int(input("Enter the coffecient of x**2"))
b=int(input("Enter the coeffecient of x"))
c=int(input("Enter the constant term"))
d=b**b-(4*a*c)
if(d>0):
    print("Root is real unequal")
    root1=-b+math.sqrt(d)/2*a
    root2=-b-math.sqrt(d)/2*a
    print("Root 1 is ",root1)
    print("Root 2 is",root2)
elif(d==0):
    print("Root is Real and equal")
    root1=-b+math.sqrt(d)/2*a
    root2=-b-math.sqrt(d)/2*a
    print("Root 1 is",root1)
    print("Root 2 is",root2)
else:
    print("Root is imaginary number")
