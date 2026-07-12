# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        current = head
        middle = n//2
        for _ in range(middle-1):
            current = current.next
        current.next = current.next.next

        return head
