# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        sums = [0] * (length//2)
        curr = head
        for i in range(len(sums)):
            sums[i] += curr.val
            curr = curr.next
        for i in range(len(sums)-1, -1, -1):
            sums[i] += curr.val
            curr = curr.next
        return max(sums)