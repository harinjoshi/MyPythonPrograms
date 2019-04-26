#program to find count of occurance of a particular number

a = []
num1 = int(input())
for x in range(1,num1+1):
    a.append(int(input()))
k = 0
sear = int(input())
for j in a:
    if j == num1:
        k += 1
print(k)