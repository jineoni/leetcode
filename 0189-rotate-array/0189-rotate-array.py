class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k >= n:
            k %= n
        subs1 = nums[:n-k]
        subs2 = nums[n-k:]
        nums[:] = subs2 + subs1