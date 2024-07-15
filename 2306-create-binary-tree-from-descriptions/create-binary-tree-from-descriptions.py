# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        children = set()
        for parent, child, isLeft in descriptions:
            parentNode = nodes.setdefault(parent, TreeNode(val=parent))
            childNode = nodes.setdefault(child, TreeNode(val=child))
            children.add(child)
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        for node in nodes:
            if node not in children:
                return nodes[node]