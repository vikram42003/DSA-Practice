package Concepts.LinkedLists;

// Defining a Linked List in Java
class Node {
    int val;
    Node next;

    Node(int val) {
        this.val = val;
    }
}

public class LinkedList {
    public static void main(String[] args) {
        System.out.println("Defining a Linked list -");
        Node head = new Node(0);
        System.out.println(head.val);

        System.out.println();

        // Inserting at the start of a singly linked list
        Node insert1 = new Node(-1);
        insert1.next = head;
        head = insert1;

        // Print the list after insertion at the beginning
        printList(head);

        System.out.println();

        // Insert at the end of the list
        Node curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = new Node(1);

        // Print the list after insertion at the end
        printList(head);
    }

    public static void printList(Node curr) {
        // Traversing and printing a singly linked list
        while (curr != null) {
            System.out.print("" + curr.val + "   ");
            curr = curr.next;
        }
        System.out.println();
    }
}
