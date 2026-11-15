class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        ans = 0
        sign = ""
        for i in range(len(s)):
            if i == 0 and (s[i] == "-" or s[i] == "+"):
                sign += s[i]
            elif s[i] in "0123456789":
                ans = ans * 10 + int(s[i])
            else:
                break
        if sign == "-":
            ans = 0 - ans
        if ans < -2**31:
            ans = -2**31
        elif ans > 2**31-1:
            ans = 2**31-1
        return ans