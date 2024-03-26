import math
print("Press 1 For Finding The Hypotenus")
print("Press 2 For Finding The Base")
print("Press 3 For Finding The Perpendicular")
ch=int(input("Enter Your Choice "))
if(ch==1):
    p=int(input("Enter the perpendicular "))
    b=int(input("Enter the base "))
    h=math.sqrt(p**2+b**2)
    print("Hypotenus is ",h)
elif(ch==2):
    h=int(input("Enter the hypotenus "))
    p=int(input("Enter the perpendicular "))
    b=math.sqrt(h**2-p**2)
    print("Base is ",b)
elif(ch==3):
     h=int(input("Enter the hypotenus "))
     b=int(input("Enter the base "))
     p=math.sqrt(h**2-b**2)
     print("Perpendicular is ",p)
else:
    print("Wrong Input")