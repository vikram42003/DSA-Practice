from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # DFS with idx precompute - Time = O(n) - Space = O(n)
    # We map inorder to idx to quickly compute the number of values that come before/after root and iterate in DFS
    # start and end control the size of elements that belong in left/right subtree
    # elements from start to mid - 1 belog to left subtree, mid + 1 to end for right subtree
    # if start == end, then that node is a leaf node and will be added as such
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        inorder_to_idx = {val: idx for idx, val in enumerate(inorder)}

        def build(start, end):
            if start > end:
                return None

            nonlocal preIdx
            root = TreeNode(preorder[preIdx])
            mid = inorder_to_idx[preorder[preIdx]]
            preIdx += 1

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)

    # DFS style tree building - Time = O(n^2) - Space = O(n)
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
