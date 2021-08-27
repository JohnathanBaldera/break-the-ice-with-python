def check(lst):
    new_lst = []
    for i in lst:
        if int(i, 2) % 5 == 0:
            new_lst.append("1")
        else:
            new_lst.append("0")
    return "".join(new_lst)

print(check(input().split(",")))