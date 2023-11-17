#minimum of two numbers
def min(a,b,c):
    if a<b and a<c:
        print("a is minimum")
    elif b<c and b<a:
        print("b is minimum")
    else:
        print("c is minimum")
#main code
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
min(a,b,c)
