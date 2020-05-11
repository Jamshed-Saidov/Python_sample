class Person
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

x = Person("John", 35)
print(x)
