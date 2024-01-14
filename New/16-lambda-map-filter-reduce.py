# lambda functions definition: lambda <parameters>: <expression>
# lambda functions are anonymous functions that can be used to create a function without a name
# map: map a function to an iterable
# filter: filter an iterable based on a function
# reduce: reduce an iterable to a single value


lambda num: num * 2


def multiply(a, b): return a * b


print(multiply(2, 3))  # 6

numbers = [1, 2, 3]


def double(a):
    return a * 2


def double_lambda(a): return a * 2

# working with map:


result = map(double, numbers)
print(list(result))  # [2, 4, 6]

result = map(double_lambda, numbers)
print(list(result))  # [2, 4, 6]

result = map(lambda a: a * 2, numbers)
print(list(result))  # [2, 4, 6]

# working with filter:


def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)
print(list(result))  # [2]

result = filter(lambda n: n % 2 == 0, numbers)
print(list(result))  # [2]

# working with reduce:

from functools import reduce
expenses = [('Dinner', 100), ('Lunch', 50)]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)  # 170


expenses = [('Dinner', 100), ('Lunch', 50), ('Breakfast', 20)]

total_expense = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), expenses)
print(total_expense)