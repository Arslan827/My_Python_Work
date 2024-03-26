# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:56:28 2024
t.
@author: saifi
"""

t=(1,2,3,4,5,6,7,8,9,10,11,122)
#Silicing the tuple which is give the new tuple
tup=t[1:5]
print("New tuple after the silicing", tup )

#Check weather the given item present in tuple or not
if 9 in t:
    print("Yes 9 is present in the given tuple")
else:
    print("9 is not present in the given tuple")
    
#Now we convert the tuple into list for performing the list operation on the tuple

temp=list(t)
temp.append(123)
temp.pop(4)
temp[1]=88
k=tuple(temp)
print("New tuple is", k)

#Count the given element from the tuple
k=t.count(8)
print("Number of the 8 is", k)

#Return the length of the given tuple
k=len(t)
print("Length of the tuple is", k)