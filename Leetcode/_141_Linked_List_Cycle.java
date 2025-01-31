// link - https://leetcode.com/problems/linked-list-cycle/

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class _141_Linked_List_Cycle {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;

        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            head = head.next;
            fast = fast.next.next;
            if (fast == head)
                return true;
        }
        return false;
    }
}
