

import os


# print(dir(os))
print(dir(os.getcwd()))


if (not os.path.exists("data")):
    os.mkdir("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/data")  ## Creating a folder just passing path


# # creating 5 files
# for i in range(0, 5):
#     os.mkdir(f"/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/data/day{i+1}")



folders=os.listdir("/Users/hanumantbhojane/Desktop/pythonPractice/OSModule/data")
print(folders)


for folder in folders:
    print(folder)