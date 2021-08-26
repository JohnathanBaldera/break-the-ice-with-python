from math import sqrt

def formula(nums):
    return sqrt((2 * 50 * nums) / 30)
    

numList = input("Enter a list of numbers seperated by a comma: ").split(",")

for idx, i in enumerate(numList):
    numList[idx] = int(i.strip())


print(numList)
for i in numList:
    print(str(round(formula(i))), end=", ")

