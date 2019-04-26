#program to check if a number is perfect number or not

#A number is a perfect number if is equal to sum of its proper divisors,that is,
# sum of its positive divisors excluding the number itself.

#For example: 6 = 1+2+3
             28 = 14+7+4+2+1

n1 = int(input())
for x in range(2,n1+1):
    k=0
    for y in range(2,x//2+1):
        if x%y == 0 :
            k = k+1
    if k<=0:
        print(x)