import math

# math.ceil(x): Returns the smallest integer ≥ x
x = 10.5
print(math.ceil(x))  # Output: 11

y = 144.5
print(math.ceil(y))  # Output: 145




# math.fabs(x): Returns the absolute value of a number (always positive float)
z = -10
print(math.fabs(z))  # Output: 10.0

zz = +10
print(math.fabs(zz))  # Output: 10.0



# math.factorial(n): Returns n! (product of all numbers from 1 to n)
s = 5
print(math.factorial(s))  # Output: 120 (5*4*3*2*1)

ss = 11
print(math.factorial(ss))  # Output: 39916800




# math.floor(x): Returns the largest integer ≤ x
ff = 11.5
print(math.floor(ff))  # Output: 11



# math.fsum(iterable): Returns accurate floating point sum of values
h = [11, 22, 33, 44, 55]
print(math.fsum(h))  # Output: 165.0

hh = (11, 22, 33, 44, 55, 55, 66)
print(math.fsum(hh))  # Output: 286.0



# math.sqrt(x): Returns the square root of x
k = 16
print(math.sqrt(k))  # Output: 4.0

kk = 165
print(math.sqrt(kk))  # Output: approx 12.845



# math.pow(x, y): Returns x to the power of y (x^y)
print(math.pow(2, 7))  # Output: 128.0 (2^7)

print(math.pow(4, 5))  # Output: 1024.0 (4^5)




#  math.log(x): Returns natural logarithm (base e) of x
print(math.log(1))  # Output: 0.0 (because log_e(1) = 0)

print(math.log(2))  # Output: approx 0.6931 (log_e(2))
