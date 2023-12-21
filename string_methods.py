# All string methods returns new values. They do not change the original string.(13)
# capitalize
string = "the captain of indian cricket team is rohit sharma"
print("Original string : ", string)
x = string.capitalize()
print("After capitalize : ", x)

# center
x = string.center(100)
print("Moved toward the center:", x)

# Count
x = string.count("a")
print("counts number of 'a' present in string:", x)

# Endswith
x = string.endswith("a")
print("Return True or False:", x)

# Index
x = string.index("of")
print("Return the index number of the given string: ", x)

# Find
x = string.find("of")
print("Return index of the finding string:", x)

# Join
list1 = [" VAMSHI", "KYATHAM"]
x = " ".join(list1)
print("joins the list into a string :", x)

# Stars with
x = string.startswith("th")
print("Return True or False:", x)

# Split
x = string.split()
print("Split into list :", x)

# Swap case
x = string.swapcase()
print("Converts lower case to upper case and vice versa :", x)

# Lower case
x = string.lower()
print("converts all to lower case:", x)

# Upper case
x = string.upper()
print("Converts all to upper case : ", x)

# Replace
x = string.replace("rohit sharma", "'K L rahul'")
print("Replaced the rohit sharma to K L rahul :", x)
