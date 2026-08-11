class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = [False] * len(rooms)

        while stack:
            curr = stack.pop()
            visited[curr] = True
            for i in rooms[curr]:
                if not visited[i]:
                    stack.append(i)
        
        if sum(visited) == len(rooms):
            return True
        return False