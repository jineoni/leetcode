class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        currRow = 0
        direction = 1
        n = len(s)

        if numRows == 1:
            return s

        for i in range(n):
            rows[currRow] += s[i]
            if currRow == numRows-1:
                direction = -1
            elif currRow == 0:
                direction = 1
            currRow += direction

        return "".join(rows)
