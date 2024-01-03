n = int(input("Enter number of lines:\n"))
m = int(input("Length of the line:\n"))
for i in range(n // 2):
    j = int((2 * i)+1)
    print((".|." * j).center(m, "-"))
print('WELCOME'.center(m, '-'))
for i in reversed(range(n//2)):
    j =int((2* i)+1)
    print((".|." * j).center(m, "-"))


"""
OUTPUT:
Enter number of lines:
Length of the line:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
