
# Dicts in python are mutable and unorderd collections of key-value pairs.

my_dicts = {
    "Name": "Hanumant Bhojane", 
    "Age": 30,
    "city": "Pune", 
    "is_student": False,
    "Skills": ["Python", "Java", "Js"],
    "Address": {
        "street": "Mg Road Solapur",
        "state": "Maharashtra",
        "country": "India",
        "pincode": 413601
    }
}

print(my_dicts)
print(type(my_dicts))
print(my_dicts["Name"])
print(my_dicts["Skills" ])
print(my_dicts["Address"]["state"])
print(my_dicts.get("Age"))
print(my_dicts.get("Country", "Not found"))
print(my_dicts.keys())
print(my_dicts.values())
print(my_dicts.items())
print("Is age key present?", "Age" in my_dicts)
print("add char in dicts", my_dicts.setdefault)
print("Add key-value pair:", my_dicts.setdefault("Country", "Usa"))
print("My updated Dicts", my_dicts)

# Loop through dicts

for key, value in my_dicts.items():
    print(f"{key}:{value}")