#Good Morning greeting game
import time
timespamp = (time.strftime("%H,%M,%S"))
print(int(timespamp))
timespamp1 = int(time.strftime("%H"))
print(timespamp1)
timespamp2 = int(time.strftime("%M"))
print(timespamp2)
timespamp3 = int(time.strftime("%S"))
print(timespamp3)


if(timespamp>0):
    {
        print("valid Date & Time")
    } 
elif(timespamp1==12):
    
        if(timespamp2==0):
            {
                print("time is 12 hour and zero minute ")
            }
        else:
            print("time is wrong")
            
