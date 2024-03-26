# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:57:37 2024

@author: saifi
"""

def greet(fx):
    def mfx(*args,**kwargs):
        print("Welcome")
        fx(*args,**kwargs)
        print("Thank you for using our function")
        return mfx
    
@greet
def add(a, b):
    return a+b
    
k=add(1, 3)
print("Sum of two number is ",k)