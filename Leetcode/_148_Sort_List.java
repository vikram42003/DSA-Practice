// link - https://leetcode.com/problems/sort-list/

import java.util.ArrayList;
import java.util.Collections;

public class _148_Sort_List {
    public ListNode sortList(ListNode head) {
        // Naive solution - store the values in an array and then sort it
        ArrayList<Integer> list = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            list.add(curr.val);
            curr = curr.next;
        }

        Collections.sort(list);

        curr = head;
        int i = 0;
        while (curr != null) {
            curr.val = list.get(i++);
            curr = curr.next;
        }

        return head;
    }
}
