from typing import List


class Solution:
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