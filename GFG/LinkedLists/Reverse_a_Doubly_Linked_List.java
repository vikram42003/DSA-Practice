// link - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

package GFG.LinkedLists;

class DLLNode {
    int data;
    DLLNode next;
    DLLNode prev;

    DLLNode(int val) {
        data = val;
        next = null;
        prev = null;
    }
}

public class Reverse_a_Doubly_Linked_List {
    public DLLNode reverseDLL(DLLNode head) {
        while (head.next != null) {
            DLLNode temp = head.next;
            head.next = head.prev;
            head.prev = temp;
            head = temp;
        }
        DLLNode temp = head.next;
        head.next = head.prev;
        head.prev = temp;

        return head;
    }
}
