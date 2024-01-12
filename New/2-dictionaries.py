# Dictionaries: store key-value pairs
# Keys must be unique
# Values can be any type
# Keys can be any immutable type (string, number, tuple)
# Values can be any type (list, dictionary, tuple, string, number)

# Create a dictionary
dict = {'name': 'John', 'age': 25, 'city': 'New York'}

choices = {"player": "rock", "computer": "paper"}

# Access a value
print(dict['name'])
print(choices['player'])

# Add a key-value pair
dict['job'] = 'Developer'
print(dict)
