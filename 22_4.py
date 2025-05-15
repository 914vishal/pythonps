# Create 3 class with objects using oops concepts in python

# 1. student
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def display(self):
        print("Student Name:", self.name)
        print("Grade:", self.grade)
s1 = Student("Vishal", "btech")
s1.display()

# output:-
# Student Name: Vishal
# Grade: btech

# 2. Mobile
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Mobile Brand:", self.brand)
        print("Price: ₹", self.price)
m1 = Mobile("Samsung", 15000)
m1.display()

# output:-
# Mobile Brand: Samsung
# Price: ₹ 15000

# 3. Animal
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    def display(self):
        print("Animal Species:", self.species)
        print("Sound:", self.sound)
a1 = Animal("Dog", "Bark")
a1.display()

# output:-
# Animal Species: Dog
# Sound: Bark

