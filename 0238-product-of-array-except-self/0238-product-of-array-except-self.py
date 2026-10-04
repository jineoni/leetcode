class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1]
        for i in range(1, len(nums)+1):
            prefix.append(prefix[i-1]*nums[i-1])
            suffix.insert(0, suffix[0]*nums[len(nums)-i])
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i+1])
        return ans
        

# [1, 2, 6, 24]
# [24, 24, 12, 4]