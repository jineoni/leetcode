from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        return sorted(cnt, key=cnt.get, reverse=True)[:k]