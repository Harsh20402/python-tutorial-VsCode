# Write __str__() method to print the vector as follows: 
# 7i + 8j +10k  
# Assume vector of dimension 3 for this problem.


class Vector:
    def __init__(self, components):
        if len(components) != 3:
            raise ValueError("This class supports only 3-dimensional vectors.")
        self.components = components  # [i, j, k]

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        # Dot product
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        # Custom string format: ai + bj + ck
        return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"

# Example usage
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("Vector 1:", v1)
print("Vector 2:", v2)

v3 = v1 + v2
print("Sum (v1 + v2):", v3)

dot = v1 * v2
print("Dot Product (v1 * v2):", dot)
