a = input()
total, string = 0, ""

for i in range(4):
    string += a
    total += int(string)

print(str(total))