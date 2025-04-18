// link - https://leetcode.com/problems/palindrome-linked-list/

import java.util.ArrayList;
import java.util.Stack;

public class _234_Palindrome_Linked_List {
    // Store it as an ArrayList approach
    public boolean isPalindromeNaive(ListNode head) {
        ArrayList<Integer> list = new ArrayList<>();

        while (head != null) {
            list.add(head.val);
            head = head.next;
        }

        for (int i = 0, j = list.size() - 1; i < j; i++, j--) {
            if (list.get(i) != list.get(j))
                return false;
        }

        return true;
    }

    // Reverse the right half appraoch
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode revHead = reverseList(slow.next);

        while (head != null && revHead != null) {
            if (head.val != revHead.val) {
                return false;
            }
            head = head.next;
            revHead = revHead.next;
        }

        return true;
    }

    public ListNode reverseList(ListNode start) {
        ListNode prev = null;
        while (start != null) {
            ListNode next = start.next;
            start.next = prev;
            prev = start;
            start = next;
        }
        return prev;
    }

    // Stack approach
    public boolean isPalindromeStack(ListNode head) {
        Stack<Integer> stack = new Stack<>();
        ListNode curr = head;

        // push all elements onto the stack
        while (curr != null) {
            stack.push(curr.val);
            curr = curr.next;
        }

        // pop elements off of stack and check if end elements are same as start
        // elements
        curr = head;
        while (curr != null) {
            if (curr.val != stack.pop()) {
                return false;
            }
            curr = curr.next;
        }

        return true;
    }
}
