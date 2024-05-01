# number checker
num = int(input("Enter the number : "))
if(num<0):
    {
        print("Number is Negative")
    }
elif(num==0):
    {
        print("Number is Zero ")
    }
elif(num>0):
    {
        print("Number is Positive & greater than Zero")
    }

else:
    print("invalid Number !!!")





#Age calculator using nested if condition  
    
age = int(input("Enter your Age : "))
if (age<0):
    {
        print("Hurry your are not born yet")
    }

elif(age>0):
        if(age<=10):
            
            print("You are a child")
        
        
        elif(age>=11 and age<20):
            
            print("You are Young")

        elif(age>=20 and age<30):
            
            print("You are Adult")

        elif(age>30 and age<50):

            print("You are an over 30 person")
        else:
            
                print("Enter the number greater then zero")
               
else:
    print("Please enter the valid age !")



