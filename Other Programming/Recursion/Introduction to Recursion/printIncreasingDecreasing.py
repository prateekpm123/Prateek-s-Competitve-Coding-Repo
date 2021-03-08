# num = int(input())
num = 5
actual = num

def IncreasingDecreasing(num):
    if(num == 0):
        return
    print(num)
    IncreasingDecreasing(num-1)
    print(num)
    

IncreasingDecreasing(num)