text = "Hello"
print(len(text))  # Output: 5

text = "HELLO"
print(text.lower())  # Output: hello

text = "hello"
print(text.upper())  # Output: HELLO

text = "python is fun"
print(text.capitalize())  # Output: Python is fun

text = "python is fun"
print(text.title())  # Output: Python Is Fun

text = "  Hello  "
print(text.strip())  # Output: Hello

text = "I like Java"
print(text.replace("Java", "Python"))  # Output: I like Python

text = "Hello World"
print(text.find("World"))  # Output: 6

print("Hello".startswith("He"))  # Output: True
print("Hello".endswith("lo"))    # Output: True

text = "a,b,c"
print(text.split(","))  # Output: ['a', 'b', 'c']

words = ['a', 'b', 'c']
print("-".join(words))  # Output: a-b-c

text = "banana"
print(text.count("a"))  # Output: 3