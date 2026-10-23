class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            elif stack and c == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and c == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True