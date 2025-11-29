from collections import defaultdict
from typing import List


class Solution:
    # Euler path / Hierholzer's Algo - Time = O(E log E) - Space = O(V + E)
    # The problem statement states that at least one valid itinerary can be formed so we dont need to
    # do the indegreee - outdegree calculation step to check if Euler path exists or not

    # First we create an adjacency list but we sort tickets in descending lexical order before adding
    # the edges, this is because Euler algo adds items from the end to start, and the problem statement
    # states that the path with the smallest lexical order should be the answer

    # Then we create a res list which will store the final positions of tickets and a stack,
    # initialized with "JFK", which is where we'll add all items BEFORE we start popping any item and adding it to res
    # Then iterate as long as stack isnt empty, and for each airport we can go to from current
    # airport, pop it from adj and add it to stack, mimicing a dfs, so go as deep as we can and once
    # we're at the last airport and no more items are left in adj, then we'll add tickets from stack
    # to res from the last airport all the way to first
    # Then reverse res and return

    # src - https://www.youtube.com/watch?v=5G0HyBhqpQo
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dest in sorted(tickets, reverse=True):
            adj[src].append(dest)

        res, stack = [], ["JFK"]

        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
                print(stack)
            res.append(stack.pop())

        return res[::-1]
