class Solution:
    def countUnguarded(
        self, m: int, n: int,
        guards: list[list[int]],
        walls: list[list[int]]
    ) -> int:
        # 0: 빈 칸, 1: 경비원, 2: 벽, 3: 감시되는 칸
        board = [[0] * n for _ in range(m)]

        for r, c in guards:
            board[r][c] = 1
        for r, c in walls:
            board[r][c] = 2

        # 각 행을 왼쪽→오른쪽, 오른쪽→왼쪽으로 확인
        for r in range(m):
            for cols in (range(n), range(n - 1, -1, -1)):
                seen_guard = False
                for c in cols:
                    if board[r][c] == 2:
                        seen_guard = False
                    elif board[r][c] == 1:
                        seen_guard = True
                    elif seen_guard:
                        board[r][c] = 3

        # 각 열을 위→아래, 아래→위로 확인
        for c in range(n):
            for rows in (range(m), range(m - 1, -1, -1)):
                seen_guard = False
                for r in rows:
                    if board[r][c] == 2:
                        seen_guard = False
                    elif board[r][c] == 1:
                        seen_guard = True
                    elif seen_guard:
                        board[r][c] = 3

        return sum(cell == 0 for row in board for cell in row)