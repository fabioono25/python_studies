# working with lists

things = ["Roger", 1, "Syd", True, 2.2]

things[2] = "Syd Barrett"

print(things)

print(things[2:4])

things.append("David")
print(things) 

things.insert(2, "Nick")
print(things)

things.extend(["Bob", "Rick"])
print(things)

things.append(["Bob", "Rick"])
print(things)

# difference between append and extend
# append adds the list as a single item
# extend adds the items of the list to the list

