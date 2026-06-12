# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    # Cleaner Version - Time = O(n) - Space = O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = 0 if total < 10 else 1
        
            cur.next = ListNode(total if total < 10 else total % 10)
            cur = cur.next

            # Safely advance l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next
    
    # Simulate addition by hand, the units are already positioned to be added correctly, just carry the "carry"
    # from left to right instead of right to left
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        res = head
        i, j = l1, l2
        while i and j:
            v = i.val + j.val + carry
            if carry == 1:
                carry = 0

            if v < 10:
                res.next = ListNode(v)
            else:
                carry = 1
                res.next = ListNode(v % 10)

            res = res.next
            i = i.next
            j = j.next

        i = i if i else j
        while i:
            v = i.val + carry
            if carry == 1:
                carry = 0

            if v < 10:
                res.next = ListNode(v)
            else:
                carry = 1
                res.next = ListNode(v % 10)
            res = res.next
            i = i.next

        if carry:
            res.next = ListNode(1)
            res = res.next

        return head.next
