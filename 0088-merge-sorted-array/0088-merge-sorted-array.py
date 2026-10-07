class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt = 0
        for i in range(n):
            while pt < m+i and nums1[pt] <= nums2[i]:
                pt += 1
            nums1.insert(pt, nums2[i])
            pt += 1
        nums1[:] = nums1[:m+n]