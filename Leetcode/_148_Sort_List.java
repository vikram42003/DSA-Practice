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
    public ListNode sortListMergeSort(ListNode head) {
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

    // Bottom-up Merge Sort approach - Time = O(n log n) - Space = O(1)
    public ListNode sortList(ListNode head) {
        // Handle edge cases
        if (head == null || head.next == null) {
            return head;
        }

        // The head of our list will change as we sort it so dummy head will serve as an
        // anchor for the entire list
        // dummy.next will be the head of the final sorted list
        ListNode dummy = new ListNode();

        // Get the size of the list
        dummy.next = head;
        int length = 0;
        while (head != null) {
            length++;
            head = head.next;
        }

        // step will be the size of the sublist we consider in each iteration of the
        // loop
        // step <<= 1 will do bitwise rightshit and assign operation on step
        // It will basically double the step or perform step *= 2 on each iteration
        for (int step = 1; step < length; step <<= 1) {
            // prev will be the dummy for each sub list in each iteration
            // prev will also be the last node in the last list we merged
            // the merge function will build the merged list starting from prev.next
            // therefore reconnecting the list we disconnected in the split step
            ListNode prev = dummy;

            // curr will track the left part of the current list we are going to merge
            // in each outer loop current will start from the head of the full list
            ListNode curr = dummy.next;

            while (curr != null) {
                // left will be
                ListNode left = curr;
                // split the left part of the list, set left's tail's next to null
                // and then return the element after tail or null
                // here we assign that element to right
                ListNode right = split(left, step);
                // split the right part of the list, set right's tail's next to null
                // and then return the element after tail or null
                // here we assign that element to curr and it will be the start of the
                // next partition we need to consider
                curr = split(right, step);
                // take the left part and right part and then merge them
                // build the merged list starting at prev.next and then return the tail
                // of the merged list
                // that tail will serve as the point where we start building the next merged
                // list
                prev = merge(left, right, prev);
            }
        }

        // dummy.next will be the start of the final list
        return dummy.next;
    }

    public ListNode split(ListNode start, int step) {
        if (start == null)
            return null;

        for (int i = 1; start.next != null && i < step; i++) {
            start = start.next;
        }
        ListNode nextHead = start.next;
        start.next = null;
        return nextHead;
    }

    public ListNode merge(ListNode left, ListNode right, ListNode curr) {
        while (left != null && right != null) {
            if (left.val < right.val) {
                curr.next = left;
                left = left.next;
                curr = curr.next;
            } else {
                curr.next = right;
                right = right.next;
                curr = curr.next;
            }
        }
        if (left != null) {
            curr.next = left;
        }
        if (right != null) {
            curr.next = right;
        }
        // Move curr to be the last node of the merged list, this will be where we start
        // connecting the next merged list
        while (curr.next != null) {
            curr = curr.next;
        }
        return curr;
    }
}
