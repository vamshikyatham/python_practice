def abcd_patten(n):
    k,j=1,65
    while(k<=n+1):
        for i in range(1,k):
            print(chr(j),end=" ")
            j=j+1
        print()
        k=k+1;
abcd_patten(5)
