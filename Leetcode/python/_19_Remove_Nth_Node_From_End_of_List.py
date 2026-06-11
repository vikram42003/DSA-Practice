from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Fast and Slow - Time = O(n) - Space = O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        # Move fast n elements ahead of slow, so that when fast.next = null, this means that slow.next is the one we need to skip
        for i in range(n):
            fast = fast.next
        
        # If n == size of linked list, meaning the head is the element we need to remove then fast will be None, so just return head.next in that case
        if fast:
            while fast.next:
                fast = fast.next
                slow = slow.next
            
            slow.next = slow.next.next
            return head
        else:
            return head.next
        
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
