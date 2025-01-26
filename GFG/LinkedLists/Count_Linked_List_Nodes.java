// link - https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0

package GFG.LinkedLists;

public class Count_Linked_List_Nodes {
    public int getCount(Node head) {
        int count = 0;
        Node curr = head;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        return count;
    }
}
