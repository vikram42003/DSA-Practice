from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS - Time = O(n) - Space = O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        dq = deque([root])
        while dq:
            curr = dq.popleft()
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
            curr.left, curr.right = curr.right, curr.left
        return root
