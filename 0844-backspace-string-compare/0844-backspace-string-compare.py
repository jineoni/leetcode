class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        for c in s:
            if c != "#": stackS.append(c)
            elif stackS: stackS.pop()
        for c in t:
            if c != "#": stackT.append(c)
            elif stackT: stackT.pop()
        return stackS == stackT