
file = open("myTextFile.txt", 'r')
# str = file.read()
# print (str)


str = file.read(8)
print (str)


str = file.read(12)
print (str)


# Output
#  Hello I am Learning Python
# also I am Learning Java 
# I am leaning AI testing
# Hello I
# am Learning

print (type(str))

# Output
#  <class 'str'>




file1 = open("myNewFile.txt", 'w')  # it creates file in write mode if not exist 
str1 =file1.read()

print(str1)


file2 = open("myNewFile.txt", 'w')
file2.write("Seasia")
with open("myNewFile.txt", 'r') as file2:
    string1 = file2.read()
    print(string1)
