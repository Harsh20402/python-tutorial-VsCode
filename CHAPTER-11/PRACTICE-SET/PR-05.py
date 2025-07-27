# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them. 

class Vector:
    def __init__(self, components):
        # Store the vector as a list of components
        self.components = components

    def __add__(self, other):
        # Overload the + operator to perform element-wise addition
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # Overload the * operator to calculate dot product
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product

    def __str__(self):
        # Nicely format the vector for display
        return f"Vector({', '.join(map(str, self.components))})"

# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

# Vector addition
v3 = v1 + v2
print("Sum (v1 + v2):", v3)

# Dot product
dot = v1 * v2
print("Dot Product (v1 * v2):", dot)
