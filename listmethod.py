# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:40:35 2024

@author: saifi
"""

l=[2,2,4,5,8,9,7]
#Check Weather given element present in the list or not
if 10 in l:
    print("Yes 10 prersent in the list")
else:
    print("No 10 not present in the list")

#Append the item to the end of the list
l.append(10)
print(l)

#Sort the list in ascending order
lst=[32,2,8,9,87,67,7,877,8,1,8,8,8,8]
lst.sort()
print(lst)

#Reverse the original list
lst.reverse()
print(lst)

#Returns the count of the number of items with the given value
k=lst.count(8)
print(k)

#Returns the copy of the list without modifying the original list
m=lst.copy()
print("Copying list is ",m)

#Insert an item at the given index
lst.insert(1,25)
print("New list is ",lst)

#Adds an entire list to the existng list 
lst.extend(l)
print(lst)

#Join two list 
list=lst+l
print("Join list is ",list)