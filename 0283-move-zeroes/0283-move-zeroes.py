class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pt = 0
        cnt = 0
        for _ in range(len(nums)):
            if nums[pt] == 0:
                nums.pop(pt)
                cnt += 1
            else:
                pt += 1
        for _ in range(cnt):
            nums.append(0)
        return nums