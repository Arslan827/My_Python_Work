n=int(input("Enter the number "))
for i in range(2,n):
    if(n%i==0):
        if(n%2==0):
            print(n,"is a composite number and also an even number.")
        else:
            print(n,"is a composite number and also an odd number.")
        break
    
else:
        print(n,"is a prime number and also a odd number.")