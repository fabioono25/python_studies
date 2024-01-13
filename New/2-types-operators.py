# Types in Python:
name = "John"
print(type(name))
print(type(name) == str)
print(isinstance(name, str)) # string is instance because it is a subclass of object

age = 2
print(isinstance(age, int)) # integer is instance because it is a subclass of object
print(isinstance(age, float)) # integer is not instance because it is not a subclass of float

median = 2.5
print(type(median))

age = float(age)
print(type(age))

age = "12"
print(type(age))

age = int(age)
print(type(age))

# number = "test"
# age = int(number)

# complex for complex numbers
# bool for boolean values
# list for lists
# tuple for tuples
# range for range objects
# dict for dictionaries
# set for sets

# booleans
print(True)

# complext numbers
print(2 + 1j)
num = complex(2, 1)
print(num)
print(num.real)
print(abs(-4.4))
print(round(4.4))

print(round(5.49))
print(round(5.49, 1))

# working with operators
# Arithmetic Operators
print(50*'-')
print(1 + 1) # addition
print(1 - 1) # subtraction
print(1 * 1) # multiplication
print(4 / 3) # division
print(4 % 3) # modulus
print(1 ** 1) # exponentiation
print(4 // 3) # floor division
print(1 + -1)
age += 20
print(age)

print( 0 or 1 )
print(False or 'hey')
print('hi' or 'hey')
print([] or False)
print([] and False)
print('asdas' or False)
print(False and 'asdasd')
print(True and 'asdas')

# identity operator
print(age is 12)
print(age is not 12)

names = ["John", "Jane", "Jack"]
print("John" in names)

def is_adult(age):
  return True if age > 18 else False # ternary operator

print(is_adult(20))



