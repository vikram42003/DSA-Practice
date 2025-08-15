from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # inorder and serialize - Time = O(n) - Space = O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        serialized = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            serialized.append(node.val)
            inorder(node.right)

        inorder(root)
        return serialized[k - 1]
