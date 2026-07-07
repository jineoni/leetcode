class Solution:
    def removeStars(self, s: str) -> str:
        pt = 0
        while pt < len(s):
            if s[pt] == '*':
                s = s[:pt-1] + s[pt+1:]
                pt -= 1
            else:
                pt += 1
        return s