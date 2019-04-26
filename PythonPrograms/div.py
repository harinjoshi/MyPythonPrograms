#Program to print all numbers in a range divisible by given number

lower = int(input("enter lower range"))
upper = int(input("enter upper range"))
divisor = int(input("enter divisor"))
for i in range(lower,upper+1):
    if i % divisor == 0:
        print(i)