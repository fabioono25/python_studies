# objects definition: class, object, method, attribute, constructor, inheritance, polymorphism, encapsulation, abstraction
# 1. class: a blueprint for creating objects
# 2. object: an instance of a class
# 3. method: a function defined in a class
# 4. attribute: a variable bound to an instance of a class
# 5. constructor: a special method that initializes an object

age = 8
print(age.real)

# classes


class Dog:
    # class attribute
    species = "mammal"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


roger = Dog("Roger", 5)
print(type(roger))
print(roger.name)
print(roger.bark())