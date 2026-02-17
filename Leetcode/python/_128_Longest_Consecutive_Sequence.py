from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        res = 0

        for n in nums:
            # looking at duplicates would mess us up and make us do duplicate calculations
            if n in lengths:
                continue

            # Give n a value in lengths to mark it visited so we skip duplicates
            # (Note - this does not mess up any calcuations due to overwrite, because if n was already
            # in the lengths dict, then we would have just skipped it due to the code above)
            lengths[n] = 0

            # Get the lengths of the subsequences of prev and next elements, so then the total final
            # length would be prevLen + 1 (for cur) + nextLen
            prevElementsLength = lengths.get(n - 1, 0)
            nextElementsLength = lengths.get(n + 1, 0)

            finalLen = prevElementsLength + 1 + nextElementsLength

            # Update the starting and ending element's lengths so that we know it in the future
            lengths[n - prevElementsLength] = finalLen
            lengths[n + nextElementsLength] = finalLen

            # update res
            res = max(res, finalLen)

        return res

    # The core idea is, we first convert it all to a set, and then we iterate over the set (since it wont have duplicates and O(1) checks)
    # and then see if n-1 is not in set, that means it cloud be a start of a longest sequence, so count how high up it gets
    # by increasing it one by one in a while loop and then return the max length
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                counter = 0
                while n in numsSet:
                    counter += 1
                    res = max(res, counter)
                    n += 1

        return res
