def func(x, y):
    my_list = []
    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        my_list.append(tmp)
    return my_list

print(func(3, 5))