// link - https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1

package GFG.LinkedLists;

class Node {
    int data;
    Node next;
    Node prev;

    Node(int val) {
        data = val;
        next = null;
        prev = null;
    }
}

public class Delete_in_a_Doubly_Linked_List {
    public Node deleteNode(Node head, int x) {
        if (x == 1) {
            head = head.next;
            head.prev = null;
            return head;
        }

        Node curr = head;

        x -= 2;
        while (--x >= 0) {
            curr = curr.next;
        }

        curr.next = curr.next.next;
        if (curr.next != null)
            curr.next.prev = curr;

        return head;
    }
}
