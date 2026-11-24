from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        ans = []
        for key, value in cnt.items():
            if value == 2:
                ans.append(key)
        return ans
        