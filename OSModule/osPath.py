


import os

# Example path
path = "/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py"

#Absolute path
print(os.path.abspath("osModule.py"))        #"/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py

#Base name (file or last folder)
print(os.path.basename(path))             # osModule.py

#Directory name
print(os.path.dirname(path))            

#Check if path exists
print(os.path.exists(path))               # True or False

#Check if it's a file
print(os.path.isfile(path))               # True

#Check if it's a directory
print(os.path.isdir(path))                # False

#Get file size in bytes
print(os.path.getsize(path))              # e.g., 1234

#Join paths safely
print(os.path.join("/Users/hanumantbhojane/Desktop/", "pythonPractice", "OSModule/osModule.py"))  

#Split path into (dir, file)
print(os.path.split(path))              

#Split file and extension
print(os.path.splitext(path))             

#Real (resolved) path
# print(os.path.realpath("file.txt"))       

#Relative path (from current dir)
print(os.path.relpath(path))              

#Check if two paths point to the same file
# print(os.path.samefile(path, os.path.realpath("file.txt")))  # True or False

#Is absolute path?
print(os.path.isabs(path))   


## Practice Exmples


import os

a= os.path.exists("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")
print("This Path is available", a)

b= os.path.exists("/Users/hanumantbhojane/Desktop/OSModule/osModule.py")
print("This Path is available", b)


c= os.path.isfile("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")
print("This file is available", c)


d= os.path.isdir("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/")
print("This directory is available", d)



e= os.path.split("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")
print("My spilited path", e)


f= os.path.join("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/", "osModule.py")
print("My joined Path", f)


g= os.path.basename("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")
print("My file basename path", g)


# h= os.path.dirname("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/", "osModule.py")
# print("My dirname Path", h)



i= os.path.getatime("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")
print("My file created time is", i)

import time

print(time.ctime(os.path.getatime("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/osModule.py")))


