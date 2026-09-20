from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCnt = Counter(ransomNote)
        magazineCnt = Counter(magazine)

        for k, v in ransomCnt.items():
            if v > magazineCnt[k]:
                return False
        
        return True