class SomeClass:
    def __init__(self):
        pass

    def getString(self):
        get = input("Enter a string: ")
        return get

    def printString(self, someString):
        print(someString.upper())

##test

c1 = SomeClass()

c1.getString()

c1.printString("This should be upper case")