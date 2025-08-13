from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Inorder (DFS) - Time = O(n) - Space = O(n)
    # For it to be a binary tree, the inorder MUST be non-increasing/non-decreasing(or ascending/descending, depends on type of bst).
    # Checking for node.left < node.val < node.right for each node is not enough
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        prev = float("-inf")

        def inorder(node):
            nonlocal ans, prev
            if not node or ans == False:
                return

            inorder(node.left)
            if prev >= node.val:
                ans = False
            else:
                prev = node.val
            inorder(node.right)

        inorder(root)
        return ans
