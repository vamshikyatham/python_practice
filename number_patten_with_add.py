def numb(n):
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1;
        print()
#main code
n=int(input("enter the number="))
numb(n)
