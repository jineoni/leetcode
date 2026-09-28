from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())


            

        