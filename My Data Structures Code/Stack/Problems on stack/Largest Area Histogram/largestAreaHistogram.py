# array = [6,5,1,6,7,1,1,0]`
array = [2,5,8,5,2,8,2,8,5,4,6]

# array= []
# n= int(input())
# for i in range(n):
#     num = int(input())
#     array.append(num)


def removeDuplicates(x):
  return list(dict.fromkeys(x))

values = removeDuplicates(array)
# values = array
stack = []
possibilities = []
for i in range(len(values)):
    curnum= values[i]
    print("curnum is ", curnum)
    stack = []
    groups = []
    for j in range(len(array)):
        if(curnum <= array[j]):
            stack.append(array[j])
            area = len(stack)*curnum
            groups.append(area)
        else:
            if( stack.count(curnum) == 0):
                while(len(stack) !=0):
                    stack.pop()  
            else:
                if(stack.count(curnum) !=0):
                    area = len(stack)*curnum
                    groups.append(area)
                    stack = []
                    continue
                else:
                    stack = []
                    continue
        print("groups formed are", groups)
        print("stack is ", stack)
    if(len(groups) !=0):
        maxAreaOfGroup = max(groups)
        # area = len(stack)*curnum
        possibilities.append(maxAreaOfGroup)
    

print(possibilities)

print(max(possibilities))