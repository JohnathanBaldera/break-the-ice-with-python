lst = []
while True:
    string = input()
    if string == "":
        break
    else:
        lst.append(string)

for i in lst:
    print(i.upper())