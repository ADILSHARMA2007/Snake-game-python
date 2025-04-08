#how to create your own class
class Dog:
    def __init__(self):
        pass
    def add(self, x):
        return x+1
    def bark(self):
        print("bark")
d = Dog()
print(d.add(10))
d.bark()
