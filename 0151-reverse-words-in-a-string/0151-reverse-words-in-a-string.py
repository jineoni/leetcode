class Solution:
    def reverseWords(self, s: str) -> str:
        words = [x for x in s.strip().split(" ") if x]
        return " ".join(words[::-1])