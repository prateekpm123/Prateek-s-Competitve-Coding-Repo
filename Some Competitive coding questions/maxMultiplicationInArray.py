arr = [ 0,10, 20, 3, 4, 3, 5, 23, 21]
firstFour = [arr[0], arr[1], arr[2], arr[3]]
stack = []

def calculate(firstFour):
    total = 1
    if(0 in firstFour == True):
        return 0
    else:
        for i in range(len(firstFour)):
            total *= firstFour[i]
        return total

for i in range(4,len(arr)):
    print(firstFour)
    total = calculate(firstFour)
    stack.append(total)
    print("the total is ", total)
    del firstFour[0]
    firstFour.append(arr[i])

stack.sort()
print(stack)
print("max value is ", stack[len(stack)-1])

# print(firstFour)