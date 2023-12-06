def ascii(n):
    k=0
    while(k<=n):
        for i in range(65,65+n):
            print(chr(i),end=" ")
        k+=1
        print()
ascii(5)
