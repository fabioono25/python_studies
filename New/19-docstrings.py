# Docstrings definition: it is a string that is the first statement in a module, function, class, or method definition.
# Docstrings purpose: it is used to document the purpose of a module, function, class, or method.

""" 
This is a docstring on the top.
  Test
  Test
  Another test
"""


def my_function():
    """This is a docstring inside the function."""
    pass


print(my_function.__doc__)


class MyClass:
    """This is a docstring inside MyClass."""
    pass


print(MyClass.__doc__)

print(help(MyClass))