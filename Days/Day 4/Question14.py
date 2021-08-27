def countCase(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isalpha():
            if i == i.upper():
                upper += 1
            elif i == i.lower():
                lower += 1
    return f"UPPER CASE {str(upper)}, LOWER CASE {str(lower)}"

print(countCase(input()))