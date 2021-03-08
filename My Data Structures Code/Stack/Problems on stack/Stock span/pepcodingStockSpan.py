array = [2,5,5,9,3,1,12,6,8,7]
# n = int(input())
# array= []
# for k in range(n):
#     num = int(input())
#     array.append(num)

stack = []
outputArr = [1]

stack.append(array[0])

def StockSpan(array):
    for i in range(1,len(array),1):
        while(len(stack)>0 and array[i]>stack[len(stack)-1]):
            stack.pop()
        if( len(stack) == 0):
            outputArr.insert(i, i+1)
        else:
            outputArr.insert(i, i-stack[len(stack)-1])
        stack.append(i)

    return(outputArr)
    

def printOutput(array):
    for i in array:
        print(i)

ans = StockSpan(array)
printOutput(ans)