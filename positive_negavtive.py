#the given number is positive or negative
def pos_neg(n):
    if(n<0):
        print("The given number is negative=",n);
    else:
        print("The given number is positive=",n);

#main code
n=int(input("enter the number="));
pos_neg(n);
