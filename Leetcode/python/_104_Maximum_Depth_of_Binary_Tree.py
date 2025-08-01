# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS - Time = O(n) - Space = O(w)
    # w - width
    # We increment height and process nodes at each level before moving onto the next level
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque([root])
        height = 0
        while dq:
            height += 1
            for _ in range(len(dq)):
                i = dq.popleft()
                if i.left:
                    dq.append(i.left)
                if i.right:
                    dq.append(i.right)
        return height
