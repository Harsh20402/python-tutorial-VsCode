# In Python, a string is a sequence of characters, representing text-based data. Strings are a fundamental data type and are immutable, meaning their content cannot be changed after creation.

# Different ways to define a string in Python
a = 'Harsh'       # Single quote string
b = "Harsh"       # Double quote string
c = '''Harsh'''   # Triple single quote string (can span multiple lines if needed)
d = """Harsh"""   # Triple double quote string (also can span multiple lines)

# Get the length of string 'a'
e = len(a)        # len() returns the number of characters in the string

print(e)          # Output: 5

# Accessing individual characters of the string using indexing
print(a[0])       # Output: H (1st character)
print(a[1])       # Output: a (2nd character)
print(a[2])       # Output: r (3rd character)
print(a[3])       # Output: s (4th character)
print(a[4])       # Output: h (5th character)

# Slicing the string
print(a[0:3])     # Output: 'Har' (characters from index 0 to 2)
print(a[-3:-1])   # Output: 'rs' (characters from 3rd last to 2nd last, i.e., index 2 to 3)