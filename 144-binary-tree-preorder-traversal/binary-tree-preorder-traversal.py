# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
            return
        preorder(root)
        return ans
  
        # # ans = []
        # # def traverse(node):
        # #     if not node:
        # #         return
        # #     ans.append(node.val)
        # #     traverse(node.left)
        # #     traverse(node.right)
        # #     return
        # # traverse(root)
        # # return ans

        # #Iteration
        # cur, stack = root, []
        # res = []
        # while cur or stack:
        #     if cur:
        #         res.append(cur.val)
        #         stack.append(cur.right)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop()
        # return res
