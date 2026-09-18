class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ""

        shortest = min(strs, key=len)
        ans = ""
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if strs[j][i] != shortest[i]:
                    return ans
            ans += shortest[i]
        
        return ans