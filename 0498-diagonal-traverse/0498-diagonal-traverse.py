class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n - 1)]
        for row in range(m):
            for col in range(n):
                diagonals[row+col].append(mat[row][col])
        
        output = []
        for i in range(m+n-1):
            if i%2 != 0:
                output.extend(diagonals[i])
            else:
                output.extend(reversed(diagonals[i]))

        return output