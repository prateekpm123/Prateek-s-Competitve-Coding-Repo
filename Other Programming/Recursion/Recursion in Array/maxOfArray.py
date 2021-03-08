n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

n= 5
arr = [12,53,231, 6733,23]

def maxOfArray(arr, n):
    if(n == len(arr)-1):
        return arr[n]

    misa = maxOfArray(arr,n+1)
    if(misa > arr[n]):      # Here we have kept arr[0] because, when stack reaches its base case, then stack would need to compare it self with the current value of n, and not the static value of arr[0]
        return misa
    else:
        return arr[n]


val = maxOfArray(arr, 0)
print(val)