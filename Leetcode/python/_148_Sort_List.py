# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


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

    # Bottom Up Merge Sort (Iterative) - Time = O(n log n) - Space = O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        dummy = ListNode(0, head)

        step = 1
        while step < n:
            prev = dummy
            cur = prev.next

            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)

                newHead, newTail = self.merge(left, right)

                prev.next = newHead
                prev = newTail

            step *= 2

        return dummy.next

    def split(self, start, step):
        if not start:
            return None

        for i in range(step - 1):
            if start.next:
                start = start.next
            else:
                break

        nextHead = start.next
        start.next = None
        return nextHead

    def merge(self, left, right):
        newHead = ListNode()
        tail = newHead

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right

        while tail.next:
            tail = tail.next

        return newHead.next, tail


# Examples:
example1 = [4, 2, 1, 3]
example2 = [-1, 5, 3, 4, 0]

# Create and print both
head1 = create_linked_list(example1)
head2 = create_linked_list(example2)

test = Solution()

print("Example 1:")
print_linked_list(head1)
print(test.sortList(head1))

# print("Example 2:")
# print_linked_list(head2)
# print(test.sortList(head2))
