class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    # The code idea is - We're gonnna need a HashMap to return values in O(1), and to keep track of the LRU and
    # MRU, without us having duplicates in our data structure (thats why we cant use a dq), we'll create a
    # Doubly Linked List with Left and Right pointers
    # Because of this, the hashmap be key: Node
    # Left pointer will tell us whats the Least Recently Used, and Right will tell us the most recently used
    # So whenever we put a new element (touching/creating still counts as use), we put it towards the right
    # If we need to evict a Node, we just get its reference from the HashMap, and then remove it, and put the new
    # one (or the replaced one in case of updates) to the right again
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def deleteNode(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insertRight(self, node: Node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertRight(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deleteNode(self.cache[key])

        newNode = Node(key, value)
        self.insertRight(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.cap:
            self.cache.pop(self.left.next.key)
            self.deleteNode(self.left.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
