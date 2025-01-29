// link - https://leetcode.com/problems/add-two-numbers/

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

public class _2_Add_Two_Numbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // (probably) Optimal approach - Time = O(n) - Space = O(n)

        ListNode head = new ListNode();
        ListNode curr = head;

        curr.val = (l1.val + l2.val) % 10;
        int carry = (l1.val + l2.val) / 10;

        l1 = l1.next;
        l2 = l2.next;

        while (l1 != null || l2 != null) {
            int n1 = l1 != null ? l1.val : 0;
            int n2 = l2 != null ? l2.val : 0;
            int sum = n1 + n2 + carry;

            carry = sum / 10;

            ListNode temp = new ListNode(sum % 10);
            curr.next = temp;
            curr = temp;

            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }

        if (carry > 0) {
            ListNode temp = new ListNode(carry);
            curr.next = temp;
            curr = temp;
        }

        return head;
    }
}
