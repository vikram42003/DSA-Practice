from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iterative - Time = O(n) - Space = O(1)
    # Its a linked list, just reverse the links and move head to last node
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    # Recursive - Time = O(n) - Space = O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(cur, prev):
            if not cur:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return rec(next, cur)

        return rec(head, None)
