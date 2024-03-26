'''Question 1'''

'''x=int(input("Enter a value for x: "))
y=int(input("Enter a value for y: "))
z=int(input("Enter a value for z: "))
if(x<y<z):
    print("branch 1",end = " ")
elif(x>y>z):
    print("branch 2",end = " ")
else:
    print("branch 3",end = " ")
print("is the branch")'''

'''Question 2'''

'''k=int(input("Enter a value for k "))
if(k>50):
    if(k<60):
        print("One")
    else:
        print("Two")
else:
    if(k>30):
        print("Three")
    else:
        print("Four")'''
        
'''Question 3'''

'''x=int(input("Enter a value for x: "))
y=int(input("Enter a value for y: "))
if(x>2):
    if(y>2):
        z=x+y
        print("z is", z)
else:
    print("x is", x)'''
    
'''Question 4'''

'''x=int(input("Enter a value for x: "))
y=int(input("Enter a value for y: "))
z=x+3
if z==1:
    y=0
    print(y)
elif z==2:
    y=10
    print(y)
elif z==4:
    y+=1
else:
    y=1
    print(y)
'''
'''for a in 10,12,14,16,18:
    print(a)
for j in range (0,5):
    print(j)
for a in "Apple":
    print(a)
'''
    
'''key="panda"
correct=False
while not correct:
    inp=input("Enter secret Key: ")
    if inp == correct:
        print("Correct")
    else:
        print("Wrong Guess")'''
        
l=[1,2,3,4,5,6,7,8,9,10,12,123,25,54,89,33,69,58,528,6358,556,88,588,566,95,236,55555,5257,845]
k1=max(l)
print(k1)
k2=min(l)
print(k2)
range=k1-k2
print("Range of given list is", range)

