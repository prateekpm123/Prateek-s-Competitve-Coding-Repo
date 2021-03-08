# array = [2,5,9,3,1,12,6,8,7]
array = [5,5,3,8,-2,7]
# array = []
# n = int(input())
# for i in range(n):
#     num = int(input())
#     array.append(num)
stack = []
stack.append(array[len(array)-1])
output = [-1]

for i in range(len(array)-2,-1,-1):
    print(array[i])
    if(stack[len(stack)-1] > array[i]):
        output.append(stack[len(stack)-1])
        stack.append(array[i])
        print("if stack top is greater than ", stack)
        print("output if stack top is greater ", output)
    elif(stack[len(stack)-1] < array[i]):
        # while(array[i] < stack[len(stack)-1]):
        for j in range(len(stack)):
            if(stack[len(stack)-1] < array[i]):
                stack.pop() 
            print("while poping length of stack is ",len(stack))
        if(len(stack)==0):
            output.append(-1)
        else:
            output.append(stack[len(stack)-1])
        stack.append(array[i])

        print("if stack top is less than array[i] ", stack)
        print("output if stack is less greater ", output)

print(output)
for i in range(len(output)-1,-1,-1):
    print(output[i])