# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    # Fast and Slow pointers - Time = O(n) - Space = O(1)
    # The reason the time is O(n) is becase for fast and slow to meet, they'd have to cover, at max, n length of 
    # distance, and on each iteration of the while loop slow moves forward by 1, bringing it 1 step FURTHER from
    # fast, but fast moves 2 steps, bringing it 2 steps CLOSER to slow, so net distance decreases by -1
    # Do that n times and they meet!
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # Fast will reach the end of the list before slow, so we just need to check if fast and its next possible
        # position is not null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        # If we broke out of the while loop it means we reached a None meaning the end of the list, so hasCycle = False
        return False
