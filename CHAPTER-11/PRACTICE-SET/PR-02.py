# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

# Base class
class Animals:
    def __init__(self):
        print("✅ Animal created")

    def info(self):
        print("This is an animal.")

# Derived class from Animals
class Pets(Animals):
    def __init__(self):
        # Call constructor of Animals
        super().__init__()
        print("✅ Pet created")

    def pet_info(self):
        print("This animal is a pet.")

# Derived class from Pets
class Dog(Pets):
    def __init__(self):
        # Call constructor of Pets (which calls Animals too)
        super().__init__()
        print("✅ Dog created")

    def bark(self):
        print("🐶 Woof! Woof!")

# Create a Dog object
tommy = Dog()

# Call methods from all levels
tommy.info()       # From Animals
tommy.pet_info()   # From Pets
tommy.bark()       # From Dog
