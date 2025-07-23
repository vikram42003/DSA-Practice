from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Store and Sort = Time - O(n log n) - Space = O(n)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return None

        dummy = ListNode()

        nums = []
        for l in lists:
            while l:
                nums.append(l)
                l = l.next

        nums.sort(key=lambda n: n.val)

        cur = dummy
        for n in nums:
            cur.next = n
            cur = cur.next

        return dummy.next
