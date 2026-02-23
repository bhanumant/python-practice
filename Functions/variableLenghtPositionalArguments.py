

# Variable length positional arguments

# *args is used for variable length arguments
# Touple is created for variable lengh arguments
# fun (a, b, *args) a and b must be passed as positional only
# fun (*args, a, b) a and b must be passed as Keyword only arguments
# fun(*L1) unpacking actual arguments


# print(10,2.5, "Hello", (1, 2,3,4), {1, 2,3}, [1, 2,3], True)


def fun(*args):
    print(args)
fun(10,20,30)


def fun2(a, b, *args):
    print(a, b, *args)
fun2(10,20,33,44,0.2,True)




def fun3(*args):
    print(*args, len(args))
    l1=[1,2,3]
    fun3 (l1)
    print(fun3(l1))

