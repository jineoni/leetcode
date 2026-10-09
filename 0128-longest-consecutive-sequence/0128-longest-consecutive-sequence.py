class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        maxLength = 0
        currLength = 1
        for num in nums:
            if num-1 in nums:
                continue
            curr = num
            while True:
                if curr+1 in nums:
                    curr += 1
                    currLength += 1
                else:
                    break
            maxLength = max(maxLength, currLength)
            currLength = 1
        return maxLength