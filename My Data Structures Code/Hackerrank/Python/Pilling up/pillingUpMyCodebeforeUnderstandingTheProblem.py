# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
num = int(input())
values = []

for i in range(num*2):
    value = list(map(int, input().split()))
    values.append(value)

number = []
for i in range(0,len(values),2):
    temp = values[i][0]
    number.append(temp)
    # print(values[i+1])
    # values.pop(i)
    
dlist = []
for i in range(1,len(values),2):
    temp = values[i]
    d = deque(temp)
    dlist.append(d)
    
stack = []
tempstack = []
for i in range(len(dlist)):
    tempstack = []
    for j in range(len(dlist[i])):
        if(j%2==0):
            temp = dlist[i][0]
            dlist[i].popleft()
        else:
            temp = dlist[i][len(dlist[i])-1]
            dlist[i].pop()
            
        tempstack.append(temp)
    stack.append(tempstack)
    
counter = 0
for i in range(len(stack)):
    counter = 0
    for j in range(len(stack[i])-2):
        # print("first no is ",stack[i][j])
        # print("second no is ",stack[i][j+1])
        
        if(stack[i][j]>=stack[i][j+1]):
            counter +=1
        else:
            counter = 0
            break
        # print("counter is ",counter)
    # print("counter is ", counter)
    if(counter == 0):
        print("No")
    else:
        print("Yes")
    
# print(dlist)
# print(stack)
# print(values)
# print(number)
