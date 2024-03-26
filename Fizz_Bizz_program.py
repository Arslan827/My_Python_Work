# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:43:09 2024

@author: saifi
"""
l=[]
n=int(input("Enter the number of element in list "))
for i in range(0,n):
    ele=int(input("Enter the element you want to add "))
    l.append(ele)
print(l)
        
def check(k):
    for i in l:
        if(i%3==0 and i%5!=0):
            print("Fizz ",i)
        elif(i%5==0 and i%3!=0):
            print("Bizz ",i)
        elif(i%3==0 and i%5==0):
            print("Fizz Bizz ",i)
        else:
            print(i)
            
            
            
k=check(l)