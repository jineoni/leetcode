class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        zero_cnt = 0
        maximum = 0
        while left <= right < len(nums):
            if zero_cnt > k:
                zero_cnt -= (1 - nums[left])
                left += 1
            else:
                zero_cnt += (1 - nums[right])
                right += 1
                if zero_cnt <= k:
                    maximum = max(maximum, right - left)
        return maximum