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

"""
class solution:
    def single(self, list2):
        self.list2 = list2
        print(self.list2)
        length = len(self.list2)
        for i in range(length):
            count = 0
            for j in range(length):
                if self.list2[i] == self.list2[j]:
                    count += 1
            if count == 1:
                print("Single element in the list is :", self.list2[i])


ob = solution()
list1 = [1, 2, 3, 3, 2, 1, 3, 4]
ob.single(list1)

"""

