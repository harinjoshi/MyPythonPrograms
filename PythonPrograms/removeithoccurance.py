#program to remove ith occurance of the given word in the list.

def removeword(list1, word, occur) :
    count = 0
    for x in range(0,len(list1)):
        if list1[x] == word:
            count += 1
            if count == occur:
                del(list1[x])
                return True
    return False


a = []
list1 = list(map(str, input().split()))
word = input()
flag = removeword(list1, word,occur)
if flag == True :
    print(list1)
else:
    print("Item not updated")