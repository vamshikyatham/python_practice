def largest(lst):
    max_list = 0
    for i in lst:
        if i > max_list:
            max_list = i
        else:
            max_list = max_list
    print(max_list)


lsts = [1, 2, 3, 4, 5, 999]
largest(lsts)
