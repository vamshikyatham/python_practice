#given number is palindrome or not
n=input("enter the number=")
rev=n[::-1]
if(rev==n):
    print("it is a palindrome=",n,"-->",rev);
else:
    print("it is not a palindrome=",n,"-->",rev);
    
