class MyGen:
    def by_seven(self, n):
        for i in range(int(n) + 1):
            if i % 7 == 0:
                yield n

gen = MyGen()

number = gen.by_seven(input("Input a number:"))
for i in number:
    print(number)
