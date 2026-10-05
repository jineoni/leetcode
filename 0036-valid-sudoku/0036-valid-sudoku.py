class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                if board[i][j] in boxes[3*(i//3)+(j//3)]:
                    return False
                else:
                    boxes[3*(i//3)+(j//3)].add(board[i][j])

        return True

"""
00 01 02 03 04 05 06 07 08
10 11 12 13 14 15 16 17 18
20 21 22 23 24 25 26 27 28
30 31 32 33 34 35 36 37 38
"""