def split_and_join(line):
    a=line.split(" ")
    return "-".join(a)
    
line = input()
result = split_and_join(line)
print(result)

'''
input:
this is a string
output:
this-is-a-string

''''
  
