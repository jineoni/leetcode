class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            elif not stack:
                return False
            elif (c == ")" and stack[-1] == "(") or (c == "}" and stack[-1] == "{") or (c == "]" and stack[-1] == "["):
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True