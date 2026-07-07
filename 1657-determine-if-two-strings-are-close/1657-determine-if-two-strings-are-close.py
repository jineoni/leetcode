from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        if sorted(count1.keys()) != sorted(count2.keys()):
            return False
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        return True