from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cnt = Counter(arr)
        return len(cnt.values()) == len(set(cnt.values()))
        