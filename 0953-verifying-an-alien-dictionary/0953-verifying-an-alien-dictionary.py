class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank = {}
        for i, c in enumerate(order):
            rank[c] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                rank1 = rank[word1[j]]
                rank2 = rank[word2[j]]
                if rank1 < rank2:
                    break
                elif rank1 > rank2:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        
        return True