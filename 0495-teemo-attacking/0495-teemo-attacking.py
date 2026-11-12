class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ans = len(timeSeries) * duration
        for i in range(len(timeSeries)-1):
            interval = timeSeries[i+1] - timeSeries[i]
            if interval < duration:
                ans -= (duration-interval)
        return ans


        # s = set()
        # for t in timeSeries:
        #     for d in range(duration):
        #         s.add(t+d)
        # return len(s)