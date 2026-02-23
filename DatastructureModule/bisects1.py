

#Bisects

import bisect

b=[10,20,20,30,40,50]


bb=bisect.insort(b, 25)
print(b)

cc= bisect.insort_left(b, 90)
print(b)


bisect.bisect(b, 5)
print(b)


bisect.bisect_right(b, 200)
print(b)
