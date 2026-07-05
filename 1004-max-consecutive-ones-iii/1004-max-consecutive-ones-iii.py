class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, zero_cnt, maximum = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum