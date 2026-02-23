

print("loops in python")

# For Loop

for i in range(5):
    print("For loop iteration:", i)

    for j in range(2):
        print("nested for loop iterations:", j)



# while loop
count = 0
while count < 5:
    print("while loop iteration:", count)
    count += 1
    if count == 3:
        print("Count reached 3!")


# For loop with else

for i in range(3):
    print("For loop with else operation:", i)


str = 'Bugraptors'

for char in str:
    print("Charactoer in this string:", char)
else:
    print("For loop completed without break")

 
str1="Hello World"

for char in str1:
 print("Character in this string:", char)
 
 if char is " ":
    print("space found breaking the loop") 
    break
 
 if char is "w":
    print ("w found continue the loop")
    continue
 
 if char is "H":
    print("H found  pass the loop")
    pass
 


 str2="Hanumant Bhojane"

 for char in str2:
    print ("Character in this string:", char)