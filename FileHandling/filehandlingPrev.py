
import os

with open("day1.txt", "r") as f :
    data = f.read()
    print(data)


with open("day1.txt", "w") as f :

    data1 = f.write("JJJJJJJ")

    os.remove("sample.txt")


with open("day1.txt", "w") as f:
    f.write("HI everyone \ni am learning Java\n")
    f.write("Java is good backend language\n")


with open("day1.txt", "r") as f :

        data = f.read()

        print(len(data))

        num= data.split(",")
        print(num)



def cal_sum(a, b):
    sum = a+b
    return sum




cal_sum(20, 77)
print(cal_sum(20, 77))


def prin_value():
    a = print("hello")
    return a

    print(prin_value)


a = 2
b = 3

d=200/3
print(d)



x = int(input("Enter data "))
y = int(input("enter data "))

data = x*y
print(data)