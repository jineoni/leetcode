class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums) # 4
        prefix = [1]
        for i in range(1, n):
            prefix.append(prefix[i-1]*nums[i-1])
        
        # print(prefix) # [1, 1, 2, 6]

        suffix = 1
        for i in range(n-1, 0, -1):
            suffix *= nums[i]
            prefix[i-1] = prefix[i-1] * suffix
        
        return prefix
        

# [1, 2, 6, 24]
# [24, 24, 12, 4]

# [1, 1, 2, 6]