from typing import List


# We use recursion here
# How many permutations does [1] have? its just [[1]] right
# So how many permutations does [1, 2] have?
#   - total size of the output will be 2 so we have 2 possible positions for 1 and 2 each
#   - actually we already know the permutations for 1 (which is [1]), so lets just add 2 at each of its possible positions
#   - that will give us [[1, 2], [2, 1]]
# okay so now how many permutations does [1, 2, 3] have?
#   - total possible positions are 3, so for each of the permutations of [1, 2], add 3 at each position
#   - [[1, 2], [2, 1]] - so thats 3 at the start, mid and end for [1, 2] and [2, 1] each
#   - that will give us [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# and so on, follow this pattern, put the new element at each possible position for each possible permutation for a smaller permutation


class Solution:
    # Neetcode version - Time = O(n! * n^2) - Space = O(n! * n)
    def permuteNC(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permuteNC(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                copy = p.copy()
                copy.insert(i, nums[0])
                res.append(copy)

        return res

    # LeetcodeTheHardWay version - Time = O(n! * n) - Space = O(n! * n)
    # here, instead of us changing where we insert the new element, we rotate the input array instead, so that
    # we can get new combinations each time
    # NOTE - for some reason this one is a bit slower than the neetcode version???
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            # we can modify nums here, the value for len(nums) will remain fixed as the value of nums when the loop first started
            saved_num = nums.pop(0)
            permutations = self.permute(nums)

            for perm in permutations:
                perm.append(saved_num)
                res.append(perm)

            nums.append(saved_num)

        return res

    # Iterative version - Time = O(n! * n^2) - Space = O(n! * n)
    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            new_perms = []
            for p in res:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, num)
                    new_perms.append(copy)
            res = new_perms

        return res


test = Solution()
# ans = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2], [1, 3, 2]]
print(test.permuteIterative([1, 2, 3]))
# ans = [
#     [5, 4, 6, 2],
#     [5, 4, 2, 6],
#     [5, 6, 4, 2],
#     [5, 6, 2, 4],
#     [5, 2, 4, 6],
#     [5, 2, 6, 4],
#     [4, 5, 6, 2],
#     [4, 5, 2, 6],
#     [4, 6, 5, 2],
#     [4, 6, 2, 5],
#     [4, 2, 5, 6],
#     [4, 2, 6, 5],
#     [6, 5, 4, 2],
#     [6, 5, 2, 4],
#     [6, 4, 5, 2],
#     [6, 4, 2, 5],
#     [6, 2, 5, 4],
#     [6, 2, 4, 5],
#     [2, 5, 4, 6],
#     [2, 5, 6, 4],
#     [2, 4, 5, 6],
#     [2, 4, 6, 5],
#     [2, 6, 5, 4],
#     [2, 6, 4, 5],
# ]
print(test.permuteIterative([5, 4, 6, 2]))
