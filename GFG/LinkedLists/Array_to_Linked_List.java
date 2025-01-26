// link - https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1

package GFG.LinkedLists;

class Node {
    int data;
    Node next;

    Node() {
        data = 0;
    }

    Node(int d) {
        data = d;
    } // constructor to create a new node
}

public class Array_to_Linked_List {

    static Node constructLL(int arr[]) {
        Node head = new Node();

        Node temp = head;
        temp.data = arr[0];

        for (int i = 1; i < arr.length; i++) {
            temp.next = new Node(arr[i]);
            temp = temp.next;
        }

        return head;
    }
}
