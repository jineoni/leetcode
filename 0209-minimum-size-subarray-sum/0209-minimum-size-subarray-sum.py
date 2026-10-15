class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLength = float('inf')
        left, right = 0, 0
        subarray = nums[0]
        while right < len(nums):
            if subarray >= target:
                minLength = min(minLength, right-left+1)
                subarray -= nums[left]
                left += 1
            else:
                right += 1
                if not right == len(nums):
                    subarray += nums[right]
        if minLength == float('inf'):
            return 0
        return minLength
