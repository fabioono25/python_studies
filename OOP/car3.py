class Car:
    #constructor
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.warnings = []
    
    #built-in method
    def __repr__(self):
        print('printing...')    
        return 'top speed: {}, Warnings: {}'.format(self.top_speed, len(self.warnings))

    def drive(self):
        print('I am driving not faster than {}'.format(self.top_speed))

#creating an object base on class
car1 = Car()
car1.drive()
# print(car1) <__main__.Car object at 0x05893310>
# print(car1.__dict__) # {'top_speed': 100, 'warnings': []}
car1.warnings.append('new warning')
print(car1.warnings)
print(car1)

'''
I am driving not faster than 100
['new warning']
printing...
top speed: 100, Warnings: 1
'''