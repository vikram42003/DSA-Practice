from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Tree -
#        1
#       / \
#      2   3
#     / \
#    4   5


def bfs(node):
    if not root:
        return

    dq = deque([node])

    while dq:
        curr = dq.popleft()
        print(curr.val, end=" ")
        if curr.left:
            dq.append(curr.left)
        if curr.right:
            dq.append(curr.right)

bfs(root)