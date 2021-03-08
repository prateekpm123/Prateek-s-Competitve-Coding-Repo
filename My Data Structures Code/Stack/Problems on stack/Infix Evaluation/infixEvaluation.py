array = "(2+((6*4)/8)-3)"
stack = []
additionStack = []

def calculate(additionStack):
    print('this is the addition stack',additionStack)
    num1 = int(additionStack[2])
    num2 = int(additionStack[0])
    print(num1, ',' ,num2)
    val = additionStack[len(additionStack)-1]
    i= len(additionStack)-1
    while( i !=0):
        if(additionStack[1]== "*"):
            i -= 1
            print("i is ",i)
            val *= int(array[i])
        elif(additionStack[1]== "+"):
            i -= 1
            print("i is ",i)
            val += int(array[i])
        elif(additionStack[1]== "-"):
            i -= 1
            print("i is ",i)
            val -= int(array[i])
        elif(additionStack[1]== "/"):
            i -= 1
            print("i is ",i)
            val /= float(array[i])
        i -=1
    return val

for i in range(len(array)):
    if(array[i] == ')'):
        while(stack[len(stack)-1] != '('):
            additionStack.append(stack[len(stack)-1])
            stack.pop()
        stack.pop()
        val = calculate(additionStack)
        stack.append(val)
        print("New stack value is ", stack)
        additionStack = []
    else:
        stack.append(array[i])
