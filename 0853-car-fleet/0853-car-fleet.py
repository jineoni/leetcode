class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        time = []
        for p, s in cars:
            time.append((target-p)/s)

        curr = time[0]
        fleet = 1
        for t in time[1:]:
            if curr < t:
                fleet += 1
                curr = t
        return fleet

# [1, 1, 7, 3, 12]

# [5, 8/3, 6]