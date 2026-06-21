class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        s = list(s)
        s_vowels = []

        for i in range(len(s)):
            if s[i].lower() in vowels:
                s_vowels.append(i)

        for j in range((len(s_vowels)+1)//2):
            s[s_vowels[j]], s[s_vowels[-j-1]] = s[s_vowels[-j-1]], s[s_vowels[j]]
        
        return "".join(s)
