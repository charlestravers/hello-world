class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Charlie", 25)
p1.myFunc()
