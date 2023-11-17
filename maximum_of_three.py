#maximum of two numbers
def max(a,b,c):
    if a>b and a>c:
        print("a is maximum")
    elif b>c and b>a:
        print("b is maximum")
    else:
        print("c is maximum")
#main code
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
max(a,b,c)
