class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i = 0
        M = []
        for j in range(len(nums)):
            if nums[j] == 1:
                i += 1
            else:
                M.append(i)
                i = 0
        M.append(i)
        return max(M)