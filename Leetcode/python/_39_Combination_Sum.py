from typing import List


class Solution:
    # Backtracking - Time = (2 ^ n) - Space = O(n)
    # For each element, we have a choice whether to pick and and keep picking it again and again, or not pick it
    # So we do a greedy search where we track running sum in rsum and current elements picked in curr
    # For each element we either add it to curr and rsum and backtrack, or we dont add it and move over to next element and backtrack
    # If rsum == target then add it to res, or if rsum crosses target or i goes out of bounds, we just return
    # In the end return the final answer
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr, n = [], [], len(candidates)

        def rec(i, rsum):
            if rsum == 0:
                res.append(curr[:])
                return
            elif rsum < 0 or i >= n:
                return

            c = candidates[i]

            curr.append(c)
            rsum -= c
            rec(i, rsum)

            curr.pop()
            rsum += c
            rec(i + 1, rsum)

        rec(0, target)
        
        return res
    
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        candidates.sort()

        return self.rec(candidates, target, curr, ans, 0)

    def rec(
        self,
        candidates: List[int],
        target: int,
        curr: List[int],
        ans: List[List[int]],
        idx: int,
    ) -> List[List[int]]:
        # The current combination is invalid so just return
        if target < 0:
            return
        # The current combination is valid so add it to ans and then return
        if target == 0:
            ans.append(curr.copy())
            return

        # Go over each possible combination
        # start from first number in candidates, and then go deeper and deeper until `target < 0` or `target == 0` condition is reached
        # and then pop out the previous candidate and then recursively proceed with the next element (through i and idx moving forward)
        # we also ensure that we dont repeat previously considered combinations by starting the for loop from the idx index, since we'll have considered all previous elements by this point
        for i in range(idx, len(candidates)):
            curr.append(candidates[i])
            target -= candidates[i]
            self.rec(candidates, target, curr, ans, i)
            curr.pop()
            target += candidates[i]

        return ans


test = Solution()

# ans = [[2,2,3],[7]]
candidates = [2, 3, 6, 7]
target = 7
print(test.combinationSum(candidates, target))
