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
    
    # (Merge Sort's) Merge - Time = O(n log k) - Space = O(1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            combined = self.merge(list1, list2)
            print_list(combined)
            lists.append(combined)
        
        return lists[0]
    
    def merge(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        
        return dummy.next
    
    
def print_list(node):
    print('->'.join(map(str, iter_list(node))))

def iter_list(node):
    while node:
        yield node.val
        node = node.next
        
test = Solution()
# ans = [1,1,2,3,4,4,5,6]
lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = []
for arr in lists:
    dummy = cur = ListNode()
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    linked_lists.append(dummy.next)
print_list(test.mergeKLists(linked_lists))
