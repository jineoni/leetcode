class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            elif mapping[s[i]] != t[i]:
                return False
        return True