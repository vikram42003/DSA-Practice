from typing import List


class Solution:
    # Greedy - Time = O(n) - Space = O(n)
    # We precompute where each character ends and store it in endings
    # Then we iterate through the array, taking start as 0 and then see where the current character
    # ends, and we take the max of the end. Now when we move over to the next array, if it should
    # belong to the first partition then max wont move, but if it moves max then it will extend
    # the first partition. If, while iterating, we see that i >= end, then that means that all
    # the duplicating characters that can belong to this partition are inside it, and we can now
    # add it to res (with +1 to account for 0 indexing) and rest start to be the next element, and
    # max will reset itself in the next iteration
    def partitionLabels(self, s: str) -> List[int]:
        endings, n = {}, len(s)
        for i in range(n):
            endings[s[i]] = i

        start, end = 0, 0
        res = []
        for i in range(n):
            end = max(end, endings[s[i]])
            if i >= end:
                res.append(end - start + 1)
                start = i + 1

        return res
