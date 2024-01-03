def factorial(n):
    fact = 1
    if n == 0:
        print(f"The factorial of {n} is 0")
    elif n < 0:
        print(f"Sorry, factorial does not exist for negative numbers {n}")
    else:
        for i in range(1,n+1):
            fact = fact * i
        print(fact)


factorial(6)
