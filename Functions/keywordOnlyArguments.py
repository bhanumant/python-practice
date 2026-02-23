

# keyword only arguments 

# First two argument can be any one but the last two arguments must be passed as keyword arguments.
# Keyword-only arguments are specified by placing a '*' in the parameter list.


def fun(a, b, *, c=3, d=4):
    print(a, b, c, d)
    """
    Keyword-only arguments are specified by placing a '*' in the parameter list.
    This means 'c' and 'd' must be passed as keyword arguments, while 'a' and 'b' can be passed positionally or as keyword arguments.
    """


fun(1, 2, c=5, d=6)  # a=1, b=2, c=5, d=6
fun(1, b=2, c=5, d=6)  # a=1, b=2, c=5, d=6
# fun(1, 2, 3, 4)  # not allowed, c and d must be passed as keyword arguments
fun(1, 2, c=5, d=6)  # a=1, b=2, c=5, d=6


def fun2(*, a  , b, c, d):
    print(a, b, c, d)
    """
    Keyword-only arguments are specified by placing a '*' in the parameter list.
    This means 'a', 'b', 'c', and 'd' must be passed as keyword arguments.
    """

    fun2(a=1,b=2,c=3,d=5)  # a=1, b=2, c=5, d=6

    