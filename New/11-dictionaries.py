# working with dictionaries: keys and values
# Dictionaries are mutable
# Dictionaries are unordered
# Dictionaries can contain any type of value

dog = {"name": "Rex", "age": 2, "isCute": True}

print(dog["name"])  # Rex
print(dog["age"])  # 2
print(dog["isCute"])  # True

print(dog.get("name"))  # Rex

print(dog.get("color", "non-defined"))  # non-defined (default value)

print(dog.pop("name"))
print(dog)
print(dog.popitem()) # remove the last key-value pair
print('dog: ', dog)

print(dog.keys())
print("age" in dog.keys())

dog["food"] = "meat"
print(list(dog.keys()))
print(list(dog.values()))
print(dog)

