class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        maxSum = sum(nums[:k])
        currSum = sum(nums[:k])
        for i in range(len(nums)-k):
            currSum = currSum-nums[i]+nums[i+k]
            maxSum = max(maxSum, currSum)
        return maxSum/k

