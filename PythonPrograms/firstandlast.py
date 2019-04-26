#program to exchange first and last character of string

def firstlast(string):
    print(string [-1:])
    print(string [1:-1])
    print(string [:1])
    return string [-1:] + string [1:-1] + string [:1]


string = input()
print(firstlast(string))