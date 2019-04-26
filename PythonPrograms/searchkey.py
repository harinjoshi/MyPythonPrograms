#program to check  whether searched key is present or not

d = {'A': 1,'B' : 2,'C':3}
key = input()
if key in d.keys():
    print(d[key])
else:
    print("key not present")