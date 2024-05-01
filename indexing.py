
# Positive Indexing
fruits = ["Apple" , "Banana" ,"Mango" , "Lichi", "WaterMelon"]
for i in range(len(fruits)):
    print(i,fruits[i])


# Negative Indexing

cars = ["toyota corolla" , "fortuner" , "BMW" , "Mehran", "suzuki Alto"]

print(cars[len(cars)-1])
#  OR
print(cars[-1])


# Nested list 
# this shows 
my_list = ["fahad", [1,2,3,4],"khan"]
print(my_list)
# to find the nested loop character 
my_str= my_list[1]
print(type(my_str[1]))
# OR
print(my_list[1][2])
del my_list[0]
print(my_list)
