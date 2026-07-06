from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cumsum = list(accumulate(gain))
        cumsum.insert(0, 0)
        return max(cumsum)