# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, components):
        # Store the vector components as a list
        self.components = components

    def __add__(self, other):
        # Element-wise addition
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension for addition.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # Dot product
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __len__(self):
        # Return the dimension of the vector
        return len(self.components)

    def __str__(self):
        # Format for 3D vector if applicable
        if len(self.components) == 3:
            return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"
        else:
            # Fallback for n-dimensional vector
            return f"Vector({', '.join(map(str, self.components))})"

# Example usage
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Dimension of Vector 1:", len(v1))  # Will use __len__()

v3 = v1 + v2
print("Sum:", v3)

dot = v1 * v2
print("Dot Product:", dot)
