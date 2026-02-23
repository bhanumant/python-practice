


# Functions in python


name ="Hanumant Bhojane"

def greet ():
    print("Hanumant Bhojane", greet())


    def greet_user(name):
        print("hello", greet_user(name))
 
        

a = 20
b = 50
c=60

def add (a, b):
    return a +b
print(add(a, b))


def subtract(a, b):
    return a-b
print(subtract(a, b))


def multiply(a, b):
    return a*b
print(multiply(a, b))


def divide(a, b):
    if b==0:
        return "Can not divide by zero"
    return a / b
print(divide(a, b))


str= "seasia Infotech"
str2="Hnaumant Bhojane"

def string_lenght(str):
    return len(str)
print("string length:", string_lenght(str))
print("string length:", string_lenght(str2))


def string_uppercase(str):
    return str.upper()
print("string uppercase:", string_uppercase(str))
print("string uppercase:", string_uppercase(str2))
