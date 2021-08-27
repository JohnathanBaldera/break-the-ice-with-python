numbers = 0
letters = 0

string = input()
for i in string:
    if i.isalpha():
        letters += 1
    elif i.isalnum():
        numbers += 1
print(f"LETTERS: {str(letters)}")
print(f"DIGITS: {str(numbers)}")