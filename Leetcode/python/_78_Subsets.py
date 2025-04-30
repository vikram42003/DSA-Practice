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
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subset = [], []

        def helper(i):
            if i >= len(nums):
                subset.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i+1)

            curSet.pop()
            helper(i+1)
        helper(0)
        
        return subset


test = Solution()
# ans = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1, 2, 3]
print(test.subsetsBacktracking(nums))
