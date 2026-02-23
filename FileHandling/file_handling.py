
# 1. Opening and Writing to a File
file_path = "myNewFile.txt"


# Open file in write mode
with open (file_path, 'w') as file1:
    file1.write("Hello This is my first file handling programme.\n")
    file1.write("Hi I am Hanumant Bhojane")

print("File write is done")



# 2. Appending to a File
with open(file_path, 'a') as file1:
    file1.write("This line is need to append \n")

    print("append Completed")


# 3. Reading from a File
with open(file_path, 'r') as file1:
       content =  file1.read()
       print(content)

       print("read Completed")


# 4. Reading Line by Line
with open(file_path, 'r') as file1:
           for lines in file1:
               print(lines.strip())


# 7. Checking if file exists

import os
if os.path.exists(file_path):
 print(f"${file_path} exist")
else:
 print(f"${file_path} not exist")


# 8. Deleting a file
# os.remove('day1.txt')
# print("file is deleted")