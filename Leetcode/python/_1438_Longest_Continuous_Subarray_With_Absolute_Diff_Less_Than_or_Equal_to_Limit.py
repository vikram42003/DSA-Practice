from typing import List


class Solution:
    # Brute Force
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dist = 0
        for i in range(len(nums)):
            min_val = nums[i]
            max_val = nums[i]

            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])

                if abs(min_val - max_val) <= limit:
                    dist = max(dist, j - i)
                else:
                    break

        return dist + 1


test = Solution()
# ans = 2
arr = [8, 2, 4, 7]
limit = 4
print(test.longestSubarray(arr, limit))
