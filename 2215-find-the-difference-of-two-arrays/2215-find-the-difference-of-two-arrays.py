class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        only1 = list(set(nums1) - set(nums2))
        only2 = list(set(nums2) - set(nums1))
        return only1, only2