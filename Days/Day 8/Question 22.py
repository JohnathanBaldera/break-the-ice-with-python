words = input().split()

each_word = sorted(set(words))

for i in each_word:
    print("{0} : {1}".format(i, words.count(i)))