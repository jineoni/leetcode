class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        pt = n
        for i in range(n-1, -1, -1):
            if nums[i] < nums[i+1]:
                pt = i
                break
        # print(pt)
        if pt == n:
            return nums.sort()
        pt2 = n
        for i in range(n, pt, -1):
            if nums[i] > nums[pt]:
                pt2 = i
                break
        nums[pt], nums[pt2] = nums[pt2], nums[pt]
        nums[pt+1:] = sorted(nums[pt+1:])
        return nums
