# working with sets
# Sets are mutable
# Sets are unordered
# Sets can contain any type of value
# Sets can contain duplicates

# examples of how to use sets in Python:
names1 = {"John", "Jane", "Joe", "Joe", "Joe"}
names2 = {"John", "Bob"}

print (names1 & names2) # intersection
print (names1 | names2) # union
print(names1)

names1.add("Bob")
print(names1)


print(names1.difference(names2))
print(names1.intersection(names2))
print(names1.union(names2))
print(names1 > names2)