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

# Inorder - Strictly left to right no matter the depth
def dfs_inorder(node):
    if not node:
        return

    dfs_inorder(node.left)
    print(node.val, end=" ")
    dfs_inorder(node.right)


def dfs_inorder_iterative(node):
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right


# Preorder - Top left to bottom right, print root first
def dfs_preorder(node):
    if not node:
        return

    print(node.val, end=" ")
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_preorder_iterative(node):
    if not node:
        return

    stack = [node]

    while stack:
        curr = stack.pop()
        print(curr.val, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


# Postorder - Bottom-up left to right
def dfs_postorder(node):
    if not node:
        return

    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.val, end=" ")


def dfs_postorder_iterative(node):
    if not node:
        return
    
    stack1 = [node]
    stack2 = []
    
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    
    while stack2:
        curr = stack2.pop()
        print(curr.val, end=" ")


dfs_inorder(root)
print()
dfs_preorder(root)
print()
dfs_postorder(root)
print()

print()

dfs_inorder_iterative(root)
print()
dfs_preorder_iterative(root)
print()
dfs_postorder_iterative(root)
print()
