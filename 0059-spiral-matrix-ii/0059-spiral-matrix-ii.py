class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        visited = [[0] * n for _ in range(n)]
        x, y = 0, 0
        visited[x][y] = 1

        i = 0
        pt = 1
        while pt < n**2:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = pt+1
                pt += 1
                x = nx
                y = ny
            else:
                i = (i+1)%4

        return visited