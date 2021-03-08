# n = int(input())
# arr = []
# for i in range(n):
#     num = int(input())
#     arr.append(num)

n = 5
arr = [4,3,6,1,5]

def displayArr(n, arr):
    if(n==-1):
        return
    else:
        print(arr[n])

        displayArr(n-1,arr)

displayArr(n-1,arr)