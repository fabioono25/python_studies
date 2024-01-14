# exceptions: try, except, else, finally, raise, assert

class MyException(Exception):
    pass


def test(a, b):
    try:
        # raise MyException("MyException")
        print("try")
        print(a / b)
        # raise Exception("raise")
        # assert False, "assert"
    except ZeroDivisionError as e:
        print("except ZeroDivisionError")
        print(e)
    except Exception as e:
        print("except")
        print(e)
    else:
        print("else. code executed correctly")
    finally:
        print("finally. always executed")


fileName = "/Users/..../test.txt"

# # try:
# #     # it doesn't work
# #     file = open(fileName, "r")
# #     print(file.read())
# #     file.close()
# # finally:
# #     file.close()

with open(fileName, "r") as file:
    print(file.read())


# test
test(1, 0)
print(25*'-')
test(1, 1)
print(25*'-')
