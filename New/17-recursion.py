# Recursion: a function that calls itself
# Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
# Usually, it is returning the return value of this function call.
# If a function definition fulfils the condition of recursion, we call this function a recursive function.

# factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# test
print(factorial(5))  # 120