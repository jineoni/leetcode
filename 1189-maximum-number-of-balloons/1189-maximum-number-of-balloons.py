from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        ans = 0
        while True:
            for c in "balloon":
                if not cnt[c]:
                    return ans
                cnt[c] -= 1
            ans += 1
