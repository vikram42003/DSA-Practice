// link - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

public class _2095_Delete_the_Middle_Node_of_a_Linked_List {
    public ListNode deleteMiddle(ListNode head) {
        // Edge case - there is only 1 node
        if (head.next == null)
            return null;

        ListNode slow = head;
        ListNode fast = head.next;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        slow.next = slow.next.next;

        return head;
    }
}
