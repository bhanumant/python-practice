

# Array allows only similar type of elements , homogenious

import array

a1=array.array("i", [10,20,30,40,50])
print(a1)

s1=b"abcdef"
print(array.array('b', s1))
print(a1[2])
print(s1[4])


s3=a1.append(103)
print(s3)

print(s1.index(97))