lst = input().split(",")
for idx, i in enumerate(lst):
    lst[idx] = i.strip()
lst.sort()
print(", ".join(lst))