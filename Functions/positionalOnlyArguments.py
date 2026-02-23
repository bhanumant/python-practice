

# Positional-only arguments are a feature introduced in Python 3.8 that allows you to define function parameters that can only be passed positionally, not as keyword arguments.

# def fun(a, b/ c, d):  # is used to define positional-only arguments
# def fun(a, b c, d/ ):  # is used to define all positional-only arguments
# def fun(/,a, b c, d ):  # invalid syntax, '/' must be at the end of positional-only arguments



def positional_only_args(a, b, /, c=3, d=4):
    """
    Positional-only arguments are specified by placing a '/' in the parameter list.
    This means 'a' and 'b' must be passed positionally, while 'c' and 'd' can be passed either positionally or as keyword arguments.
    """
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

    positional_only_args(1, 2, 5, 6)  # a=1, b=2, c=5, d=6





