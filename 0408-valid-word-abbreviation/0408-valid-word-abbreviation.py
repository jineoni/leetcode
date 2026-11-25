class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pt1, pt2 = 0, 0
        while pt1 < len(word) and pt2 < len(abbr):
            if abbr[pt2] == "0":
                return False
            elif abbr[pt2].isdigit():
                i = 0
                while pt2+i < len(abbr)-1 and abbr[pt2+i+1].isdigit():
                    i += 1
                pt1 += int(abbr[pt2:pt2+i+1])
                pt2 += i+1
            elif word[pt1] != abbr[pt2]:
                return False
            else:
                pt1 += 1
                pt2 += 1
        return (pt1 == len(word)) and (pt2 == len(abbr))
