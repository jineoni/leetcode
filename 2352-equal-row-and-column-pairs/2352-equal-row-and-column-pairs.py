from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid2 = [[0] * len(grid) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                grid2[j][i] = grid[i][j]
        
        c1 = Counter(tuple(row) for row in grid)
        c2 = Counter(tuple(row) for row in grid2)

        ans = 0
        for k in c1.keys():
            if k in c2.keys():
                ans += (c1[k] * c2[k])
        return ans
