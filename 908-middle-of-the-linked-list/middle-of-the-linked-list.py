# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # array_new = []
        # length = 0
        # while (head is not None):
        #     array_new.append(head)
        #     head = head.next
        #     length += 1
        # return array_new[length//2]