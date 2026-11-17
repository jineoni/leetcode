class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        t = 0
        n = len(commands)
        x, y = 0, 0
        maxdist = 0
        obstacles = set(map(tuple, obstacles))

        for i in range(n):
            if commands[i] == -1:
                t += 1
            elif commands[i] == -2:
                t -= 1
            else:
                t %= 4
                for _ in range(commands[i]):
                    nx = x + dx[t]
                    ny = y + dy[t]
                    if (nx, ny) in obstacles:
                        break
                    x = nx
                    y = ny
                maxdist = max(maxdist, x**2+y**2)
        return maxdist


