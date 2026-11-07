from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = 0
        for word in cnt1.keys():
            if cnt1[word] != 1:
                continue
            if cnt2[word] and cnt2[word] == 1 and cnt1[word] == 1:
                ans += 1
        return ans