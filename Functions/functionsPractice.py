

# Functions

# Performs a specific task
# Can take inputs
# Can return outputs
# Reusable writte once used many times
# Built -in and user defined


# Header, Retuns, Parameters, Calling


def volume(lengh, breadth, height):
    volume = lengh * breadth * height
    return volume
print("Volume of the box is:", volume(10, 20, 30))  # Calling the function with arguments
volume(10, 20, 30)  # Calling the function with arguments


def area(length, breadth):
    area = length * breadth
    return area

print("Area of the rectangle is:", area(10, 20))  # Calling the function with arguments
area(10, 20)  # Calling the function with arguments



# Functions Positional and Keyword Arguments


# Positional arguments are the arguments that are passed to a function in the order in which they are defined.
def volume(lengh, breadth, height):
    print( lengh, breadth, height)
    volume = lengh * breadth * height
    return volume
print("Volume of the box is:", volume(10, 20, 30))  # Calling the function with arguments
volume(10, 20, 30)  # Positional arguments




# Keyword arguments are the arguments that are passed to a function by specifying the name of the parameter.
def volume (lenght=1000, breadth=200, height=300):
    print(lenght, breadth, height)
    volume = lenght * breadth * height
    return volume

print("Volume of the box is:", volume())  # Calling the function with keyword arguments


# Positions and keyword arguments can be used together, but positional arguments must come before keyword arguments.

volume(10, 20000000, height=333330)  # Calling the function with positional and keyword arguments
print(volume())








def positional_and_keyword_arguments(lenght, breadth, height):
    print(lenght, breadth, height)
    volume = lenght * breadth * height
    return volume

v= positional_and_keyword_arguments(10, breadth=20, height=30)  # Calling the function with positional and keyword arguments 
# v= positional_and_keyword_arguments(length=10, 20, 30)  # Calling the function with positional and keyword arguments
# v = positional_and_keyword_arguments(10,20, height2=30) # Calling the function with positional and keyword arguments
# v=positional_and_keyword_arguments(10,20, breadth=0.3)  # Calling the function with positional and keyword arguments