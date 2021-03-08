
nums = [2,3,4,5,6,7,11,15]
target = 9
ans = []
nums.sort()
i = 0
j = len(nums)-1
temp = []
while i < j:
    if(nums[i]+nums[j] == target):
        temp = [i, j]
        ans.append(temp)
        i += 1
        j += 1
    elif(nums[j]>target):
        j -= 1

print(ans)