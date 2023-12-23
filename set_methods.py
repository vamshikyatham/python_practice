# set -->mutable, unordered, duplicates are not allowed, unchangeable

# add
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}
set1.add(10)
print("Adding 10 to the set1 :", set1)

# copy
set3 = set1.copy()
print("copying from set1 to set3:", set3)

# clear()
set3.clear()
print("Clearing the set :", set3)

# difference
x = set1.difference(set2)
print("Show the difference of set1 only by set2", x)

# difference_update
set1.difference_update(set2)
print("Set1 is complete change because difference of the s1 to s2 ,only s1 will be changed", set1)

# intersection
set1 = {1, 2, 3, 4, 5}
x = set1.intersection(set2)
print("Show the present in the set1 and set2", x)

# intersection_update
set1 = {1, 2, 3, 4, 5}
set1.intersection_update(set2)
print("updates the intersection values in set1 :", set1)

# pop
set1 = {1, 2, 3, 4, 5}
x = set1.pop()
print("Removes an element from the set1:", set1, "POPPED element:", x)

# remove
set1.remove(2)
print("Removed a specified element from the set1", set1)

# union
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}
x = set1.union(set2)
print("Return the unique elements from the both sets:", x)

# update
set1.update(set2)
print("Update the set with another set, or any other iterable:", set1)
