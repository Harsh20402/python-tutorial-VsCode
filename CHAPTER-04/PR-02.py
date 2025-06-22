# Write a program to accept the marks of 6 students and display them in a sorted manner.

# Initialize an empty list to store the marks of students
marksList = []

# Take marks input from the user 6 times and convert it to an integer
# Use .strip() to remove extra spaces before conversion

# Input 1
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Input 2
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Input 3
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Input 4
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Input 5
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Input 6
inputMark = int(input("Enter the marks: ").strip())
marksList.append(inputMark)

# Sort the marks in ascending order
# The .sort() method sorts the list in-place and returns None
marksList.sort()

# Print the sorted marks list
print(f"The sorted marks list is : {marksList}")