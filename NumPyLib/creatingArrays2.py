



#Creating An array

import numpy as np

# np.zeros()
# np.ones()
# np.empty()
# np.eye()
# np.diag()
# np.arange(start, end , step)
# np.linspace()


array = np.zeros(3)
print("My array ", array)
print("My array Datatype ", array.dtype)



array1 = np.zeros((3, 4))
print("My array with 3 Row 4 Coloumn ", array1)
print("My array with 3 Row 4 Coloumn ", array1.dtype)
print("My array with 3 Row 4 Coloumn ", array1.dtype)

array2 = np.zeros((3, 4, 6))
print("My array with 3D array with 4 Row 6 Coloumn ", array2)
print("My array with 3D array with 4 Row 6 Coloumn ", array2.dtype)
print("My array with 3D array with 4 Row 6 Coloumn ", array2.dtype)


ar = np.ones(3)
print("My array ", ar)
print("My array Datatype ", ar.dtype)

ar1 = np.ones((3,4))
print("My array ", ar1)
print("My array Datatype ", ar1.dtype)

ar2= np.empty((3,5))
print("My empty array", ar2)


ar3 = np.eye(5)
print('My identical matrix is', ar3)



ee= np.diag((2, 3)) # All the passed element filled as diagonal
print(ee)

ff= np.diag((1, 2,3, 4, 5)) # For Touple
print(ff)


gg= np.diag([1, 2,3, 4, 5]) # For List
print(gg)


kk= np.arange(1, 8, 2)  # Start element , End  element, step
print("My array after use of range function", kk)


jj= np.linspace(1, 12, 20)
print(jj)