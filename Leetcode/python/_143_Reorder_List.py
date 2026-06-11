# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # Split with Fast and Slow, Reverse and Interweave - Time = O(n) - Space = O(1)
    # Careful with the interweave logic, what we do there is first we run the loop while both l and r are not None
    # Then we first save their nexts in t1 and t2, since we'll be overwriting the nexts, then we set l.next to r
    # and r.next to t1, then update l and r with t1 and t2
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        l, r = head, self.reverse(second)

        while l and r:
            t1, t2 = l.next, r.next
            l.next = r
            r.next = t1
            l, r = t1, t2

    def reverse(self, head):
        cur, prev = head, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
