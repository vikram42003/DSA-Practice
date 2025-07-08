# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two Pointers One pass ( ͡° ͜ʖ ͡°) - Time = O(n) - Space = O(1)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller, larger = None, None
        smallerStart, largerStart = None, None

        while head:
            if head.val < x:
                if not smaller:
                    smaller = head
                    smallerStart = head
                else:
                    smaller.next = head
                    smaller = smaller.next
            else:
                if not larger:
                    larger = head
                    largerStart = head
                else:
                    larger.next = head
                    larger = larger.next

            head = head.next

        if larger:
            larger.next = None
        if smaller:
            smaller.next = largerStart

        return smallerStart or largerStart
