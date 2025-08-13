# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS and keep track of max - Time = O(n) - Space = O(n)
    # Just iterate over it in dfs and keep track of the max value of all parents/ancestors of this node, if node.val >= then we can add, otherwise continue dfs
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, max_till_now):
            if not node:
                return

            if node.val >= max_till_now:
                nonlocal good
                good += 1
                max_till_now = node.val

            dfs(node.left, max_till_now)
            dfs(node.right, max_till_now)

        dfs(root, float("-inf"))

        return good
