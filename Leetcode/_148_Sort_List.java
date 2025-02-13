// link - https://leetcode.com/problems/sort-list/

import java.util.ArrayList;
import java.util.Collections;

public class _148_Sort_List {
    public ListNode sortListNaive(ListNode head) {
        // Naive solution - store the values in an array and then sort it
        ArrayList<Integer> list = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            list.add(curr.val);
            curr = curr.next;
        }

        Collections.sort(list);

        curr = head;
        int i = 0;
        while (curr != null) {
            curr.val = list.get(i++);
            curr = curr.next;
        }

        return head;
    }

    // Merge Sort Approach - Time = O(n log n) - Space = O(log n)
    public ListNode sortList(ListNode head) {
        // base case - if theres 0 or 1 elements in the list then return that
        if (head == null || head.next == null) {
            return head;
        }

        // Split the list into 2 parts
        ListNode left = head;
        ListNode right = getMidNode(head);

        // right will be the middle node and will still be connected to the right part
        // of the list
        // so save right list's head in temp and then set the next of left list's tail
        // as null
        ListNode temp = right.next;
        right.next = null;
        right = temp;

        left = sortList(head);
        right = sortList(right);

        return merge(left, right);
    }

    public ListNode getMidNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public ListNode merge(ListNode left, ListNode right) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while (left != null && right != null) {
            if (left.val < right.val) {
                curr.next = left;
                curr = curr.next;
                left = left.next;
            } else {
                curr.next = right;
                curr = curr.next;
                right = right.next;
            }
        }

        if (left != null) {
            curr.next = left;
        }

        if (right != null) {
            curr.next = right;
        }

        return dummy.next;
    }
}
