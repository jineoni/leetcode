class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        time = []
        for p, s in cars:
            time.append((target-p)/s)
        curr = time.pop(0)
        fleet = 1
        while time:
            if curr < time[0]:
                fleet += 1
            curr = max(curr, time.pop(0))
        return fleet

# [1, 1, 7, 3, 12]

# [5, 8/3, 6]