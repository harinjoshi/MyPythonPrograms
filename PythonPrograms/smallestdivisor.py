#program to find smallest divisor of an integer

n = int(input())
a= []
for x in range(2,n+1):
    if n%x==0:
        a.append(x)
a.sort()
print(a[0])