class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j+1
                n = len(nums)-1
                while k < n:
                    total = nums[i]+nums[j]+nums[k]+nums[n]
                    if total == target:
                        lst = [nums[i], nums[j], nums[k], nums[n]]
                        if lst not in ans:
                            ans.append(lst)
                        k += 1
                        n -= 1
                    elif total < target:
                        k += 1
                    else:
                        n -= 1
        return ans