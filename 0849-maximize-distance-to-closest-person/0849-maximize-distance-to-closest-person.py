class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        indices = [i for i, value in enumerate(seats) if value == 1]
        dist = 0
        for i in range(len(indices)-1):
            dist = max(dist, (indices[i+1]-indices[i])//2)

        if not seats[0]:
            dist = max(dist, indices[0])
        if not seats[-1]:
            dist = max(dist, len(seats)-1-indices[-1])
        return dist
        

        