class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                sumup = nums[i] + nums[left] + nums[right]
                if sumup > 0:
                    right -= 1
                elif sumup < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
        return [list(x) for x in set(tuple(x) for x in ans)]