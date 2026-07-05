class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cnt = sum(c in vowels for c in s[:k])
        maximum = cnt
        for i in range(len(s)-k):
            if s[i] in vowels: cnt -= 1
            if s[i+k] in vowels: cnt += 1
            maximum = max(maximum, cnt)
        return maximum