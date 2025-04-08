#OBJECT= a'bundle' of related attributes (variables) and methdods(functions)
#CLASS = (blueprint) used to design the structure and layout of an object

class Car:
    #Class attribute
    def __init__(self, model, year,color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        #Instance attribute
    
car1 = Car("challenger", 2022, "black", False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
#Inheritance: allows a class to inherit properties and methods from another class

def drive(self):
    print(f"You can drive the {self.model}")

def stop(self):
    print("You can stop the car")

