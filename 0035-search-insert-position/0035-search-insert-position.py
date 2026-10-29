class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if nums[-1] < target:
            return right+1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        return left