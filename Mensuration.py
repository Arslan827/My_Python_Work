import math
class algebra:
    def quad(self,a,b,c):
        d=b**2-4*a*c
        if(d>=0):
            print("Roots Are Real And Unequal")
            r1=-b+math.sqrt(d)/2*a
            r2=-b-math.sqrt(d)/2*a
            print("Root 1 is",r1)
            print("Root 2 is",r2)
        elif(d==0):
            print("Roots Are Real And Equal")
            r=-b/2*a
            print("Root is",r)
        else:
            print("Roots Are Imaginary")
class shape:
    def rectangle(self,len,breadth):
        print("1.For Area")
        print("2.For Perimeter")
        choice=int(input("Enter Your Choice "))
        if(choice==1):
            print("Area of Rectangle is ",len*breadth)
        elif(choice==2):
            print("Perimeter of Rectangle is ",2*(len+breadth))
        else:
            print("Wrong Input")  
    def triangle(self,base,height):
        print("1.For Area")
        print("2.For Perimeter")
        choice=int(input("Enter Your Choice "))
        if(choice==1):
            print("Area of Triangle is ",1/2*base*height)
        elif(choice==2):
            side1=int(input("Enter the side 1 "))
            side2=int(input("Enter the side 2 "))
            print("Perimeter of Triangle is ",base+side1+side2)
        else:
            print("Wrong Input")
    def square(self,side):
        print("1.For Area")
        print("2.For Perimeter")
        choice=int(input("Enter Your Choice "))
        if(choice==1):
            print("Area of Square is ",side*side)
        elif(choice==2):
            print("Perimeter of Square is ",4*side)
        else:
            print("Wrong Input")
    def cylinder(self,rad,hei):
        print("1.For Volume")
        print("2.For Lateral Surface Area")
        print("3.For Total Surface Area")
        ch=int(input("Enter Your Choice"))
        if(ch==1):
            v=math.pi*rad**2*hei
            print("Volume of Cylinder is",v)
        elif(ch==2):
            lsa=2*math.pi*r*h
            print("Lateral Surface Area of Cylinder is",lsa)
        elif(ch==3):
            tsa=2*math.pi*r*(h+r)
            print("Total Surface Area of Clinder is",tsa)
        else:
            print("Wrong Input")
    def cuboid(self,length,breadth,height):
        print("1.For Volume")
        print("2.For Curved Surface Area")
        print("3.For Total Surface Area")
        ch=int(input("Enter Your Choice "))
        if(ch==1):
            v=length*breadth*height
            print("Volume of Cuboid is",v)
        elif(ch==2):
            csa=2*(length+breadth)*height
            print("Curved Surface Area  of Cuboid is",csa)
        elif(ch==3):
            tsa=2*((length*breadth)+(height*breadth)+(length*height))
            print("Total Surface Area of Cuboid is",tsa)
        else:
            print("Wrong Input")
    def cone(self,sl,h,r):
        print("1.For Volume")
        print("2.For Curved Surface Area")
        print("3.For Total Surface Area")
        ch=int(input("Enter Your Choice "))
        if(ch==1):
            v=1/3*math.pi*r**2*h
            print("Volume of Cone is",v)
        elif(ch==2):
            csa=math.pi*r*sl
            print("Curved Surface Area of Cone is",csa)
        elif(ch==3):
            tsa=((math.pi*r**2)+(math.pi*r*sl))
            print("Total Surface Area of Cone is",tsa)
        else:
            print("Wrong Input")
object1=shape()
object2=algebra()
print("A.For Algebra")
print("M.For Mensuration")
ch=input("Enter Your Choice ")
match ch:
    case "M":
        while(True):
            print("1.For Rectangle")
            print("2.For Triangle")
            print("3.For Square")
            print("4.For Cylinder")
            print("5.For Cuboid")
            print("6.For Cone")
            print("If You Want to Quit Press 7")
            choice=int(input("Enter your choice "))
            if(choice==1):
             l=int(input("Enter the length of the rectangle "))
             b=int(input("Enter the breadth of the rectangle "))
             object.rectangle(l,b)
            elif(choice==2):
              b=int(input("Enter the base of Triangle "))
              h=int(input("Enter the height of Triangle "))
              object.triangle(b,h)
            elif(choice==3):
              s=int(input("Enter the side of the Square "))
              object.square(s)
            elif(choice==4):
              r=int(input("Enter the radius"))
              h=int(input("Enter the height"))
              object.cylinder(r,h)
            elif(choice==5):
              l=int(input("Enter the length of cuboid "))
              b=int(input("Enter the breadth of cuboid "))
              h=int(input("Enter the height of cuboid "))
              object.cuboid(l,b,h)
            elif(choice==6):
              sl=int(input("Enter the slant height "))
              h=int(input("Enter the height "))
              r=int(input("Enter the radius "))
              object.cone(sl,h,r)
            elif(choice==7):
             print("Thank You Visit Again")
             break
    case "A":
        a=int(input("Enter the cofficient of x**2 "))
        b=int(input("Enter the cofficient of x "))
        c=int(input("Enter the constant "))
        object2.quad(a,b,c)