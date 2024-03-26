# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:59:52 2024

@author: saifi
"""

cube=lambda x:x*x*x


'''We can pass a function as a argument by using the lambda function'''
def appl(fx,value):
    return 6+fx(value)

if __name__=="__main__":
    print(cube(8))
    print(appl(cube,5))


'''l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newl=[]
for item in l:
    newl.append(cube(item))
    
print(newl)'''