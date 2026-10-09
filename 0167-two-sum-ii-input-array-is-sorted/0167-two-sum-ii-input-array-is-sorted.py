class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            addup = numbers[left] + numbers[right]
            if addup > target:
                right -= 1
            elif addup < target:
                left += 1
            else:
                return [left+1, right+1]