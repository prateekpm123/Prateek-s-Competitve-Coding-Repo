# In this problem we are finding an element X, from an Array

# n = int(input())
# arr = []
# for i in range(n):
#     num = int(input())
#     arr.append(num)
# x = int(input())    

num= 6
arr = [15, 4, 11, 40,  4, 9]
x = 4

def searchIndex(arr, x, n):
    if(num == n):
        return -1

    if(x == arr[n]):
        return n
    else:
        currIndex = searchIndex(arr, x, n+1)
        return currIndex


val = searchIndex(arr, x, 0)
print(val)

