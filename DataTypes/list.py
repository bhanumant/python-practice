
my_list = [10, 20, 30, 40]
# List
print("List Operations:")
print("List:", my_list)
print("List Length:", len(my_list))
print("List Indexing:", my_list[0])
print("List Slicing:", my_list[1:3])
print("list append:", my_list.append(10))
print("List after append:", my_list.append(50))


#loop on list

for item in my_list:
    print("items in this list:", item)


    for i in range(len(my_list)):
        print("items :", my_list[i])