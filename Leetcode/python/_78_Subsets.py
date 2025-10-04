from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            curr = []
            for p in res:
                copy = p.copy()
                copy.append(i)
                curr.append(copy)
            res.extend(curr)

        return res

    # Concise (and more memory efficient) version
    #
    # for nums = [ 1, 2, 3 ]
    # nums will have a total of 8 subsets (2 ^ 3)
    # and the decision tree will look like this
    #
    #                               []                          we start out with an empty subset
    #                       /                 \
    #                  [1]                      []              now at this point, we can either add element i to the curr subset, or we can just not add it
    #             /           \             /        \
    #          [1,2]          [1]         [2]         []        now at this step, we have a choice to either add 2 to each previous subset or to not add it
    #         /     \        /    \      /    \     /    \
    #      [1,2,3] [2,3]   [1,2] [1]   [2,3] [2]   [3]   []     similarly we do the same thing here, but now that i == len(nums), we have considered all levels and we can return
    #
    # so for each level of the decision tree, we'll look at the ith element, and revursively either add ith element to the result or not add it
    # actually we're just running dfs on the decision tree 😭

    def subsetsConcise(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [p + [i] for p in res]
        return res

    def subsetsBacktracking(self, nums: List[List[int]]) -> List[List[int]]:
        res, curr, n = [], [], len(nums)

        def backtrack(i):
            if i >= n:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)

        backtrack(0)

        return res

    # For loop version
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr, n = [], [], len(nums)

        def rec(i):
            for j in range(i, n):
                curr.append(nums[j])
                res.append(curr[:])
                rec(j + 1)
                curr.pop()

        rec(0)

        return res
    
    # Bitmasking - Time = O(n * 2^n) - Space = O(n * 2^n)
    # If we need to generate all subsets, i.e. the result should have n^2 subsets then we can map presence/absense of the element to a bit
    # We'll count in 0 index
    # If nums = [1, 2], it'll have 4 or 2^2 or 1<<(2 - 1) combos
    # NOTE: In python 2^2 == 1<<1 NOT 1<<2
    # we can mask the presence/absence of the digits to a bitmask where i'th bit maps to i'th element
    # for [1, 2], rightmost bit maps to 1 and the one left to it maps to 2
    # (0) 00   =   []     (no bits set so empty array)
    # (1) 01   =   [1]    (only rightmost bit set so [1])
    # (2) 10   =   [2]    (and so on)
    # (3) 11   =   [1, 2]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], 2<<(len(nums) - 1)

        # Calculate and add the bitmasked subset for all numbers from 0 to 2**n - 1
        for i in range(n):
            res.append(self.bitmaskedSubset(i, nums))
        
        return res
    
    def bitmaskedSubset(self, i, nums):
        j, temp = 0, []

        while i > 0:
            # If rightmost bit is set append the corresponding element to temp
            if i & 1:
                temp.append(nums[j])
            
            # Increment j and rightshift i to look at the next corresponding element
            j += 1
            i >>= 1

        return temp


test = Solution()
# ans = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1, 2, 3]
print(test.subsetsBacktracking(nums))
