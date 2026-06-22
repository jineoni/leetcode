class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        return False