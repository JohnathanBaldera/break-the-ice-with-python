my_list = []

while True:
    name_age_scores = input().split(",")
    if not name_age_scores[0]:
        break
    my_list.append(tuple(name_age_scores))

my_list.sort(
    key=lambda x : (x[0], x[1], x[2])
)

print(my_list)
