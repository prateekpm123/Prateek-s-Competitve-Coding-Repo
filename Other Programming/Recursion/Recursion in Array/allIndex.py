n = int(input())

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

x = int(input())

# arr = [15, 4, 11,4,4,4, 40,  4, 9]
# n = len(arr) 
# x = 4
count = len(arr)
array = []

def allIndex(arr, x, n):
    if(count == n):
        return array

    allIndex(arr, x, n+1)
    if(arr[n] == x):
        array.append(n)
        return array
    else:
        return array

val = allIndex(arr, x, 0)
# print(val)

for i in range(len(val)-1,-1,-1):
    print(val[i])