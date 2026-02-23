
import numpy as np

aaa = np.array([1, 2, 3, 4, 5,6,6,6,6,7,7,7])
print(aaa)
print("Shape of my array", aaa.shape)
print("reshape my array", aaa.reshape(3,4))
print("reshape my array", aaa.reshape(4,3))
print("reshape my array 3 planes , 2 row , 3 coloumns", aaa.reshape([3, 2, 2]))


a1= aaa.reshape([3,2, 2 ])
print("My array", a1)
print(a1.flatten()) # Convert into single dimentional array