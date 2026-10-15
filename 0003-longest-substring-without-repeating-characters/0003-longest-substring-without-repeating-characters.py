class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        longestLen = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longestLen = max(longestLen, len(substring))
        
        # for c in s:
        #     if c in substring:
        #         substring = set(c)
        #     else:
        #         substring.add(c)
        #     longestLen = max(len(substring), longestLen)
        
        return longestLen
        