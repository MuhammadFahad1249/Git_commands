# a = 12
# b = 12.343435
# c= "practice"
# d= True
# e= None

# print("the datatype is : ", type(a))
# print("the datatype is : ", type(b))
# print("the datatype is : ", type(c))
# print("the datatype is : ", type(d))
# print("the datatype is : ", type(e))


# list2 = [9 , 3 , "fahad" ,["aman ","hammad"],94,81]
# print(list2[3])

# tuple2 = (90,"aman" , "fahad" ,("hello" , 10))
# print(tuple2[3])

# dict2 = {"name":"fahad" , "age":22 , "rollnum":"CT-94"}
# print(dict2["rollnum"])


# nm = "harry"
# print(nm[::-1])


import numpy as np 
my_array = np.array(["fahad", 9 , 4, 8 ,1 ,4 ,2])
print(my_array)
sorted_array= np.sort(my_array)
print(sorted_array)

import numpy as np 
my_array = np.array(["fahad", 9 , 4, 8 ,1 ,4 ,2])
print(my_array)
reverse_array = my_array[::-1]
print(reverse_array)

import numpy as np 
my_array = np.array([  4, 8 ,1 ,4 ,2])
print(my_array)
max_num_index = np.max(my_array)
#max_num= my_array[max_num_index]
print(max_num_index)
#print(max_num)

import numpy as np 
my_array = np.array([  4, 8 ,1 ,4 ,2])
print(my_array)
non_repeated = np.unique(my_array)
print(non_repeated)

# if number is divided by 2 
import numpy as np 
my_array = np.array([1,2,5, 6, 3,10 , 45])
filtered_array = my_array[my_array %2 != 0]
print(filtered_array)


my_list = ["aman " , 1 , 8, 3]
print(my_list[0][0])


print("nested")
nested_list = ["hammad" , [1,"aman",0], 5]
print(nested_list[1][1][1])



my_tupple = ("hello" , 1 , 2 ,3 )
print(my_tupple[1])

my_dic = {
    "name": "fahad",
    "age": 20,
    "gender":"male"

}

print(my_dic["gender"])

m= 5
my_list= []
for i in range (10):
    my_list.append(i)

updated_list = my_list
print(updated_list)   
               