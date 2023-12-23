# if __name__ == ' __main__ ':
n = int(input("no of commands :"))
list1 = []
clist = []
for i in range(n):
    command = input("Input command:").split()
    if command[0] == "append":
        list1.append(command[1])
    elif command[0] == "copy":
        clist = list1.copy()
    elif command[0] == "insert":
        list1.insert(int(command[1]), str(command[2]))
    elif command[0] == "reverse":
        list1.reverse()
    else:
        print(list1, clist)
print(list1, clist)
