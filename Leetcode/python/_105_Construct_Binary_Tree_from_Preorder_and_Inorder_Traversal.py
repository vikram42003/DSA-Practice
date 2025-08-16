from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS style tree building - Time = O(n^2) - Space = O(n)
    # inorder will tell us the order of occurence of elements from left to right
    # preorder will tell us current.val, then all the elements in the left subtree, then all the elements in the right subtree (through recursion)
    # With that info we can just take preorder[0] as current val, find it in preorder, now the umber of values before it will belong to
    # the left subtree, and values after it will belong to the right subtree
    # So now we can just extract the left subtree relevant portion of preorder and inorder and run buildTree on that recursively (do the same for right subtree) 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
