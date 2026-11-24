from itertools import accumulate
from collections import Counter

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        breaks = []
        for w in wall:
            breaks.extend(list(accumulate(w))[:-1])
        cnt = Counter(breaks)
        max_cnt = max(cnt.values(), default=0)
        # print(breaks)
        # print(cnt)
        return len(wall)-max_cnt