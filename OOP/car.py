class Car:
    top_speed = 100

    def drive(self):
        print('I am driving not faster than {}'.format(self.top_speed))

#creating an object base on class
car1 = Car()
car1.drive()
