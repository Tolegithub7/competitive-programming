class Solution:
    def reverse_list(self, head):
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        head = prev
        
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_list(head)

        local_max = 0
        prev, current = None, head

        while current:
            local_max = max(local_max, current.val)

            if current.val < local_max:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                current = current.next
            else:
                prev, current = current, current.next
        
        return self.reverse_list(head)