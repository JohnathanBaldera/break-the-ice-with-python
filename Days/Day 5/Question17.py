def checkBalance():
    balance = 0
    while True:
        transaction = input()
        if transaction == "":
            return balance
        elif transaction[0 : 2] == "D ":
            balance += int(transaction[2:])
        elif transaction[0 : 2] == "W ":
            balance -= int(transaction[2:])

print(checkBalance())