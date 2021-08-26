numList = input("Insert a set of numbers seperated by a comma: ").split(",")
for idx, i in enumerate(numList):
    numList[idx] = i.strip()

tup = tuple(numList)

print(numList, tup)