n = int(input())
# n = 3

def makePattern(n):
    if(n == 0):
        return
    # print('pre ', n)
    # makePattern(n-1)
    # print('in ', n)
    # makePattern(n-1)
    # print("post ", n)
    print(n, end=" ")
    makePattern(n-1)
    print(n, end=" ")
    makePattern(n-1)
    print(n, end=" ")

val = makePattern(n)
# print(val)