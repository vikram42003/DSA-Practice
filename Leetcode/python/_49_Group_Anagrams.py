from collections import defaultdict
from typing import List


class Solution:
    # HashMap + Tuple = Time = O(n * k) - Space = O(n * k)
    # Same as below except instead of sorting array values, we just count the frequency of each alphabet, and then hash
    # with that (converted to tuple) as the key, so that we can uniqely detect anagrams since they'll have the same
    # frequency of elements
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            seen[tuple(freq)].append(s)
        return [arr for arr in seen.values()]

    # HashMap and Sort - Time = O(n * k log k) - Space = O(n * k)
    # Use a HashMap, and just let the key be sorted s in strs to uniquely identify anagrams, and add the corresponding
    # word to its key
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            seen["".join(sorted(s))].append(s)
        return [arr for arr in seen.values()]

    # Sort the words in the list
    # Make it a tuple to retain original indices and then sort the whole list itself
    # Add the original of the first sorted word in sortedStrs to the res array of arrays and then iterate over
    # sortedStrs, if its the same as previous then it belongs in the same group, otherwise create a new group for it
    # by appending an empty list to res, and then append the original word to the latest list in res
    # and then return res
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = ["".join(sorted(word)) for word in strs]
        sortedStrs = sorted((x, i) for i, x in enumerate(sortedStrs))
        print(sortedStrs)

        res = [[]]
        res[0].append(strs[sortedStrs[0][1]])

        for i in range(1, len(strs)):
            if sortedStrs[i][0] != sortedStrs[i - 1][0]:
                res.append([])

            res[-1].append(strs[sortedStrs[i][1]])

        return res
