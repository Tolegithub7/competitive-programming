# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def maxdepth(node, depth):
        #     if not node:
        #         return depth
        #     left = maxdepth(node.left, depth + 1) 
        #     right = maxdepth(node.right, depth + 1)
        #     return max(left, right)
        # return maxdepth(root, 0)

        def maxep(node):
            if not node:
                return 0
            l = maxep(node.left)
            r = maxep(node.right)
            return max(l, r) + 1
        return maxep(root)
        
