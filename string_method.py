# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 15:31:44 2024

@author: saifi
"""

'txt = "Hi Sam!"'
'x = "mSa"'
'y = "eJo"'
'mytable = str.maketrans(x, y)'
'print(txt.translate(mytable))'

''' Reverse the String
'''
'm="Hello World"[::-1]'
'print(m)'

''' Program that reads a line and prints its statistics like:
    Number of uppercase letters
    Number of lowercase letters
    Number of alphabets
    Number of digits
    '''
'''line=input("Enter a line  ")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
        if a.islower():
            lowercount+=1
        elif a.isupper():
            uppercount+=1
        elif a.isdigit():
            digitcount+=1
        if a.isalpha():
            alphacount+=1
print("Number of Uppercase Letter",uppercount)
print("Number of Lowercase Letter",lowercount)
print("Number of Digit",digitcount)
print("Number of alphabets",alphacount)'''

'''Program for cheking string are pallindrome or not'''
'''line1=input("Enter the string")
length=len(line1)
rev=-1
for a in range(length):
    if(line1[a]==line1[rev]):
        a+=1 
        rev-=1 
    else:
        print("String are not pallindrome")
        break
else:
    print("Sring are pallindrome")'''
    
''' Write a program that reads a email in the form string and ensure that it belongs to 
domain @edupillar.com '''

email=input("Enter the email = ")
domain='@edupillar.com'
domain_length=len(domain)
email_length=len(email)
sub=email[email_length-domain_length:]
if sub==domain:
    if domain_length != email_length:
        print("Valid Email")
    else:
        print("Invalid Email")
else:
    print("Email belongs to other domain")