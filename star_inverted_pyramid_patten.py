def invertedpyramid(n):
    j=n
    for i in range(1,n+1):
       print(" "*(i)+" *"*j)
       j=j-1
  
invertedpyramid(5)
