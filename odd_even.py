#given number is odd or even number 
def even_odd(n):
    if(n%2==0):
        print("THE GIVEN NUMBER IS EVEN=",n);
    else :
        print("THE GIVEN NUMBER IS ODD=",n);
#main code
n=int(input("enter the number="))
even_odd(n)
