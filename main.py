# print("my name is fahad")
# print('my age is ', 22)                    multiple lines comment =  cntrl + forwrd /
# print("my Cgpa is ", 3*1 + 0.15 )

a= 1
print(1+a)


a= 1
b= 1.567
c= "fahad"
d= True
e= complex(2,10)
print("the data type is ", type(a))
print("the data type is ", type(b))
print("the data type is ", type(c))
print("the data type is ", type(d))
print("the data type is ", type(e))



#List
list1 = [9 , 4 ,["apple , banana", "i love you"]]
print(list1[1])


#Tuple

tuple1 = ("loin", ("tiger , banana"),("bear , fox"))
print(tuple1)


#dictionary

dict1 ={"name":"fahad", "age":22 ,"canVote":True}
print(dict1["name"])

#TypeCasting

A= 10
B = "20"
print(int(A)+int(B))



#for loop
fathername = "Hafeez Ullah"

for character in fathername:
    print(character)
    

#len()
    
child="shahmeer son of, fahad"
length= len(child)
print(length)

print(child[0:8])


# .upper & .lower

mothername = "Lutfia"
print("length of mother name is ",len(mothername))
print("length of mother name in lower case ", mothername.lower())
print("length of mother name in upper case ", mothername.upper())


# rstrip()

brother = "!!khizar !!!!!!!!!!! !!!!!"
print(brother)

print(brother.rstrip("!"))

#split()

print(brother.split(" "))

#endswith()
print(brother.endswith("!!!!!"))
str1 = "welcome to fahad are you fine "
print(str1.endswith("to",4 ,10))

#find()
print(str1.find("o"))

#index()
#print(str1.index("lo"))

#isalnum()
str2  = "MuhammadFahad"
print(str2.isalnum())
#isalpha()
str3 = "My Bike was Stolen By Theft"
print(str3.isalpha())

#swapcase
print(str3.swapcase())





# if & else statements 

print("Driving Liscense checking :")
print("=============================")
Q = int(input("Enter Your Age : "))

if(Q>17 ):
    {
    print("you are eligible for driving")
    }

else:
    print("you are not allowed to drive")
