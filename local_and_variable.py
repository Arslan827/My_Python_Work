# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:34:01 2024

@author: saifi
"""

x=9
print(x)
def fun():
    global x
    x=111
    print(x)
    v=10
    print(v)
fun()
