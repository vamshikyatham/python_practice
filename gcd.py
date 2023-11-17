def gcd(a,b):
    if(a==0):
        return b;
    if(b==0):
        return a;
    if(a==b):
        return a;
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)

#main code
a=10
b=12
if(gcd(a,b)):
    print("Gcd of a=%d and b=%d is %d"%(a,b,gcd(a,b)));
else:
    print("not define")
