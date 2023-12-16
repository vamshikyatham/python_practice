# reverse string

def rev_string(input_str):
    rev_s = ""
    for char in input_str:
        rev_s = char + rev_s
    print(rev_s)


def other_method(input_string):
    revs = input_string[::-1]
    print(revs)


rev = "abcd"
rev_string(rev)
other_method(rev)
