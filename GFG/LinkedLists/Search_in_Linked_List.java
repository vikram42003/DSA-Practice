// link - https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1

package GFG.LinkedLists;

public class Search_in_Linked_List {
    static boolean searchKey(int n, Node head, int key) {
        Node curr = head;
        while (curr != null) {
            if (curr.data == key)
                return true;
            curr = curr.next;
        }
        return false;
    }
}
