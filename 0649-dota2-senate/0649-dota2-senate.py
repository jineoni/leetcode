from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            r0 = r.popleft()
            d0 = d.popleft()
            if r0 < d0:
                r0 += len(senate)
                r.append(r0)
            else:
                d0 += len(senate)
                d.append(d0)
        
        if r: 
            return "Radiant"
        else: 
            return "Dire"