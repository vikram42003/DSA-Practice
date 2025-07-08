# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Naive with Extra Memory - Time = O(n log n) - Space = O(n)
    # For some reason does really well 97.26% Time and 87.00% Space 💀💀
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort()

        cur = head
        for i in range(len(arr)):
            cur.val = arr[i]
            cur = cur.next

        return head
