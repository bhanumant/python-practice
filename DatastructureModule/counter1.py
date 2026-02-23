
from collections import Counter


L=["Js", "Java", "Js", "Ts", "Py", "C#", "Py", "Html", "Java"]
LL=( "Js", "Java", "Js", "Ts", "Py", "C#", "Py", "Html", "Java")
# LLL={"Js", "Java", "Js", "Ts", "Py", "C#", "Py", "Html", "Java"}

print(L)
# Count the no of times occurance in list
print(Counter(L))
print(Counter(LL))
# print(Counter(LLL))

c=Counter(L)
print(c["Js"])       # Access like a dictionary
print(c.get("Java"))  
print(c.get("Py")) 
print(c.keys()) 
print(c.values()) 


c.update({'Ruby':4})
print(c)
d=c.elements()
print(d)

print(c.most_common(1))
print(c.most_common(2))


