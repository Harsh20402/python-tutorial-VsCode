# Open two files at once using a single 'with' statement
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    # Read content from both files
    data1 = f1.read()
    data2 = f2.read()

print("Contents of file1:")
print(data1)

print("Contents of file2:")
print(data2)
