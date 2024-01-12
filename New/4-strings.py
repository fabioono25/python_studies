# working with strings
# Strings are immutable
# Strings are ordered
# Strings can contain any type of value
# Strings can contain duplicates
# Strings can be indexed

# examples of how to use strings in Python:

# Create a string
string = "Hello, World!"
print(string)

# Access a character in a string
print(string[0])
print(string[1])
print(string[2])

# Access a substring
print(string[0:5])
print(string[7:12])

# Access the last character in a string
print(string[-1])
print(string[-2])

# Access the last 5 characters in a string
print(string[-5:])
print(string[7:])

# Access the first 5 characters in a string
print(string[:5])

# Access every other character in a string
print(string[::2])

# Access every other character in a string, starting at the second character
print(string[1::2])

# Access every other character in a string, starting at the second character, and ending at the second to last character
print(string[1:-1:2])

# Access every other character in a string, starting at the second character, and ending at the second to last character
print(string[1:-1:2])

# functions that can be used with strings in Python
print(f"Length of string: {len(string)}")
print(f"Lowercase: {string.lower()}")
print(f"Uppercase: {string.upper()}")
print(f"Capitalize: {string.capitalize()}")
print(f"Title: {string.title()}")
print(f"Swapcase: {string.swapcase()}")
print(f"Is string alphanumeric: {string.isalnum()}")
print(f"Is string alphabetic: {string.isalpha()}")
print(f"Is string numeric: {string.isnumeric()}")
print(f"Is string decimal: {string.isdecimal()}")
print(f"Is string digit: {string.isdigit()}")
print(f"Is string identifier: {string.isidentifier()}")
print(f"Is string lowercase: {string.islower()}")

# string interpolation
print(f"Hello, {string}")
print("Hello, {}".format(string))
print("Hello, %s" % string)

# string formatting
print("Hello, {0}".format(string))

# string methods
print(string.count("l"))
print(string.find("l"))
print(string.index("l"))
print(string.replace("l", "L"))
print(string.split(","))
print(string.strip())
print(string.rstrip())
print(string.lstrip())
print(string.startswith("H"))
print(string.endswith("!"))
print(string.isupper())
print(string.islower())
print(string.isspace())
print(string.istitle())
print(string.isprintable())
