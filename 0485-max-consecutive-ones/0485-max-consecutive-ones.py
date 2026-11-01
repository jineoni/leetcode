class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr = 1
        cnt = 0
        maxCnt = 0
        for n in nums:
            if n == 1 and curr == 1:
                cnt += 1
            elif n == 1 and curr == 0:
                cnt = 1
            else:
                cnt = 0
            curr = n
            maxCnt = max(cnt, maxCnt)
        return maxCnt

        