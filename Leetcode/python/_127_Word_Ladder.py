from collections import defaultdict, deque
from typing import List


class Solution:
    # WildCard + BFS - Time = O(n * m ^ 2) - Space = O(n * m)
    # Where n is the number of words in wordList and m is len(word)
    # For time we iterate over n words a couple times and we run a nested loop for each letter of each word
    # For space we may create m wildcard entries for every single word + n for dict and n for seen

    # The main idea is, we have a beginWord, and we have to make it endWord by chaging it one letter at a time
    # We also have a wordList that lists to us all the possible changes we have available to make
    # And from that we have to find the shortest path of changes that gets us from beginWord to endWord
    # "shortest path" screams that we need a pathfinding alo like Djikstra or BFS, BFS would be applicable here.
    # We can make an adjacency list by checking for each word the words it can reach in n^2 but thats inefficient
    # From the constraints we see that len(wordList) can be upto 5000 but len(word) can only be upto 10
    # So from that we use a trick. We convert each letter of a word to a wildcard to denote that it can be changed like
    # for hit we'd save { *it: [hit], h*t: [hit], hi*: [hit] } in our adj list. Do that for each word
    # and we'll have every single possible hop we can make from the current word
    # Once we've done that then we can just keep a seen set and a deque, start by putting beginWord in each
    # and do bfs level by level and use the wildcard trick to see all the neighbours of current word
    # and add them to the list and if we find that current word == endWord, then return the level of
    # BFS we're at and we're done
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                wildCardPattern = word[:j] + "*" + word[j + 1 :]
                adj[wildCardPattern].append(word)

        seen = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                else:
                    for j in range(len(word)):
                        wildCardPattern = word[:j] + "*" + word[j + 1 :]
                        for n in adj[wildCardPattern]:
                            if n not in seen:
                                seen.add(n)
                                q.append(n)
            res += 1

        return 0
