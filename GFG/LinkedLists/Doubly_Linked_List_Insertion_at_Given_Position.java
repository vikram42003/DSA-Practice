// link - https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1

package GFG.LinkedLists;

class Node {
    int data;
    Node next;
    Node prev;

    Node(int data) {
        this.data = data;
        next = prev = null;
    }
}

public class Doubly_Linked_List_Insertion_at_Given_Position {
    Node addNode(Node head, int p, int x) {
        Node curr = head;

        while (curr != null) {
            p--;
            if (p < 0) {
                Node newNode = new Node(x);
                newNode.prev = curr;
                newNode.next = curr.next;
                curr.next = newNode;
                break;
            }
            curr = curr.next;
        }

        return head;
    }
}
