from typing import List


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = TrieNode()
            curr = curr.nodes[w]
        curr.word = word


class Solution:
    # Trie and DFS - Time = (words * eachWordLength + matrixLength * matrixBreadth * dfsDepth * dfsBreadth) - Time = O(wordLength + stackSpace)
    # Time: O(N * L + M * W * 4^D)
    #   - N*L to build the Trie (N=num words, L=max word length)
    #   - M*W*4^D to search the board (M*W=board size, 4^D=DFS work)
    # Space: O(N*L)
    #   - O(N*L) for the Trie (dominant)
    #   - O(L) for the recursion stack
    
    # The basic idea is we first create a trie for each node and then we iterater over the matrix and check for starting positions of a word in the trie
    # If we find it then we run a dfs in all 4 directions (mark visited as #) and see if we can check off words along the way. (check off "OAT" while
    # looking for "OATH") and add it to res if any word ends at current letter (by checking TreeNode's word property which should contain the whole word)
    # For optimization we clear the visited words from the Trie and delete the tree branch if all curr.nodes have been visited.
    
    # 1. First put all the words in a Trie (Also use curr.word instead of curr.end, so that we can quickly get the word we need to add to res)
    # 2. Then, iterate over the matrix and run dfs for each letter and pass the root node of the trie
    # 3. The base case for dfs will be if row/col is out of bounds or the current letter is not in curr.nodes.
    # 4. Then save curr as parent (We need this for pruning) AND THEN move curr over to be its next value. We also mark board[row][col] as "#" (after saving
    # the original value) so that we dont add the same letter and we can change it back
    # 5. We check if a word ends at this node by checking curr.word (which should have the full word that ends there) and add it to res and set it to None.
    # 6. Then we run dfs for all 4 directions and for optimization, delete curr if it has no children, it's a dead-end path. We delete it from its parent 
    # node to prevent future DFS calls from exploring this useless branch. 
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        self.trie = Trie()

        # Put the words in the Trie
        for word in words:
            self.trie.addWord(word)

        def dfs(row, col, curr):
            # Base Case: invalid indices or current letter not in trie
            if (
                row < 0
                or col < 0
                or row == len(board)
                or col == (len(board[0]))
                or board[row][col] not in curr.nodes
            ):
                return

            # Save parent so that we can prune the tree after visiting it
            parent = curr
            # Update curr so that we are at the word we just checked for, and can check if it ends
            # here or if we can keep recursing
            curr = curr.nodes[board[row][col]]

            # If a word ends here, add it to res and prune
            if curr.word != None:
                res.append(curr.word)
                curr.word = None

            original = board[row][col]
            # Mark visited
            board[row][col] = "#"

            dfs(row + 1, col, curr)
            dfs(row - 1, col, curr)
            dfs(row, col + 1, curr)
            dfs(row, col - 1, curr)

            # mark unvisited
            board[row][col] = original

            # Prune - delete curr if all branches of curr have been explored
            if not curr.nodes:
                del parent.nodes[board[row][col]]

        for row in range(len(board)):
            for col in range(len(board[row])):
                dfs(row, col, self.trie.root)

        return res


class Solution:
    # Backtracking (TLE) - Time = (n^m) - Space = O(n)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        for word in words:
            if self.search(board, word):
                res.append(word)

        return res

    def search(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                # Find the starting letter then search from there
                if board[row][col] == word[0]:
                    # If we find the whole word, return true and exit
                    if self.searchAdjacent(board, word, 0, row, col, set()):
                        return True

        return False

    def searchAdjacent(self, board, word, idx, row, col, visited):
        # Base case 1: we found the full word
        if idx == len(word) - 1:
            return True
        # Base case 2: current board[row][col] does not match current letter
        # Likely wont happen because of algo design but nice to have guard rails
        if board[row][col] != word[idx]:
            return False

        visited.add((row, col))
        idx += 1

        if (
            (row - 1, col) not in visited
            and row > 0
            and board[row - 1][col] == word[idx]
        ):
            if self.searchAdjacent(board, word, idx, row - 1, col, visited):
                return True

        if (
            (row + 1, col) not in visited
            and row < len(board) - 1
            and board[row + 1][col] == word[idx]
        ):
            if self.searchAdjacent(board, word, idx, row + 1, col, visited):
                return True

        if (
            (row, col - 1) not in visited
            and col > 0
            and board[row][col - 1] == word[idx]
        ):
            if self.searchAdjacent(board, word, idx, row, col - 1, visited):
                return True

        if (
            (row, col + 1) not in visited
            and col < len(board[0]) - 1
            and board[row][col + 1] == word[idx]
        ):
            if self.searchAdjacent(board, word, idx, row, col + 1, visited):
                return True

        visited.remove((row, col))
        return False
