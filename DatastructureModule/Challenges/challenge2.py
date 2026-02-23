
import array
import bisect

# Sorting List

List = [1,2,3,4,5,6,7,88,99,11]
List2 = [1,2,3,4,5,6,7,1,2,22]

# Function to sort list
def insertion_sort(ele):
    sorted_list=[]
    for e in ele:
        bisect.insort(sorted_list, e)
        print(sorted_list)
        return sorted_list
    
s_list=insertion_sort(List2)
print('Sorted List', s_list)






# Find First duplicate ele in array

list3 = [1, 2, 3, 2, 3, 4, 5, 6, 7, 1, 2, 22]

def find_duplicates(lst):
    num = set()
    for n in lst:
        if n in num:
            return n
        num.add(n)
    return -1  # No duplicates found

# Call and print result
result = find_duplicates(list3)
print("First duplicate:", result)
