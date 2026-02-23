

import statistics as s


data = [1, 2, 3,4]
print(s.mean(data))

print(s.harmonic_mean(data))

data1 = [1, 2, 3,4, 3, 5, 6,7]

print(s.median(data1))
print(s.median_high(data1))
print(s.median_low(data1))

data2=[1, 2, 1, 2, 3, 4, 1, 2, 4, 6, 7, 8,9]
print(s.mode(data2))