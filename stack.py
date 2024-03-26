s=[]
c="y"
while(c=='y'):
    print("1.PUSH OPERATION")
    print("2.POP OPERATION")
    print("3.DISPLAY OPERATION")
    choice=int(input("Enter your choice"))
    if(choice==1):
        a=int(input("Enter the number"))
        s.append(a)
    elif(choice==2):
        if(s==[]):
            print("Stack is Empty")
        else:
            print("Deleted element is",s.pop())
    elif(choice==3):
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])
    else:
        print("Wrong Input")
    c=input("Do you want to continue or not?")