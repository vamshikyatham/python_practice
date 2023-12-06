def fabonacii(n):
    a=1;
    b=0;
    for i in range(1,n+1):
        print(b)
        a=a+b;
        b=a-b
    print()
fabonacii(10)
