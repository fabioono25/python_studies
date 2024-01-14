# Loops definition: for, while, break, continue, pass, range, enumerate, zip, list comprehension
# 1. for: iterate over a sequence
# 2. while: iterate while a condition is true
# 3. break: stop the loop
# 4. continue: skip the current iteration
# 5. pass: do nothing
# 6. range: create a sequence of numbers

count = 0
while count < 5:
    print("This is true: ", count)
    count += 1

items = ["Bob", "Rick", "David"]
for item in items:
    print('item: ', item)

for item in enumerate(items):
    print('item with index: ', item)

for item in range(3):
    print('item: ', item)

for item in range(1, 3):
    print('item: ', item)

ret = [x for x in range(10) if x % 2 == 0]
print(ret)

# break or contine
for item in range(10):
    if item == 5:
        break
    print(item)
    
