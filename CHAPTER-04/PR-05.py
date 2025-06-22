# Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

# Define a tuple with numbers including some zeros
a = (7, 0, 8, 0, 0, 9)

# Use the count() method to count how many times 0 appears in the tuple
numberOfZeros = a.count(0)

# Display the number of zeros found
print(f"The number of zeros are : {numberOfZeros}")