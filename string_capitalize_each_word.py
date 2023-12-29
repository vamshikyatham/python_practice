
def solve(s):
    string = s.split(" ")
    '''ans = (i.capitalize() for i in string)
    return " ".join(ans)
    '''
    ans=[]
    for i in string:
        ans1 = i.capitalize()
        ans.append(ans1)
    return " ".join(ans)
#Main code
s = input("Enter the string:")
result = solve(s)
print(result)
"""
Output:
Enter the string:vamshi kyatham
Vamshi Kyatham
"""
