// link - https://leetcode.com/problems/middle-of-the-linked-list/

public class _876_Middle_of_the_Linked_List {
    // Fast and slow pointer method - Time = O(n) - Space = O(1)
    public ListNode middleNode(ListNode head) {
        if (head.next == null)
            return head;

        ListNode middle = head;
        ListNode last = head;

        while (last != null && last.next != null) {
            middle = middle.next;
            last = last.next.next;
        }

        return middle;
    }
}
