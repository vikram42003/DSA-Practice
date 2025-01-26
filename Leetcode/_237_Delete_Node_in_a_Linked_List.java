// link - https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class _237_Delete_Node_in_a_Linked_List {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
