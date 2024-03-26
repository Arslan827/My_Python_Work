import math
print("Press 1 For Finding Area of Circle")
print("Press 2 For Finding Circumference of Circle")
print('Press 3 For Quit The Program')
while(True):
    ch=int(input("Enter Your Choice "))
    if(ch==1):
        r=float(input("Enter the radius of the circle in meter "))
        ar=math.pi*r*r
        print("Area of Circle is ",ar,"m")
    elif(ch==2):
        r=float(input("Enter the radius of the circle meter "))
        cir=2*math.pi*r
        print("Circumference of Circle is ",cir,"m")
    elif(ch==3):
        print("Thank You Visit Again")
        break