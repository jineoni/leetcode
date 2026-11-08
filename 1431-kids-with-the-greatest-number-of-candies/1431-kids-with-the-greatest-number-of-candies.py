class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [candy >= max(candies)-extraCandies for candy in candies]
        