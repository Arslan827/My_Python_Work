def lcm(n1,n2):
    if(n1>n2):
        greater=n1
    else:
        greater=n2
    while(True):
        if((greater % n1 == 0) and (greater % n2 == 0)):
           lcm = greater
           break
        greater += 1

    return lcm

n1=int(input("Enter the number n1 "))
n2=int(input("Enter the number n2 "))
print("Lcm is ",lcm(n1,n2))