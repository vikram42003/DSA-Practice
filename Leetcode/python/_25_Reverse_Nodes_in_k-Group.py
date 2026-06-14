from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # The code idea is - We need to make k lengthed partitions of the list, and then reverse those partitions one by one
    # if a partition's size is less than k then leave it as is, it also means we're done
    # First we're gonna need a dummy head to act as the newHead, since we'll also be reversing from the first node
    # So we'll have a prev, the node right before the part we reverse, so that we can attach the reversed list to it
    # Then behind, to track the head of the part we reverse
    # And the ahead, to track the last node, we'll move this k - 1 steps so that its at the last element of the partition
    # we need to remove, we remember its next and set its next to None to snip the list
    # (While moving ahead, if it becomes None BEFORE moving forward k - 1 steps then quit the whole loop,
    # append prev.next = behind to complete the list and return)
    # Otherwise we reverse the list with the reverse function, take the head and tail of the reversed part 
    # (tail will just be "behind" btw)
    # After that just set prev.next as the head of reversed list, prev to tail and set ahead = behind = nxt
    # And return dummy.next
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        # prev = 1 node before current behind
        # behind = start of the list partition we have to reverse
        # ahead = start of the next list partition we have to reverse
        prev, behind, ahead = dummy, head, head

        while ahead:
            # Push ahead k - 1 steps so that we can sever the prev partition at current ahead position and then move it ahead to be k steps ahead of behind
            # break if ahead becomes None before moving k - 1 steps, this means the partition is not big enough
            # for us to reverse so skip all that and return
            for i in range(k - 1):
                ahead = ahead.next
                if not ahead:
                    break
            if not ahead:
                break

            nxt = ahead.next
            ahead.next = None

            head, tail = self.reverse(behind)
            prev.next = head
            prev = tail

            behind = ahead = nxt

        prev.next = behind
        return dummy.next

    def reverse(self, head: ListNode):
        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # Prev will be the head and tail will just be head since we've reversed it
        return prev, head
