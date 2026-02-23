

# Default argument functions

# Fill from right to left

# def default_args(a=2, b,  c=3): # not allowed
#     return a + b + c


def default_args(a, b=2, c=3):
    return a + b + c
print(default_args(1))  # a=1, b=2, c=3 
print(default_args(1, 4, 6))  # a=1, b=4, c=3



# Default argumet is any type of argument that is assigned a default value in the function definition. like string, integer, list, tuple, etc.
# passing the arguments in the function with any type of data type like string, integer, list, tuple, etc.


def fun(a=1, b=2, c="Hello"):
    print(a, b, c)
fun()

def fun2(a=1, b=2, c=(1, 2, 3)):
    print(a, b, c)
fun2()


def fun3(a=1, b=2, c=[1, 2, 3]):
    print(a, b, c)
fun3()


def fun4(a=1, b=2, c={1, 2, 3}):
    print(a, b, c)
fun4()


