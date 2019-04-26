#program to implement identity matrix

n1=int(input())
for i in range(0,n1):
    for j in range(0,n1):
        if i==j:
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()