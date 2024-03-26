# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:02:43 2024

@author: saifi
"""

'''a=int(input("Enter the number "))
print(f"Multiplication of {a} is:")
try:
    for i in range (1,11):
        print(f"{(a)}*{i}={int(a)*(i)}")
except :
    print("Invalid Input")
    
print("End of Program")'''

def factorial (n):
    if(n<0):
        raise ValueError("Value must be positive")
    elif(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
   
x=int(input("Enter the number for calculating the factorial "))
k=factorial(x)
print("Factorial of the given number is ",k)