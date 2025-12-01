from typing import List


class Solution:
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
