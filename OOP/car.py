class Car:
    top_speed = 100
    warnings = []

    def drive(self):
        print('I am driving not faster than {}'.format(self.top_speed))

#creating an object base on class
car1 = Car()
car1.drive()

# Car.top_speed = 1000
car1.warnings.append('new warning')
# car1.top_speed = 99

car2 = Car()
car2.drive()
print(car2.warnings)

car3 = Car()
car3.drive()
print(car2.warnings)

'''I am driving not faster than 100
I am driving not faster than 100
['new warning']
I am driving not faster than 100
['new warning']'''