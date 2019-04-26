#program to implement tuple comprehension

n1 = int(input())
n2 = int(input())
a = [(x,x**2) for x in range(n1,n2+1)]
print(a)