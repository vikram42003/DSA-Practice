from collections import deque
from typing import List


class Solution:
    # Kahn's Topo Sort + Multi Source BFS - Time = O(N * M + C + E) - Space = O(C + E)
    # Where
    #   N = number of words
    #   M = average length of each word
    #   C = number of distinct characters across all words
    #   E = number of edges in the graph (max C², but usually much less)
    
    # We need to return the all the letters, and the letter whose relationship we do know should be in hierarchical order. Eg [ab, c], here we know that
    # a is smaller than c so res will be "ac", but for b, we dont know since the comparison short circuited but we need to return all letters, so we can
    # return "bac" or "abc", as long as a comes before c, the answer will be valid.
    # That relationship gives us the idea that we're gonna need to maintain a graph/adjacency list to denote the relations. And whats a good algo for 
    # traversing stuff in some sort of hierarchy of relations, Topo Sort!
    # We also notice that there could even be a forest possibly, e.g. ["ab", "bc", "rs", "tl"] forms three independent chains (a -> b -> c), (r -> s),
    # and (t -> l), so the overall graph is a forest. So we'll use a multi source bfs
    
    # Also there are 2 edge cases we need to consider -
    #   Edge Case 1 - w1 is "abcd" and w2 is "abc", so there is no certain way to rank d and therefore according to constrains the list is invalid
    #   Edge Case 2 - there is a cycle [ab, bc, ac] so this means a is less than b and b is also less than a, which is also not possible
    
    # Start by initializing adj with a set and indegree with 0 for all letters (since what we return should have all letters)
    # for each letter pair, first check for edge case 1 with the minLength match logic, then traverse them upto first non-matching character and then
    # mark the relationship ONE TIME ([er, et, r, t] should not do indegree[t] for r 2 times) and then break immediately (since we cant conclude anything
    # for letters after the first non-matching ones)
    # Then just put all the items with indegree 0 into q, traverse the q until empty, then in the end we compare if topo sort procesed all elements (it
    # wont if there is a cycle) by checking lengths and return the ans or "" for cycle
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))

            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2):
                return ""

            for j in range(minLength):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            w = q.popleft()
            res.append(w)
            for n in adj[w]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        print(res)
        return "".join(res) if len(res) == len(indegree) else ""

    # Topo Sort - Time = O(N * M + C + E) - Space = O(C + E)
    # Where
    #   N = number of words
    #   M = average length of each word
    #   C = number of distinct characters across all words
    #   E = number of edges in the graph (max C², but usually much less)
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))
            # Edge case 1: w1 is abcd and w2 is abc, so there is no certain way
            # to rank d and therefore according to constrains the list is invalid
            if w1[:minLength] == w2[:minLength] and len(w1) > len(w2):
                return ""

            for i in range(minLength):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break

        # here in seen w: False means visited, w: True means in current path
        # So if we see it again in current path then its a cycle
        seen = {}
        res = []

        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = True
            for n in adj[c]:
                if dfs(n):
                    return True

            seen[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
