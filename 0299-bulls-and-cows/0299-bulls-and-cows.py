from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        
        count = sum((Counter(secret) & Counter(guess)).values())
        cows = count - bulls

        return f"{bulls}A{cows}B"
        