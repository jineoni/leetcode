from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lcumsum = list(accumulate(nums))
        rcumsum = list(accumulate(nums[::-1]))[::-1]
        for i in range(len(nums)):
            if lcumsum[i] == rcumsum[i]:
                return i
        return -1