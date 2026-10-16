from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        maxLength = 0
        maxFreq = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            maxFreq = max(maxFreq, cnt[s[right]])
            while (right-left+1) - maxFreq > k:
                cnt[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right-left+1)
        return maxLength


        # cnt = defaultdict(int)
        # left = 0
        # maxLength = 0
        # for right in range(len(s)):
        #     cnt[s[right]] += 1
        #     while sum(cnt.values()) - max(cnt.values()) > k:
        #         cnt[s[left]] -= 1
        #         left += 1
        #     maxLength = max(maxLength, sum(cnt.values()))
        # return maxLength
