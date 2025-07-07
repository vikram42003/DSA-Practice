from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        while fast.next != None and n > 0:
            fast = fast.next
            n -= 1

        if n > 0:
            head = head.next
            return head

        slow = head
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
