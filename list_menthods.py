"""
list.append(2) :-> adds the element to end of the list.
list.extend(1,2):-> adds the elements  end of a list(or any iterable), to the end of the current list.
list.clear() :-> removes  all the items in  the list.
list.copy() :-> copy the one list to another
list.pop() :-> removes the last element of the list.
list.remove("a") :-> removes the element from the list.
list.index("a") :-> finds the index number of the element in the list.
list.insert(index number,element):-> adds the element at the specified position
list.sort()  :-> sort in list (only IF have all numbers or all strings not both at a time)
list.count("a")  :->returns number of elements with this
list. reverse() :-> reverse the list """
# append
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)
list1.append(9)
print(f"9 append at the end :{list1}")

# extend
list2 = [10, 11]
list1.extend(list2)
print(f"After extend adds 10,11 at the end : {list1}")

# remove
list1.remove(11)
print(f"remove the 11 element :{list1}")

# pop
list1.pop()
print(f"After pop() :{list1} pops the last element")
list1.pop(3)
print(f"After pop(3) :{list1} pops the 3rd index element")

# insert
list1.insert(3, 4)
print(f"After insert 4 in 3rd index:{list1}")

# reverse
list1.reverse()
print(f"After reversing the list :{list1} ")

# sort
list1.sort()
print(f"After sorting the list:{list1}")

# count
c = list1.count(1)
print(f"counts the 1 in the list:{c}")

# index
i = list1.index(2)
print(f"find the index of the element (2): {i}")

# copy
list3 = list1.copy()
print(f"copes the list1 to list3 : {list3} ")

# clear
list3.clear()
print(f"After clear the list3 is empty:{list3} ")
