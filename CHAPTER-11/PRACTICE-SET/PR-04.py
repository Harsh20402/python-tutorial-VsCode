# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex:
    def __init__(self, real, imag):
        # Initialize the real and imaginary parts
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Overload the + operator to add two complex numbers
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def __mul__(self, other):
        # Overload the * operator to multiply two complex numbers
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + self.imag * other.real
        return Complex(new_real, new_imag)

    def __str__(self):
        # Return a string representation of the complex number
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

# Example usage
c1 = Complex(3, 2)
c2 = Complex(1, 7)

print("Complex Number 1:", c1)
print("Complex Number 2:", c2)

# Addition
c3 = c1 + c2
print("Addition (c1 + c2):", c3)

# Multiplication
c4 = c1 * c2
print("Multiplication (c1 * c2):", c4)
