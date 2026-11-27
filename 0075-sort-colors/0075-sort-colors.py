from collections import Counter
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        pt = 0
        for i in range(3):
            for j in range(cnt[i]):
                nums[pt] = i
                pt += 1


        # def mergeSort(nums):
        #     if len(nums) == 1:
        #         return nums
            
        #     mid = len(nums)//2
        #     left = mergeSort(nums[:mid])
        #     right = mergeSort(nums[mid:])

        #     pt1, pt2 = 0, 0
        #     result = []
        #     while pt1 < len(left) and pt2 < len(right):
        #         if left[pt1] > right[pt2]:
        #             result.append(right[pt2])
        #             pt2 += 1
        #         else:
        #             result.append(left[pt1])
        #             pt1 += 1
        #     result.extend(left[pt1:])
        #     result.extend(right[pt2:])
        #     # while pt1 < len(left):
        #     #     result.append(left[pt1])
        #     #     pt1 += 1
        #     # while pt2 < len(right):
        #     #     result.append(right[pt2])
        #     #     pt2 += 1
        #     return result

        # nums[:] = mergeSort(nums)