num = int(input("Enter the num"))
# num = 5
def printRecursion(num):
    if( num == -100):
        return
    print(num)
    print(printRecursion(num-1))

printRecursion(num)