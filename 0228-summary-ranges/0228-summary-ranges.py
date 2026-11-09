class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        if not nums:
            return ans
            
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if start != nums[i-1]:
                    ans.append(str(start) + "->" + str(nums[i-1]))
                    start = nums[i]
                else:
                    ans.append(str(start))
                    start = nums[i]
        if start != nums[-1]:
            ans.append(str(start) + "->" + str(nums[-1]))
        else:
            ans.append(str(start))
        return ans



        