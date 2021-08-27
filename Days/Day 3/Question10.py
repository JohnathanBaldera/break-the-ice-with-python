def sortNoRepeats(string):
    lst = string.split(" ")
    lst = sorted(list(set(lst)))
    return " ".join(lst)

print(sortNoRepeats(input()))