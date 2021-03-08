array = [2,5,5,9,3,1,12,6,8,7]
# n = int(input())
# array= []
# for k in range(n):
#     num = int(input())
#     array.append(num)

stack = []
outputArr = [1]

stack.append(array[0])
print(stack)
def peek(arr):
    length = len(arr)
    print("stack length is ", length)
    return arr[length-1]
count = 0

for i in range(1, len(array),1):
    count = 0
    print("stack len ", len(stack)," and array len ", len(array))
    for j in range(len(stack)-1,-1,-1):
        if(len(stack)>0 and len(array)>0 and stack[j]<=array[i]):
            # stack.pop()
            count +=1
        else:
            break
    # stack.append([])
    stack.append(array[i])
    print("array of i is ",array[i])
    # stack[i].append(count+1)
    print("stack is ", stack)
    outputArr.append(count+1)
    print("Output array is ",outputArr)
    print(count+1)


print(outputArr)
