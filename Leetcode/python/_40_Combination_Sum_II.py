from typing import List


class Solution:
    # Backtracking - Time = O(2 ^ n) - Space = O(n)
    # We first need to sort the array (this note assumes its non decreasing)
    # For each candidate starting at index i, either pick it (add to curr, rsum -= candidate) and recurse, or move to the next candidate in the loop.
    # Skip duplicates at the same depth: if j > i and candidates[j] == candidates[j-1]: continue.
    # When rsum == 0, append a copy of curr to res. Stop recursion if rsum < 0 or i goes out of bounds.
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr, n = [], [], len(candidates)
        candidates.sort()

        def rec(i, rsum):
            if rsum == 0:
                res.append(curr[:])
                return
            elif i >= n or rsum < 0:
                return

            c = candidates[i]

            curr.append(c)
            rec(i + 1, rsum - c)
            curr.pop()

            # Skip all duplicates
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            rec(i + 1, rsum)

        rec(0, target)

        return res
    
    # Same as abolve but uses a for loop
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr, n = [], [], len(candidates)
        candidates.sort()

        def rec(i, rsum):
            if rsum == 0:
                res.append(curr[:])
                return
            elif rsum < 0 or i >= n:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]: continue
                curr.append(candidates[j])
                rec(j + 1, rsum - candidates[j])
                curr.pop()

        rec(0, target)

        return res
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        res = []
        curr = []
        return self.rec(candidates, target, res, curr, 0)

    def rec(
        self,
        candidates: List[List[int]],
        target: int,
        res: List[List[int]],
        curr: List[int],
        idx: int,
    ) -> List[List[int]]:
        if target < 0:
            return
        if target == 0:
            res.append(curr.copy())
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]: continue
            curr.append(candidates[i])
            self.rec(candidates, target - candidates[i], res, curr, i + 1)
            curr.pop()

        return res


test = Solution()
# ans = [
#   [1,2,5],
#   [1,1,6],
#   [1,7],
#   [2,6]
# ]
candidates = [10,1,2,7,6,1,5]
target = 8
print(test.combinationSum2(candidates, target))