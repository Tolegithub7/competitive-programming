# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if n == length:
            return head.next
        prev = None
        cur = head
        for i in range(length-n):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return head