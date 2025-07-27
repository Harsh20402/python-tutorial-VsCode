# Define a class to represent a 2D vector
class TwoDVector:
    def __init__(self, i, j):
        # Initialize the i and j components of the vector
        self._i = i
        self._j = j

    def show(self):
        # Display the vector in 2D form: i and j components
        print(f"The vector is {self._i}i + {self._j}j")

# Define a subclass to represent a 3D vector, inheriting from TwoDVector
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        # Call the parent class constructor to initialize i and j
        super().__init__(i, j)
        # Initialize the new component k for the 3D vector
        self._k = k

    def show(self):
        # Override the show method to include the k component
        print(f"The vector is {self._i}i + {self._j}j + {self._k}k")

# Create a 2D vector instance
a = TwoDVector(1, 2)
a.show()  # Output: The vector is 1i + 2j

# Create a 3D vector instance
b = ThreeDVector(4, 5, 6)
b.show()  # Output: The vector is 4i + 5j + 6k
