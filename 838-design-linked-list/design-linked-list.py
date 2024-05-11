#Using Doubly linked_list
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node, next, prev = Node(val), self.left.next, self.left
        next.prev = new_node
        prev.next = new_node
        new_node.next = next
        new_node.prev = prev

    def addAtTail(self, val: int) -> None:
        new_node, next, prev = Node(val), self.right, self.right.prev
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node, next, prev = Node(val), cur, cur.prev
            next.prev = new_node
            prev.next = new_node
            new_node.next = next
            new_node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next 
        while cur and index>0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index==0:
            next, prev = cur.next, cur.prev
            prev.next = next
            next.prev = prev


# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MyLinkedList:
#     def __init__(self):
#         self.head = None

#     def get(self, index: int) -> int:
#         current = self.head
#         count = 0
#         while current is not None:
#             if count == index:
#                 return current.val
#             count += 1
#             current = current.next
#         return -1

#     def addAtHead(self, val: int) -> None:
#         self.head = Node(val, self.head)

#     def addAtTail(self, val: int) -> None:
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index == 0:
#             self.addAtHead(val)
#             return
#         current = self.head
#         count = 0
#         while current is not None:
#             if count == index - 1:
#                 new_node = Node(val, current.next)
#                 current.next = new_node
#                 return
#             count += 1
#             current = current.next

#     def deleteAtIndex(self, index: int) -> None:
#         if index == 0:
#             self.head = self.head.next
#             return
#         current = self.head
#         count = 0
#         while current is not None:
#             if count == index - 1 and current.next is not None:
#                 current.next = current.next.next
#                 return
#             count += 1
#             current = current.next

# Example usage
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1)) # Should return 2
# obj.deleteAtIndex(1)
# print(obj.get(1)) # Should return 3

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self.head = None

#     def get(self, index: int) -> int:
#         if index == 1:
#             return self.head
#         else: 
#             for i in range(1, index):
#                 if self.head.next:
#                     self.head = self.head.next
#                 else:
#                     return -1 
#         return self.head

#     def addAtHead(self, val: int) -> None:
#         new_node = Node(val)
#         new_node.next = self.head
#         self.head = new_node

#     def addAtTail(self, val: int) -> None:
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def addAtIndex(self, index: int, val: int) -> None:
#         cur = self.head
#         for i in range(index):
#             cur = cur.next
#         cur.next = val
#         # val.next = cur
#     def delete_node(self, key):
#         temp = self.head
#         if temp is not None:
#             if temp.data == key:
#                 self.head = temp.next
#                 temp = None
#                 return
#         while temp is not None:
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next
#         if temp == None:
#             return
#         prev.next = temp.next
#         temp = None
                
#         # cur = self.head
#         # for i in range(index):
#         #     cur = cur.next
#         # cur.next = val
#         # val.next = cur


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)