class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_length = 1
        for left in range(len(nums)):
            prod = 1
            GCD = 0
            LCM = 1
            for right in range(left, len(nums)):
                prod *= nums[right]
                GCD = gcd(GCD, nums[right])
                LCM = lcm(LCM, nums[right])
                if prod == GCD * LCM:
                    max_length = max(max_length, right-left+1)
        return max_length


        # left, right = 0, 1
        # max_length = 1
        # prod = nums[0]
        # GCD = nums[0]
        # LCM = nums[0]
        # while right < len(nums):
        #     prod *= nums[right]
        #     GCD = gcd(GCD, nums[right])
        #     LCM = lcm(LCM, nums[right])
        #     if prod == GCD*LCM:
        #         max_length = max(max_length, right-left)
        #         right += 1
        #     else:
        #         left += 1
        # return max_length
            