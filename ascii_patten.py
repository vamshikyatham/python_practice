def ascii(n):
    a=65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(a),end=" ")
        a=a+1
        print()
#main code
n=int(input("enter the number="))
ascii(n)
