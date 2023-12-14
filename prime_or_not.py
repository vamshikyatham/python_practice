def prime_or_not(number):
    flag = False
    if number == 1:
        print(f"{number},is not a prime number")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
                #if it true then break the loop and come out
    else:
        print(f"{number},is not a prime number")
    if flag:
        print(f"{number},is not a prime number")
    else:
        print(f"{number},is a prime number")


num = int(input("Enter the number:"))
prime_or_not(num)

