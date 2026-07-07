class Solution:
    def removeStars(self, s: str) -> str:
        temp = []
        for i in range(len(s)):
            if s[i] == '*':
                temp.pop()
            else:
                temp.append(s[i])
        return "".join(temp)