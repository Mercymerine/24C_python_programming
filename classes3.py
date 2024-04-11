class Person:
    def __init__(self, age, weight, height, color):
        self.age = age
        self.weight = weight
        self.height = height
        self.color = color

    def walk(self):
        print('You can walk')

    def run(self):
        print('You can run')

#Creating object
mercy = Person( 23, 50, 150, 'Chocolate')
eric = Person(25, 78, 170, 'Black')


mercy.walk()
eric.run()