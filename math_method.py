# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:35:59 2024

@author: saifi
"""

import math
ab=int(input("Enter the perpendicular"))
bc=int(input("Enter the base"))
ac=math.sqrt(ab**2+bc**2)
print("Hypotenus is ",ac)
theta=round(math.sin(ab/bc)*180/math.pi)
print("Angle is ",theta)