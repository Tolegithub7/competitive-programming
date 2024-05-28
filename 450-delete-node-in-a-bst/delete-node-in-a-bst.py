# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.minValue(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root

    def minValue(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        current = node
        while current.left:
            current = current.left
        return current