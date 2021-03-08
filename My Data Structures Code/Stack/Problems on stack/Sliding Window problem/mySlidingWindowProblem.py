# array = [2,9,3,8,1,7,12,6,14,4]
# k=4

array = []
n = int(input())
for i in range(n):
    num = int(input())
    array.append(num)
k = int(input())

stack = []
output = [] 
count = 0
val = 0
setter = 0
for i in range(len(array)):
    if(i < k):
        stack.append(array[i])
        if(i==k-1):
            # print('stack in the first time ',stack) 
            val = max(stack)
            output.append(val)
            setter = 1
    elif( i>=k):
        del stack[0]
        stack.append(array[i])
        val = max(stack)
        output.append(val)
        # print("stack new ",stack)
    if(setter == 1):
        print(val)

# for j in output:
#     print(j)

# print(stack)
# print(output)