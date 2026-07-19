# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        len = 1
        tail = head
        while tail.next:
            tail = tail.next
            len += 1

        odd = head
        even = head.next

        if len <= 2:
            return head
        if len == 3:
            odd.next = odd.next.next
            odd = odd.next
            odd.next = even
            even.next = None
            return head

        cnt = 1
        while cnt < len:
            odd.next = odd.next.next
            odd = odd.next
            next_even = even.next.next
            tail.next = even
            tail = tail.next
            tail.next = None
            even = next_even
            cnt += 2

        return head