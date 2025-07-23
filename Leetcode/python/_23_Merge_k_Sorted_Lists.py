import heapq
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
    
    # Heap - Time = O(n log k) - Space = O(k)
    # The lists are already in ascending order, so only keep track of each head of the list, add the min from the current heads
    # and then move that head forward and add its value to the pool again. This way we only store k elements and we check k elements
    # with the heap n times
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return None

        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        dummy = cur = ListNode()
        while heap:
            val, i, l = heapq.heappop(heap)
            cur.next = l
            cur = cur.next
            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))
        
        return dummy.next
