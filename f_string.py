# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:53:05 2024

@author: saifi
"""

#Print today date
import datetime
today=datetime.datetime.today()
print(f"{today:%B %d,%Y}")

#print the name with the help of f_string
name="Shakeeb Arslan Saifi"
age=23
print(f"Hello, My name is {name} and I'am {age} years old")