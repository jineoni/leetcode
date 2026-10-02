class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pt, k = 0, 0
        while pt < len(nums) and isinstance(nums[pt], int):
            if nums[pt] == val:
                nums.pop(pt)
                nums.append("_")
            else:
                pt += 1
                k += 1
        return k