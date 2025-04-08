#Class Variables = shared among all instances of a class
                    #Defined outside the constructor
                    #Allow you to share data among all objects created from the class

'''class Student:
    class_year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Shrek", 45)
student2 = Student("Donkey", 35)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(student2.name)
print(student2.age)'''

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  # Output: Buddy
print(dog1.species)  # Output: Canine
print(f"the age of the dog is {dog1.age}")
