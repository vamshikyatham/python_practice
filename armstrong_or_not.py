#the given number is armstrong or not
n=input("enter the numdber=");
sum=0;
for i in n:
    sum=sum+int(i)**len(n);

if int(n)==sum:
    print("It is a armstrong number")
else:
    print("not a armstrong number")
