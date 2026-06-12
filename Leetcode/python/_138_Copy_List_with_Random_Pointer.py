# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    # Interweave - Time = O(n) - Space = O(1)
    # The core idea is we'll first interweave the new lists nodes right next to the original one
    # With that when we want to map a relation, the original and the clone are right next to each other, so we can always get the newly created copy for that particular node by just looking 1 step ahead
    # We'll have to do 3 passes (since if a random "looks ahead", then we wont be able to map a relationship on the fly since we havent created a copy for that node and we dont know how many nodes are between cur and that one) -
    # First pass - Interweave the new nodes
    #   - Just store the next in nxt and then put the new one between them, then set cur to nxt
    # Second pass - Map the relationship for the randoms
    #   - if cur.random (beacause it could be null), then set cur.next.random = cur.random.next (set copy of cur, at the idx next to cur to copy of random, at cur.random.next)
    # Third pass - Split the two lists again
    #   - We'll need a dummy head, set copyCur.next to cur.next and move it forward, then update cur to cur.next.next, this will correctly sever the two lists
    # Then return the copyHead
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        cur = head
        while cur:
            nxt = cur.next
            new = Node(cur.val, nxt)
            cur.next = new
            cur = nxt

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        copyHead = Node(0)
        cur, copyCur = head, copyHead
        while cur:
            copyCur.next = cur.next
            copyCur = copyCur.next
            cur = cur.next.next

        return copyHead.next

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
