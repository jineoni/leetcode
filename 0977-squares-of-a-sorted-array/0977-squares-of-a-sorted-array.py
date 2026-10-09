class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        ans = [0] * len(nums)
        pos = len(nums)-1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans[pos] = nums[right]**2
                pos -= 1
                right -= 1
            else:
                ans[pos] = nums[left]**2
                pos -=1
                left += 1
        return ans