

# Tuples Operations

my_new_tuple= (10,20,30,40,50,60, 70, 80, 80)

print(my_new_tuple)
print("Tuple Operations:", my_new_tuple)
print("tuples lengh:", len(my_new_tuple))
print("tuples index:", my_new_tuple[0])
print("tuples slicing:",my_new_tuple[1:5])
print("tuples count:", my_new_tuple.count(10))
print("tuples count:", my_new_tuple.count(80))
print("tuples index:", my_new_tuple.index(10))
print("tuples index:", my_new_tuple.index(80))
print("tuple join:", my_new_tuple+(90,100))
print("tuple repeat:" , my_new_tuple*2)
print("tuple convert to list:", list(my_new_tuple))
print("tuple converts into set:", set(my_new_tuple))
print("tuple converts into string:", str(my_new_tuple))
print("tuple converts into dictionary", dict(enumerate(my_new_tuple)))
print("touple reversing:",my_new_tuple[::-1])
print("remove elements from tuple:", my_new_tuple[1:5])
print("add elements in tuple:", my_new_tuple+(8000, 5000))
print("tuple with single elements", (20,))
print("tuple with single elements", (80,))
print("tuple with single elements", (100,))

# List [], Set {}, Tuple ()