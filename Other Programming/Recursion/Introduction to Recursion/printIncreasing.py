num = int(input())

def Increasing(num):
    if(num ==0):
        return
    Increasing(num-1)
    print(num)

Increasing(num)


Increasing(num)