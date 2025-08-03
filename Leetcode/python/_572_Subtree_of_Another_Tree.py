from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS - Time = O(n) - Space = O(h)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val and isSameTree(node, subRoot):
                nonlocal ans
                ans = True
                return

            dfs(node.left)
            dfs(node.right)

        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            else:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        dfs(root)

        return ans
