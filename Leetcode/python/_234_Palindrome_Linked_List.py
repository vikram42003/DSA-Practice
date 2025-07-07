# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    # Fast and Slow Pointers - Time = O(n) - Space = O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Get to the middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        start = head
        # Reverse list from middle to the end
        revStart = self.rev(slow)

        # Now check if start and revStart match
        while start and revStart:
            if start.val != revStart.val:
                return False
            start = start.next
            revStart = revStart.next

        return True

    def rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
