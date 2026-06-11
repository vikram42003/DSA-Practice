from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = ListNode()
        cur = sortedHead

        i, j = list1, list2
        while i and j:
            if i.val <= j.val:
                cur.next = i
                i = i.next
            else:
                cur.next = j
                j = j.next
            cur = cur.next

        cur.next = i if i else j

        return sortedHead.next
