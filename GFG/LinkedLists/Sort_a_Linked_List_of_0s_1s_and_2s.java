package GFG.LinkedLists;

// link - https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

class Sort_a_Linked_List_of_0s_1s_and_2s {
    static Node segregate(Node head) {
        Node curr = head;

        Node zeroHead = new Node(-1);
        Node zeroTail = zeroHead;

        Node oneHead = new Node(-1);
        Node oneTail = oneHead;

        Node twoHead = new Node(-1);
        Node twoTail = twoHead;

        while (curr != null) {
            Node node = curr;
            curr = curr.next;
            node.next = null;
            if (node.data == 0) {
                zeroTail.next = node;
                zeroTail = zeroTail.next;
            } else if (node.data == 1) {
                oneTail.next = node;
                oneTail = oneTail.next;
            } else {
                twoTail.next = node;
                twoTail = twoTail.next;
            }
        }

        head = null;
        Node tail = null;
        if (zeroHead.next != null) {
            head = zeroHead.next;
            tail = zeroTail;
        }

        if (oneHead.next != null) {
            if (head == null) {
                head = oneHead.next;
                tail = oneTail;
            } else {
                tail.next = oneHead.next;
                tail = oneTail;
            }
        }

        if (twoHead.next != null) {
            if (head == null) {
                head = twoHead.next;
            } else {
                tail.next = twoHead.next;
            }
        }

        return head;
    }
}
