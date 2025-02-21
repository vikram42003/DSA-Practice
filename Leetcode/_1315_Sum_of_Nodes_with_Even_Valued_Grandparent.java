// link - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class _1315_Sum_of_Nodes_with_Even_Valued_Grandparent {

    // BFS solution - Time = O(n) - Space = O(1)
    // really slow, the bfs can be further optimized
    public int sumEvenGrandparent(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        int total = 0;
        while (!q.isEmpty()) {
            // we can optimize this i think
            TreeNode curr = q.poll();
            if ((curr.val & 1) == 0) {
                total += getGrandChildren(curr);
            }

            if (curr.left != null)
                q.add(curr.left);
            if (curr.right != null)
                q.add(curr.right);
        }

        return total;
    }

    public int getGrandChildren(TreeNode curr) {
        TreeNode leftChild = curr.left;
        TreeNode rightChild = curr.right;

        int total = 0;

        if (leftChild != null) {
            if (leftChild.left != null) {
                total += leftChild.left.val;
            }
            if (leftChild.right != null) {
                total += leftChild.right.val;
            }
        }

        if (rightChild != null) {
            if (rightChild.left != null) {
                total += rightChild.left.val;
            }
            if (rightChild.right != null) {
                total += rightChild.right.val;
            }
        }

        return total;
    }
}
