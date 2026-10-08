class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        end = len(nums)-1
        while curr < end:
            if nums[curr] == 0:
                nums.pop(curr)
                nums.append(0)
                end -= 1
            else:
                curr += 1