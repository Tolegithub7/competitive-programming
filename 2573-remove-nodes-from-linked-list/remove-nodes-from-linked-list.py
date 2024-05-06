class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first reverse the list
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        curr = prev
        while curr:
            while curr.next and curr.val>curr.next.val:
                curr.next = curr.next.next
            curr=curr.next

        curr = prev
        prev = None
        while curr:
            next = curr.next
            curr.next=prev
            prev =curr
            curr = next
        return prev