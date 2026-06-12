# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    # Map - Time = O(n) - Space = O(n)
    # The core idea is that we accept that we'll need to do 2 passes
    # First we duplicate all the nodes that are in the original list and we map the newly created node to its
    # original (We initialize the map with { None: None } so that the null case is taken care of through the map)
    # After that we create the same relationships between the nodes as the original ones, taking its mapped
    # copy through the duplicate map
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copyMap = {None: None}

        cur = head
        while cur:
            copyMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = copyMap[cur]
            copy.next = copyMap[cur.next]
            copy.random = copyMap[cur.random]
            cur = cur.next

        return copyMap[head]
