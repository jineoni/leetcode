class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = dict()
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hashmap.keys():
                if lst[i] in hashmap.values():
                    return False
                hashmap[pattern[i]] = lst[i]
            else:
                if hashmap[pattern[i]] != lst[i]:
                    return False
        return True

        