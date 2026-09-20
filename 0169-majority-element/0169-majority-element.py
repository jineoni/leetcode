from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_cnt = Counter(nums)
        return nums_cnt.most_common(1)[0][0]
        