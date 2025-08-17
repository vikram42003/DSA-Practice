from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Optimized - Time = O(n) - Space = O(n)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_max = float("-inf")
        
        def postorder(node):
            if not node:
                return 0

            # We do max with 0 to ignore the paths that give us negative values
            left = max(0, postorder(node.left))
            right = max(0, postorder(node.right))
            # Update the special case, where we take node as root
            self.max_max = max(self.max_max, node.val + left + right)
            
            # Now return whichever path would give us bigger sum, or node.val itself if both paths were <= 0 
            return node.val + max(left, right)

        postorder(root)
        return self.max_max
    
    # DFS type - Time = O(n) - Space = O(n)
    # We'll do a post-order traversal because we need to find the maxPathSum for left and right subtree before we do calculations
    # We need to find the max path, so there could be only 1 straight path in the left subtree and right subtree
    # And on each node of the subtrees, we have to add the max among the 3 choices, node.val itself, node.val + maxPathSum(left subtree)
    # or node.val + maxPathSum(right subtree)
    # Another Special case we need to consider is that the maxPath may not go through the root, it could go through any node, and thats what
    # max_max will track, it'll track the max if we were to take the current node as root
    max_max = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        left = self.doTheThing(root.left)
        right = self.doTheThing(root.right)
        return max(
            self.max_max,
            root.val,
            root.val + left,
            root.val + right,
            root.val + left + right,
        )

    def doTheThing(self, root):
        if not root:
            return 0

        left = self.doTheThing(root.left)
        right = self.doTheThing(root.right)
        cur_max = max(root.val, root.val + left, root.val + right)
        self.max_max = max(self.max_max, cur_max, root.val + left + right)
        return cur_max

        # [5,4,8,11,null,13,4,7,2,null,null,null,1]
        # [9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
        # [10,2,10,20,1,null,-25,null,null,3,4]
        # [1,-2,-3,1,3,-2,null,-1]
        # [0,1,2,3,4,5,6,7,8,9,10]
        
