#program to exchange first and last character of string

def rmv(string, n):
    first = string[:n]
    last = string[n+1:]
    return first + last
string = input()


n = int(input())
print(rmv(string,n))

