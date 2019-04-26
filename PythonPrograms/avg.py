#Program to Calculate Average of numbers in a list

n = int(input("enter number:")) #Number of elements in list
avg = [] #List declaration
for x in range(0,n):
    element=int(input("enter element"))
    avg.append(element)  #Adding elements in list
avg=sum(avg)/n
print("Avarage=", round(avg,2)) #rouding off to 2 decimal points
