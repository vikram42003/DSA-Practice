from typing import List


class Solution:
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
