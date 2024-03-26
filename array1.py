def check(l1):
    print("List is",l1)
    pos=0
    ne=0
    neg=0
    L=len(l1)
    print("length of list",L)
    for num in l1:
        if num>0:
            pos +=1
            ratio1=pos/L
        elif num==0:
            ne +=1
            ratio2=ne/L
        else:
            neg +=1
            ratio3=neg/L
    print("Positive Number in the list is",pos)
    print("Negative Number in the list is",neg)
    print("Zero in the list is",ne)
    print("Ratio of positive number",ratio1)
    print("Ratio of negative number",ratio3)
    print("Ratio of zero",ratio2)
    
    
lst=[]
n=int(input("Enter the number of elements for the list"))
for i in range(0,n):
    print("Enter elements of the list")
    ele=int(input())
    lst.append(ele)
    
    
check(lst)