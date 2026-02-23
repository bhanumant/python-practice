


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3= {22,11,33,44,555,66}
set4 = {1, 2, 3, 4}

# Set Operations
print("set operations:")
print("Set 1:", set1)
print("set 2:", set2)
print('set 3:', set3)
print("Set lenght", len(set1), len(set2), len(set3))
print("Set Union:", set1.union(set3), set2.union(set3)) # Combine all elemnets both sets
print("Set Intersection:", set1.intersection(set2)) # finds common ele
print("set defference:", set1.difference(set2)) #find elements in set1 that are not in set2
print("set symmetruc difference:", set1.symmetric_difference(set2)) #find ele that are in either set but not both
print("set issubset:", set1.issubset(set4))  # return true
print("set issubset:", set1.issubset(set2)) # returns false
print("set issuperset:", set1.issuperset(set4)) # find if the set contains all the elements of another set Return true
print("set issubset:", set1.issuperset(set2)) # returns false
