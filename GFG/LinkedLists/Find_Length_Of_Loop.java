// link - https://www.geeksforgeeks.org/problems/find-length-of-loop/1

package GFG.LinkedLists;

class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

public class Find_Length_Of_Loop {
    public static int countNodesinLoop(Node head) {
        if (head == null)
            return 0;

        Node slow = head;
        Node fast = head;
        int count = 0;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                count++;
                slow = slow.next;
                while (slow != fast) {
                    count++;
                    slow = slow.next;
                }
                break;
            }
        }

        return count;
    }
}
