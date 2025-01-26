// link - https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0

package GFG.LinkedLists;

class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class Linked_List_Insertion_At_End {
    Node insertAtEnd(Node head, int x) {
        if (head == null)
            return new Node(x);

        Node curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = new Node(x);
        return head;
    }
}
