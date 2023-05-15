class Dog:
    def bark(self):
        print("Woof!")
        
d = Dog()
d.bark()
print(type(d))

class Cat:
    def __init__(self, name):
        self.name = name
        print(name)
    def meow(self):
        print("Meow!")
        
c = Cat("Felix")
c2 = Cat("Tom")

class Animal:
    def __init__(self, name):
        self.name = name

    def falar(self):
        print(f"{self.name} diz: Miau!")

a = Animal("Garfield")
a.falar()