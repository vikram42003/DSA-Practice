// link - https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1

package GFG.LinkedLists;

class Node {
    int data;
    Node next;
    Node prev;

    Node(int x) {
        data = x;
        next = null;
        prev = null;
    }
}

public class Introduction_to_Doubly_Linked_List {
    Node constructDLL(int arr[]) {
        Node head = new Node(arr[0]);
        if (arr.length == 1)
            return head;

        Node curr = head;
        for (int i = 1; i < arr.length; i++) {
            Node newNode = new Node(arr[i]);
            curr.next = newNode;
            newNode.prev = curr;
            curr = curr.next;
        }

        return head;
    }
}
