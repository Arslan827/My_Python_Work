# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:21:57 2024

@author: saifi
"""
import random



def game(computer,user):
    if computer==user:
        return 0
    elif computer==0 and user==2:
        return -1
    elif computer==1 and user==0:
        return -1
    elif computer==2 and user==1:
        return -1
    else:
        return 1
    
print("0.For Rock")
print("1.For Paper")
print("2.For Scissor")
user=int(input("Enter your choice "))
computer=random.randint(0,2)
    
score=game(computer,user)

if(score==0):
    print("Match are draw")
elif(score==-1):
    print("Computer Win")
else:
    print("You Win")
    
print("Computer Select Number is ",computer)
print("Your Number is ",user)