def patten(n):
    k=1;
    l=n-1
    for i in range(1,n+1):
        print(" "*(n-k)+" *"*i)
        k=k+1;
    for j in range(1,n+1):
        print(" "*(j)+" *"*l)
        l=l-1;
patten(5)
'''
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
  '''
