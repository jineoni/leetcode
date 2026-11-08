class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        return [candy >= maximum-extraCandies for candy in candies]
        