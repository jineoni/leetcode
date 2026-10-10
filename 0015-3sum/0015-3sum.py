class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                sumup = nums[i] + nums[left] + nums[right]
                if sumup > 0 or (right < len(nums)-1 and nums[right] == nums[right+1]):
                    right -= 1
                elif sumup < 0 or (left > i+1 and nums[left] == nums[left-1]):
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
        return ans