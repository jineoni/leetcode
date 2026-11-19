class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [1, 0, -1, 0, 1, -1, 1, -1]
        dy = [0, 1, 0, -1, 1, -1, -1, 1]

        r = len(board)
        c = len(board[0])

        original = [row[:] for row in board]
        for x in range(r):
            for y in range(c):
                cnt = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        cnt += original[nx][ny]
                if original[x][y]:
                    if cnt < 2 or cnt > 3:
                        board[x][y] = 0
                if not original[x][y]:
                    if cnt == 3:
                        board[x][y] = 1