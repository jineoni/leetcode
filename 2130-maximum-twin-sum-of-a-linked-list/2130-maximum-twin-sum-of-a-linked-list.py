# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 중간 지점 찾기
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow 이후는 뒤집기
        prev = None
        curr = slow
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        
        # 이동하면서 최대 합 구하기
        max_sum = 0
        first = head
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum