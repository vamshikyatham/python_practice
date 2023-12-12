import random

print("Wellcome To Password Generator ")
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@$&1234567890"
number = int(input("Enter number of passwords  you want:"))
length = int(input("Length of the password you want:"))
print("Here your Passwords:")
for pw in range(1,number+1):
    password = ""
    for c in range(length):
        password = password+random.choice(char)
    print(pw,":",password)
