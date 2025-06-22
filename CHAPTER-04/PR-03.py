# Check that a typle cannot be changed in python.

myTuple = (1, 2, 3)

# This will cause an error because tuples are immutable
myTuple[0] = 100

print(myTuple)
