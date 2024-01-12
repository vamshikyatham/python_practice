# input  : [1, 2, 3, 4, 5, 6,7]
#          k = 3
# output : [5, 6, 7, 1, 2, 3, 4]
import random
def rotate(list1, k):
    print("List to rotate :", list1)
    print("no of elements to rotate from backward:", k)
    Listend = []
    Liststart =[]
    length = len(list1)
    Listend = list1[-k:length]
    Liststart = list1[0:(length-k)]
    Listend.reverse()
    Liststart.reverse()
    new_list = []
    new_list = Liststart + Listend
    new_list.reverse()
    return new_list

times = 5
for i in range(times):
    num = [1, 2, 3, 4]
    list1 =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    k = random.choice(num)
    x = rotate(list1, k)
    print(x)

