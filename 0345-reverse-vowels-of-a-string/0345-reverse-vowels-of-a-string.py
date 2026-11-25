class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        lst = list(s)
        while left < right:
            if lst[left] in 'aeiouAEIOU':
                while lst[right] not in 'aeiouAEIOU':
                    right -=1
                lst[left], lst[right] = lst[right], lst[left]
                right -= 1
            left +=1
        return "".join(lst)