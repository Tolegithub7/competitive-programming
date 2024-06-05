class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

class Solution:
    def maxAncestorDiff(self, root):
        return self.dfs(root)[2]

    def dfs(self, root):
        if not root:
            return float('inf'), float('-inf'), 0

        left_min, left_max, left_diff = self.dfs(root.left)
        right_min, right_max, right_diff = self.dfs(root.right)

        min_val = min(root.val, left_min, right_min)
        max_val = max(root.val, left_max, right_max)
        max_diff = max(left_diff, right_diff, abs(max_val - root.val), abs(min_val - root.val))

        return min_val, max_val, max_diff

