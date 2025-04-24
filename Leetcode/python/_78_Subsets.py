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
    def subsetsConcise(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [p + [i] for p in res]
        return res
    
    # def subsetsBacktracking(self, nums: List[List[int]]) -> List[List[int]]:
        


test = Solution()
# ans = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1, 2, 3]
print(test.subsets(nums))
