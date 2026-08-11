class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = [False] * len(rooms)
        visited[0] = True

        while stack:
            curr = stack.pop()
            for i in rooms[curr]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        
        if sum(visited) == len(rooms):
            return True
        return False