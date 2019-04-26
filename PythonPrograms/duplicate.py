#program to remove duplicate items from a list

a = []
n = int(input())
for x in range(0,n):
    ele = int(input())
    a.append(ele)
b = set()
uniq = []
for y in a:
    if y not in b:
        uniq.append(y)
        b.add(y)
print(uniq)