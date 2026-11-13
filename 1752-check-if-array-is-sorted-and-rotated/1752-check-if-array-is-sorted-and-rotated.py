class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                cnt += 1
        return cnt <= 1


        # for i in range(len(nums)): # 0, 1, 2, 3, 4
        #     left = i
        #     right = i+1
        #     cnt = 0
        #     for _ in range(len(nums)-1):
        #         if nums[left] <= nums[right]:
        #             cnt += 1
        #         if cnt == len(nums)-1:
        #             return True
        #         left += 1
        #         right += 1
        #         if left >= len(nums):
        #             left -= len(nums)
        #         if right >= len(nums):
        #             right -= len(nums)
        # return False
