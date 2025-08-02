from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS - Time = O(n) - Space = O(h)
    # Basically get max depth we can reach at each node (ground up to save time) and track max left depth + right depth
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter
