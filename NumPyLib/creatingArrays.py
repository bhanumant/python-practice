

import numpy as np



# 1D Array, 2D Array, 3D Array, Multidimenstional Array

a = np.array([1,2,3,4,5]) # 1D
b = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 5, 3, 4, 0]])  #2D
print(a)
print(b)


c = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 5, 3, 4, 0], [2,3,5,4,5,8]])  
print(c)


d=np.array([ [ [1,2], [3,4] ],[ [5,6],[7,8] ]]) #3D array
print(d)


arra1=[1,2,5,6]
e= np.array(arra1, ndmin=3)  #ndim=no of dimensions - specify the dimensions with the param
print(e)



f=np.array([1, 2, 3, 4,5,6], ndmin=2)
print(f)




#Numpy attributes

# np.dtype
# np.shape
# np.size


x = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 5, 3, 4, 0]])  
print("Array dimensions", x.ndim)
print("Array Bytes", x.nbytes)
print("Array Shape", x.shape)
print("Array Size", x.size)
print("Array Datatype", x.dtype)


y = np.array([["Hi", "hello", "Bye", "Js", "Py"]])  
print("Array dimensions", y.ndim)
print("Array Bytes", y.nbytes)
print("Array Shape", y.shape)
print("Array Size", y.size)
print("Array Datatype", y.dtype)





