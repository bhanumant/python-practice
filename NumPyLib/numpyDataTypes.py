

import numpy as np

aa= np.array([1,2,3, 4])
print(aa)
print("my array datatype", aa.dtype)  #Int



aa1= np.array([1.1,2.2,3.3, 4.4])
print(aa1)
print("my array datatype", aa1.dtype) # Float --64 bit -8byte each



aa2= np.array([1, 2, 3,4], "b")
print("My array is", aa2.dtype)



arr = np.array(["apple", "banana"], dtype=np.str_)
print(arr)
print("Data type:", arr.dtype)


arr = np.array([True, False, True], dtype=np.bool_)
print(arr)
print("Data type:", arr.dtype)
