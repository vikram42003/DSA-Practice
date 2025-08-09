from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS (Extra Space) - Time = O(n) - Space = O(1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        buffer_tree = [root]
        res = [[root.val]]

        while buffer_tree:
            buffer_temp = []
            res_temp = []
            for node in buffer_tree:
                if node.left:
                    buffer_temp.append(node.left)
                    res_temp.append(node.left.val)
                if node.right:
                    buffer_temp.append(node.right)
                    res_temp.append(node.right.val)
            if len(buffer_temp) > 0:
                buffer_tree = buffer_temp
                res.append(res_temp)
            else:
                break

        return res
