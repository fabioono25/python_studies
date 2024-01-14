# decorators: functions that take a function as an argument and return a function
# alter how a function works

def logtime(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@logtime
def hello():
    print("Hello")


# call the function
hello()
