array = [7,4,8,2,3]
# array.sort()
array2 = [7,4,8,2,3]
# array2.sort()
k = 12
stack = []
count = 0

def stackSum(stack):
    summ = 0
    for i in stack:
        summ += i
    return summ


# def SumCheck(summ):
    
for i in range(len(array)):
    stack = []
    stack.append(array[i])
    val = [i]
    summ = array[i]
    indexOfRemoved = array2.index(array[i])
    array2.remove(array[i])
    for j in range(len(array2)):
         
        if( summ > k and len(stack) != 0):
            print("if summ is greater, stack is ", stack)
            print("if summ is greater than sum is ", summ)
            stack.pop()
            print("if summ is greater than k")
        elif( summ < k):
            # summ += array[j]
            stack.append(array2[j])
            summ = stackSum(stack)
            print("this is the array before pop ", stack)
            print("this is the sum ", summ)
            if(summ > k):
                stack.pop()
                summ = stackSum(stack)
                print("this is the array after pop ", stack)
                print("this is the sum if its less", summ)
            elif(summ ==k ):
                count += 1
            # # SumCheck(summ)
            # if(summ == k):
            #     count +=1

        # elif(summ == k):
        #     count +=1
        #     print("The sum is equal now",count)
    array2.insert(indexOfRemoved,array[i])
    
print("count is ", count)


