num = int(input())

arr = []
for i in range(num):
    n = int(input())
    arr.append(n)

x = int(input())

# print(arr)
# print(x)
# print(num)

# n= 7
# arr = [15, 4, 11, 40, 4, 4, 9]
# x = 15

def lastIndex(arr, x, n):
    if( n == -1):
        return -1
    if(x == arr[n]):
        return n
    else:
        currIndex = lastIndex(arr, x, n-1)
        return currIndex


val = lastIndex(arr, x, num-1)
print(val)