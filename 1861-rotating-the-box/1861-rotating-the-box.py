class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for i in range(m):
            pt1, pt2 = n-2, n-1
            while pt1 >= 0:
                if boxGrid[i][pt2] == ".":
                    if pt1 >= 0 and boxGrid[i][pt1] == ".":
                        pt1 -= 1
                    elif boxGrid[i][pt1] == "#":
                        boxGrid[i][pt1], boxGrid[i][pt2] = boxGrid[i][pt2], boxGrid[i][pt1]
                        pt1 -= 1
                        pt2 -= 1
                    elif boxGrid[i][pt1] == "*":
                        pt2 = pt1
                        pt1 -= 1
                else:
                    pt2 -= 1
                    pt1 = pt2 - 1
        
        return [list(row) for row in zip(*boxGrid[::-1])]