# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:25:58 2024

@author: saifi
"""


# Python program to illustrate rstrip()
# trailing whitespaces removed
txt = '   Good Morning   '
print('Original string:', txt)
print('New string:', txt.rstrip())
print('')

# 'm' trailing character not removed
txt = 'Python Programming'
print('Original string:', txt)
print('New string:', txt.rstrip('m'))
print('')

# 'ing' trailing character removed
txt = 'Python Programming'
print('Original string:', txt)
print('New string:', txt.rstrip('ing'))

a="Arslan!!!!!!!!!!!"
print(a.rstrip("n"))