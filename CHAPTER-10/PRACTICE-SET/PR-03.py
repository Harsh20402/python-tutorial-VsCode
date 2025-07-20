# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class Test:
  a = 10  # Class attribute

dummy = Test()

print(dummy.a)  # Accesses class attribute: 10

dummy.a = 0     # Creates an instance attribute 'a', doesn't change the class attribute

print(dummy.a)  # Accesses the instance attribute: 0