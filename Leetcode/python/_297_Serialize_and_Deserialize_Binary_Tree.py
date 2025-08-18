# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Unoptimized but does the job - Time = O(n^2) - Space = O(n)
    # Strings are immuatable in python so rebuilding strings (and parsing) makes it pretty slow
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "(N)"
        return f"({root.val},{self.serialize(root.left)},{self.serialize(root.right)})"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "(N)":
            return None
        # data will be something like (1,(2,(N),(N)),(3,(N),(N))) for
        #      1
        #    2   3
        # So strip away rightmost and leftmost brackets and then parse it
        val, left_part, right_part = self.parse(data[1:-1])

        root = TreeNode(val)
        root.left = self.deserialize(left_part)
        root.right = self.deserialize(right_part)

        return root

    def parse(self, data):
        # data will look like this 1,(2,(N),(N)),(3,(N),(N))
        val = ""
        i = 0

        while data[i] != ",":
            val += data[i]
            i += 1

        i += 2
        left_part = "("
        counter = 0
        # One extra closing bracket ")" means we've reached the end of that part
        while counter >= 0:
            left_part += data[i]
            if data[i] == "(":
                counter += 1
            elif data[i] == ")":
                counter -= 1
            i += 1

        i += 2
        right_part = "("
        counter = 0
        while counter >= 0:
            right_part += data[i]
            if data[i] == "(":
                counter += 1
            elif data[i] == ")":
                counter -= 1
            i += 1

        return int(val), left_part, right_part


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
