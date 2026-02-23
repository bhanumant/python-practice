

# some practice for numpy basic operations


import  numpy as np 

str1 = "Hello"
str2="World"

# Creating a numpy array
arr1=np.array([1, 2, 3,4,5, 6, 8.5])
print("numopy array:", arr1)

# creating a numpy array with a specific data type
arr2 = np.array([1,2,3,4,5], 
dtype=np.float32)
print(arr2)
print(np.float32)