lst = input().split(",")
lst2 = [int(x) ** 2 for x in lst if int(x) % 2 == 1]
print(lst2)