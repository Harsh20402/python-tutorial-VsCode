# What will be the length of the following set?
# 
# s = set()
# s.add(20)
# s.add(20.0)
# a.add("20")

s = set()
s.add(20)       # Adds the integer 20
s.add(20.0)     # 20.0 is a float, but 20 == 20.0 → considered the same in a set
s.add("20")     # Adds the string "20" → a different type and value

print(f"The lenth will be: {len(s)}")
# Output: The length will be: 2