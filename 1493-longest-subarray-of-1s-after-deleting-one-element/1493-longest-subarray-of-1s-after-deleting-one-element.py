class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        left = 0
        deleted = 0
        subarray = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1
            while deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1
            subarray = max(subarray, right - left)
        return subarray