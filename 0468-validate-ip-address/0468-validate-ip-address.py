class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        queryIPlst = queryIP.split(".")
        if len(queryIPlst) == 4:
            for x in queryIPlst:
                if not x.isdigit() or int(x) > 255 or (len(x) > 1 and x[0]=="0"):
                    return "Neither"
            return "IPv4"

        queryIPlst = queryIP.split(":")
        if len(queryIPlst) == 8:
            for x in queryIPlst:
                if len(x) > 4 or len(x) < 1:
                    return "Neither"
                for c in x:
                    if not c.isdigit() and c not in 'abcdefABCDEF':
                        return "Neither"
            return "IPv6"
        
        return "Neither"
        