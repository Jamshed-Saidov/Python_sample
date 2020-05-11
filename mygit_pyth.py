class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

x = Person("John", 35)
x.age = 40

print(x.name)
print(x.age)
x.myfunc()
