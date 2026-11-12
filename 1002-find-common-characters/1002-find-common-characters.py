from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cnt = Counter(words[0])
        ans = []
        for i in range(1, len(words)):
            cnt2 = Counter(words[i])
            for w in cnt:
                cnt[w] = min(cnt[w], cnt2[w])
        for w in cnt:
            for _ in range(cnt[w]):
                ans.append(w)
        return ans
        