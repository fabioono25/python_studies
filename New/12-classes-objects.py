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

    def eat(self):
        print(f"{self.name} is eating (Dog)")

    def bark(self):
        print("Woof!")

    def __gt__(self, other):
        return self.age > other.age

class Cat:
    # class attribute
    species = "mammal"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating (Cat)")

    def meow(self):
        print("Meow!")

roger = Dog("Roger", 5)
print(type(roger))
print(roger.name)
print(roger.bark())

# polymorphism
animal1 = Dog("Roger", 5)
animal2 = Cat("Syd", 8)

animal1.eat()
animal2.eat()

# operator overloading
roger = Dog("Roger", 5)
syd = Dog("Syd", 8)

print(roger > syd)
