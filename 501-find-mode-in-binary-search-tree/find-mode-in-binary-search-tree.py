# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        count = {}
        def checkDup(root):
            if root.val not in count:
                count[root.val] = 1
            else:
                count[root.val] += 1
            if not root.left and not root.right:
                return 
            if root.left:
                checkDup(root.left)
            if root.right:
                checkDup(root.right)
        checkDup(root)
        res = []
        mx = max(count.values())
        for key, value in count.items():
            if value == mx:
                res.append(key)
        return res
        