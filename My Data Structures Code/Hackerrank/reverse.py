arr = [1,3,4,5]
arr2 = []
for i in range(len(arr)-1, -1, -1):
    temp = arr[i]
    arr2.append(temp)

print(arr2)