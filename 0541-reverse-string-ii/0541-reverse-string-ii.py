class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), 2*k):
            sub = s[i:i+k]
            ans += sub[::-1]
            ans += s[i+k:i+k+k]
        return ans