num = int(input())
power = int(input())
# num = 2
# powerNum = 0

def power(num, powerNum):
    if(powerNum ==0):
        return 1
    elif(num == 0):
        return 1
    else:
        if(powerNum == 1):
            return num
        val = num*power(num, powerNum-1)
        return val

ansIs= power(num, powerNum)
print(ansIs)