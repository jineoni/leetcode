class Solution:
    def merge(self, left, right):
        result = []
        ptLeft = ptRight = 0
        while ptLeft < len(left) and ptRight < len(right):
            if left[ptLeft] < right[ptRight]:
                result.append(left[ptLeft])
                ptLeft += 1
            else:
                result.append(right[ptRight])
                ptRight += 1
        
        if ptLeft < len(left):
            result += left[ptLeft:]
        if ptRight < len(right):
            result += right[ptRight:]
        return result

    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sortedLeft = self.sortArray(left)
        sortedRight = self.sortArray(right)

        return self.merge(sortedLeft, sortedRight)

        