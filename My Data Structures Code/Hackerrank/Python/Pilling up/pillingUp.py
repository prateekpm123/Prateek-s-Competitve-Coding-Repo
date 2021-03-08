from collections import deque
# num = int(input())

def properCube(d):
    cube = [999999999999999999999999999999999999]
    for i in range(len(d)):
        temp = []
        temp.append(d[0])
        temp.append(d[-1])
        print(temp)
        if(temp[0]>=temp[1]):
            if(temp[0]<=cube[-1]):
                d.popleft()
                cube.append(temp[0])
                print("cube from 1st temp",cube)
            else:
                return("No")
                
        else:
            if(temp[1]<=cube[-1]):
                d.pop()
                cube.append(temp[1])
                print("cube from 2nd temp",cube)
            else:
                return("No")
    return("Yes")


for i in range(int(input())):
    int(input())
    d = deque(map(int, input().split()))
    ans = properCube(d)
    print(ans)