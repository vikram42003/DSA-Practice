// link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

public class _19_Remove_Nth_Node_From_End_of_List {
    // 2 passes solution
    public ListNode removeNthFromEnd2Passes(ListNode head, int n) {
        int size = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            size++;
        }

        n = size - n + 1;

        if (n == 1) {
            // remove the first element of the list
            return head.next;
        } else {
            // remove the nth element from the start
            n--;
            curr = head;
            while (n != 1) {
                curr = curr.next;
                n--;
            }
            curr.next = curr.next.next;
        }

        return head;
    }
}
