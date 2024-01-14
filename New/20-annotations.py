# Annotations definition: it is a way to add metadata to functions.
# Annotations purpose: it is used to add information about the types used in a function.

def my_function(a: int, b: int) -> str:
    return str(a + b)

# test
print(my_function.__annotations__)
print(my_function(1, 2))

count: int = 0
print(count)

