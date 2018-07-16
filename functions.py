# def unlimited_arguments(args):
#     for argument in args:
#         print(argument)

# unlimited_arguments([1,2,3,4])

def unlimited_arguments(*args):
    for argument in args:
        print(argument)

unlimited_arguments(1,2,3,4)
unlimited_arguments([1,2,3,4])
unlimited_arguments(*[1,2,3,4])

def unlimited_argumentsLists(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

unlimited_argumentsLists(1,2,3,4, name='Max', age=29)