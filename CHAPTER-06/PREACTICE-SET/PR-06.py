# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => O
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# Taking input marks from the user and stripping extra whitespace
stdMark = int(input("Enter Your Marks: ").strip())

# Check if the entered marks are in the valid range (0 to 100)
if(0 <= stdMark <= 100):
  grade = ""  # Initialize an empty grade variable

  # Determine the grade based on the mark ranges
  if(stdMark >= 90 and stdMark <= 100):
    grade = "O"   # Outstanding
  elif(stdMark >= 80 and stdMark <= 89):
    grade = "A"   # Excellent
  elif(stdMark >= 70 and stdMark <= 79):
    grade = "B"   # Very Good
  elif(stdMark >= 60 and stdMark <= 69):
    grade = "C"   # Good
  elif(stdMark >= 50 and stdMark <= 59):
    grade = "D"   # Pass
  else:
    grade = "F"   # Fail

  # Print the final grade
  print(f"Your grade is {grade}")

else:
  # If marks are not within 0–100, show an error message
  print("Marks should be between 0 and 100.")
