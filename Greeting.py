#Program for the capable of greeting you with Good Morning,Good Afternoon and Good Night
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
minute=int(time.strftime('%M'))
second=int(time.strftime('%S'))
print("Hour is", hour)
print("Minute is", minute)
print("Second is", second)

if(hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
elif(hour>=17 and hour<0):
    print("Good Night Sir")
