class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.nodes:
                node.nodes[w] = TrieNode()
            node = node.nodes[w]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.nodes:
                return False
            node = node.nodes[w]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.nodes:
                return False
            node = node.nodes[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
