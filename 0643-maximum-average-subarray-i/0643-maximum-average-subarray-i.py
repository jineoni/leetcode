class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        current = sum(nums[left:left+k])
        maximum = current
        while (left+k) < len(nums):
            current = current - nums[left] + nums[left+k]
            maximum = max(maximum, current)
            left += 1
        return maximum/k