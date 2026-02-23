
text = "Hello, World!"
# String 
print(type(text))
print("firstCharactor:", text[0])
print("lastCharactor", text[-1])
print("substring:", text[0:5])
print("upperCase:", text.upper())
print("lowerCase:", text.lower())
print("replace:", text.replace("Hello", "Hi"))
print("replace:", text.replace("World", "Hanumant"))
print("split", text.split(", "))
print("join:", ",".join(["Hello", "World", "Hanumant"]))
print("lenght:", len(text))
print("count:", text.count("l"))
print("find:", text.find("Hello"))
print("find:", text.find("Hanumant")) #Returns -1 if not found
print("startswith:", text.startswith("Hello"))
print("endswith:", text.endswith("!"))
print("add string:", text + "How are you?")
