from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS - Time = O(n) - Space = O(w)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        dq1 = deque([p])
        dq2 = deque([q])

        while dq1 and dq2:
            cur1 = dq1.popleft()
            cur2 = dq2.popleft()

            if cur1.val != cur2.val:
                return False

            if cur1.left and cur2.left:
                dq1.append(cur1.left)
                dq2.append(cur2.left)
            elif (cur1.left and not cur2.left) or (not cur1.left and cur2.left):
                return False

            if cur1.right and cur2.right:
                dq1.append(cur1.right)
                dq2.append(cur2.right)
            elif (cur1.right and not cur2.right) or (not cur1.right and cur2.right):
                return False

        return True

    # DFS - Time = O(n) - Space = O(h)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
