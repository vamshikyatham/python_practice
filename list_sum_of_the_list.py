def sum_of_list(n):
    sum_list = 0
    for ii in n:
        sum_list += ii
    print("Sum of the list:", sum_list)


# main code
li = []
length = int(input("Length of the list:"))
for i in range(length):
    li.append(int(input("Enter the numbers :")))
sum_of_list(li)


