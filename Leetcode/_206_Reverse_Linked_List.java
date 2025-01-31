// link - https://leetcode.com/problems/reverse-linked-list/

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class _206_Reverse_Linked_List {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public ListNode reverseListRec(ListNode head) {
        return reverseListRecursive(null, head, null);
    }

    public ListNode reverseListRecursive(ListNode prev, ListNode curr, ListNode newHead) {
        if (curr == null) {
            newHead = prev;
            return newHead;
        }
        newHead = reverseListRecursive(curr, curr.next, newHead);
        curr.next = prev;
        return newHead;
    }
}
