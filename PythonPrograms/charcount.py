#progeam to count number of words and character in string

def charactercount(string):   #function definition
    char = 0
    word = 1
    for x in string:
        char += 1
        if x == '':
            word += 1
    return char,word


string = input()
print(charactercount(string))  #calling a function
