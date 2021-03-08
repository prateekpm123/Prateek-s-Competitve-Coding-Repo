# to find the reverse of the string or array

arr = [4, 2,1,3,6, 8, 9, 10, 11, 12,13,14]
# arr = 'hello there'
# arr = []
# num = int(input("Enter the number of elements you want in an array "))
# for i in range(num):
#     val = input()
#     arr.append(val)
start = 0
# if(len(arr)%==0):

for i in range(len(arr)-1, int((len(arr)/2)-1), -1):
    print(start)
    firstval = arr[start]
    secondval = arr[i]
    print(start,i, firstval, secondval)
    # temp = firstval
    # firstval = secondval
    # secondval = temp
    # arr.insert(start, secondval)
    arr[start] = secondval
    # arr.insert(i, firstval)
    arr[i] = firstval

    start+=1

# arr.insert(0, 234)
# arr[0] = 23423

print(arr)