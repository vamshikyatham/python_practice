def single(list2):
    print(list2)
    length = len(list2)
    for i in range(length):
        count = 0
        for j in range(length):
            if list2[i] == list2[j]:
                count += 1
        if count == 1:
            print("Single element in the list is :", list2[i])


list1 = [1, 2, 3, 3, 2, 1, 3, 4]
single(list1)

