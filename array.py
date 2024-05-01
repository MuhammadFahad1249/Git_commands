import array as arr

# we can create array in two different ways one from using array keyword , another by using numpy 

my_arr = arr.array('i',[1,2,3,4,5])
print(my_arr)
print(type(my_arr))



# In numpy array it supports different data types 
import numpy as nm
my_arr1 = nm.array(["hello", 1, 2, 3])
print(my_arr1)


# CODE FOR UNIQUE ITEMS IN AN ARRAY
import numpy as np
my_arr1 = np.array(["hello", 1, 2, 3, 1, 2])
print(my_arr1)
# Using numpy.unique() to discard repeated elements
unique_elements = np.unique(my_arr1)
print(unique_elements)


#CODE FOR SORTED ITEMS IN ARRAY
import numpy as np
my_arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted_arr = np.sort(my_arr)
print("Sorted array:", sorted_arr)


#CODE FOR THE REVERSE ITEMS IN AN ARRAY 

import numpy as np
my_arr = np.array([1, 2, 3, 4, 5])
reversed_arr = my_arr[::-1]
print("Reversed array:", reversed_arr)

# CODE to FIND THE LARGEST NUMBER IN AN ARRAY

import numpy as np
my_arr = np.array([5, 2, 8, 1, 6, 9])
index_of_largest = np.argmax(my_arr)
print("Index of the largest number:", index_of_largest)
print("Largest number:", my_arr[index_of_largest])

#code for min number in an array
import numpy as np
my_arr = np.array([5, 2, 8, 1, 6, 9])
index_of_minimum = np.argmin(my_arr)
print("Index of the minimum number:", index_of_minimum)
print("minimum number:", my_arr[index_of_minimum])


#CODE FOR THE NUMBERS WHICH ARE GREATER THAN 2 
import numpy as np
my_arr = np.array([1, 2, 3, 4, 5])
# Filter elements greater than 2
filtered_arr = my_arr[my_arr > 2]
print("Filtered array with numbers greater than 2:", filtered_arr)
