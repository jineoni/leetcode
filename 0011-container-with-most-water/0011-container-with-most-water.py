class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        left = 0
        right = len(height) - 1
        while left < right:
            most = max(most, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return most