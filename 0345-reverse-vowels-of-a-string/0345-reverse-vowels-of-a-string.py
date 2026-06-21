class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        s = list(s)
        
        right = len(s) - 1
        left = 0

        while left < right:
            if not s[left].lower() in vowels:
                left += 1
            elif not s[right].lower() in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return "".join(s)
