class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(len(nums)):
                if(i != j):
                    if(target == temp+nums[j]):
                        # print(temp, nums[j])
                        ans.append(i)
                        # print(ans)
                        ans.append(j)
                        # print(ans)
                        break
                        
        ans.pop()
        ans.pop()
        print(ans)
        