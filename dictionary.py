import json
'''n=int(input("How many Employee ?"))
emp={}
for a in range(n):
    name=input("Enter name of the employee: ")
    salary=int(input("Enter the salary: "))
    age=int(input("Enter the age: "))
    add=input("Enter the address: ")
    emp[name]=salary,age,add
print(json.dumps(emp,indent=2))'''
'''for b in emp:
    print(b,":"," Salary "," Age "," Address ",emp[b])
'''

'''birthday={"Newton":1642,
          "Darwin":1809,
          "Turing":1912}
print("keys:",birthday.keys())
print("values:",birthday.values())
print("items:",birthday.items())
print("get:",birthday.get("Curle",1867))
temp={"Curie":1867,
      "Hopper":1906,
      "Franklin":1920}
birthday.update(temp)
print('After Update:',birthday)
birthday.clear()
print("After Clear:",birthday)'''

'''n=int(input("Enter the user number? "))'''
'''user={}'''
'''Creating the dicitionary'''
'''for a in range(n):
    name=input("Enter User_Name ")
    code=int(input("Enter Your Password "))
    user[name]=code'''
    
'''Checking the Username and Password'''
'''print("You Have Only 3 Chance For Login")
i=0
while(i<3):
    name=input("Enter Your Username ")
    code=int(input("Enter Your Password "))
    if name in user and user[name]==code:
      print("Successfully Login")
    else:
      print("Invalid Users")
    i=i+1
else:
    print(" !Your Accpunt Are Blocked! ")
    print(" Please Contact Your Office ")'''
    
'''n= int(input("How many team has been added "))
team={}
for i in range(n):
    key=input("Enter Team Name ")
    win=float(input("How many matches are win please mention W "))
    loss=float(input("How many matches are loss please mention L "))
    team[key]=win,loss
    
print(team)

t=input("Enter Team Name For Finding The Winning Percentage ")
if t in team:
    p=team.get(t)
    print(p)
    per=win/p
    print("Winning Percentage is ",per)
else:
    print("Team Are Not Found")'''
    
#Program for store the product name and its price in the dicitionary

'''store={}
n=int(input("How many product you may want add in the store? "))
i=0
while(i<n):
    p_name=input("Enter the product name ")
    p_price=int(input("Enter the product price "))
    store[p_name]=p_price
    i=i+1
print("Products Available In The Store Are: ")
print(store)
check=input("Enter product name ")
if check in store:
    ch=store.get(check)
    print("Product Name is ",check)
    print("Product Price is Rs ",ch)
    print("Thank You For Select Our Product")
else:
    print("Sorry Product Are Not Available in the Store")
    print("Thank You Visit Again")
   ''' 
#Program to store the records of the student in dicitionary
student={}
i=0
while(i<5):
    s_roll=int(input("Student Roll Number "))
    s_name=input("Student Name ")
    s_class=int(input("Student Class "))
    s_total_marks=int(input("Student Total Marks "))
    s_grade=input("Student Grade ")
    student[s_roll]=s_name,s_class,s_total_marks,s_grade
    i=i+1
print("Student Records Are:")
print(json.dumps(student,indent=2))