# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# Taking input marks for three subjects
stdMark1 = int(input("Enter Mark 1: "))
stdMark2 = int(input("Enter Mark 2: "))
stdMark3 = int(input("Enter Mark 3: "))

# Calculating total average percentage
totalAverage = ((stdMark1 + stdMark2 + stdMark3) * 100) / 300

# Checking pass condition:
# - Total average should be >= 40
# - Each subject mark should be >= 33
passStatus = (
    totalAverage >= 40 and
    stdMark1 >= 33 and
    stdMark2 >= 33 and
    stdMark3 >= 33
)

# Final decision based on pass status
if passStatus:
    print(f"You passed! 🎉 Total average: {round(totalAverage, 2)}%")
else:
    print(f"You failed. 😞 Try again next year. Total average: {round(totalAverage, 2)}%")