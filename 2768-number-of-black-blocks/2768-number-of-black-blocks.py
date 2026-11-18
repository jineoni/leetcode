from collections import defaultdict

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        ans = [0] * 5
        blocks = defaultdict(int)

        for r, c in coordinates:
            for dr in [0, -1]:
                for dc in [0, -1]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m-1 and 0 <= nc < n-1:
                        blocks[(nr, nc)] += 1
        
        for count in blocks.values():
            ans[count] += 1
        
        ans[0] = (m-1)*(n-1)-len(blocks)

        return ans