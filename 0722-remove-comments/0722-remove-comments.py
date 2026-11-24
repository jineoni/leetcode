class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        ans = []
        cmt = False
        line = ""
        for i in range(len(source)):
            pt = 0
            n = len(source[i])
            while pt < n:
                if not cmt and pt < n-1 and source[i][pt:pt+2]=="/*":
                    cmt = True
                    pt += 2
                elif not cmt and pt < n-1 and source[i][pt:pt+2]=="//":
                    break
                elif cmt and pt < n-1 and source[i][pt:pt+2]=="*/":
                    cmt = False
                    pt += 2
                else:
                    if not cmt:
                        line += source[i][pt]
                    pt += 1
            if not cmt and line:
                ans.append(line)
                line = ""
        return ans