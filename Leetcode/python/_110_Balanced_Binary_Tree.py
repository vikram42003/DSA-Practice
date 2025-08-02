from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS - Time = O(n) - Space = O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                nonlocal ans
                ans = False

            return 1 + max(left, right)

        dfs(root)
        return ans
