def fibonacci(n):
    i=0;
    a=1;
    b=0;
    while i<=n-1:
        print(b);
        a=a+b;
        b=a-b;
        i=i+1;
#main code
n=int(input("enter the number="))
fibonacci(n)
