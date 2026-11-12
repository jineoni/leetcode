import string
from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        result = ""
        while len(result) < len(s):
            for c in string.ascii_lowercase:
                if cnt[c]:
                    cnt[c] -= 1
                    result += c
            for c in reversed(string.ascii_lowercase):
                if cnt[c]:
                    cnt[c] -= 1
                    result += c
        return result

        # result = ""
        # while s:
        #     minchar = min(s)
        #     result += minchar
        #     s = s.replace(minchar, '', 1)

        #     while True:
        #         lst = set([c for c in s if c > minchar])
        #         if not lst: break
        #         minchar = min(lst)
        #         result += minchar
        #         s = s.replace(minchar, '', 1)
            
        #     if not s: return result
        #     maxchar = max(s)
        #     result += maxchar
        #     s = s.replace(maxchar, '', 1)

        #     while True:
        #         lst = set([c for c in s if c < maxchar])
        #         if not lst: break
        #         maxchar = max(lst)
        #         result += maxchar
        #         s = s.replace(maxchar, '', 1)
            
        # return result


            # while result[-1] != min(s):
            #     minchar = min(s)
            #     result += minchar
            #     s = s.replace(minchar, '')
            #     if not s: return result
            # while result[-1] != max(s):
            #     maxchar = max(s)
            #     result += maxchar
            #     s = s.replace(maxchar, '')
            #     if not s: return result