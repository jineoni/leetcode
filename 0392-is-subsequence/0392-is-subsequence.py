class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spt = 0
        tpt = 0
        while spt < len(s):
            if tpt >= len(t): return False
            if s[spt] == t[tpt]:
                spt += 1
            tpt += 1
        
        return True