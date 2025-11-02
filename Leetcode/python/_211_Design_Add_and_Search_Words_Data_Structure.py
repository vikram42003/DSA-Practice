class Node:
    def __init__(self):
        self.nodes = {}
        self.end = False

# Tries and DFS - Time = O(n^b) - Space = O(n)
# Where n is the length of word and b is the breadth of nodes for each dfs we had to run

# Just split the word by chars and put it in the Trie one my one, create a TrieNode( nodes: {}, end: boolean ) for each missing node
# search function should take the word, starting idx (default 0) and the TrieNode to start the search from (default None, set to the root of Trie
# if its None (can't set default value with self in default args in python)) and search normally with curr for any char
# If we see a "." then switch the approach and run search again for each child in current TrieNode's children from the i + 1 char
# Do the same for any subsequent "." and immediately return True if a recursive search returns true. Else return false

class WordDictionary:

    def __init__(self):
        self.list = Node()

    def addWord(self, word: str) -> None:
        curr = self.list
        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = Node()
            curr = curr.nodes[w]
        curr.end = True

    def search(self, word: str, start=0, node=None) -> bool:
        curr = node
        if not node:
            curr = self.list

        for i in range(start, len(word)):
            # If a "." is found, run self search from the next letter for all child nodes
            if word[i] == ".":
                for key in curr.nodes:
                    if self.search(word, i + 1, curr.nodes[key]):
                        return True
                return False
            elif word[i] in curr.nodes:
                curr = curr.nodes[word[i]]
            else:
                return False

        return curr.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
