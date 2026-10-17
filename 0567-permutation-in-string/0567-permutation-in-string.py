from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n])
        for left in range(len(s2)-n):
            if cnt1 == cnt2:
                return True
            cnt2[s2[left]] -= 1
            cnt2[s2[left+n]] += 1
        if cnt1 == cnt2:
            return True
        return False
