potential_passwords = input().split(",")
print(potential_passwords)
good = []
for i in potential_passwords:
    cap = 0
    lower = 0
    num = 0
    special = 0
    length = 0
    for char in i:
        length += 1
        if char.islower():
            lower += 1
        elif char.isupper():
            cap += 1
        elif char.isdigit():
            num += 1
        elif char == "@" or char =="$" or char == "#":
            special += 1
    if cap >= 1 and lower >= 1 and num >= 1 and special >= 1 and length >= 6 and length <= 12:
        good.append(i)

print(",".join(good))

#Test Case: ABd1234@1,a F1#,2w3E*,2We3345