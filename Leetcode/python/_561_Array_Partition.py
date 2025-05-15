from typing import List


class Solution:
    # We need to find pairs for which min(x, y) results to the greatest possible number

    # Now imagine nums is [1, 4, 3, 2]
    # We know for sure that nums will be of even length since we gotta find pairs and the
    # problem statement states so

    # Now for these elements - 1 4 3 2  If we include 1 into any pair then that pair
    # would result into 1 since theres no element smaller than 1 in nums

    # so in order to find the pair that result to the biggest sum, it needs to have the
    # biggest and the second biggest number, which may or may not be equal to biggest (since
    # number reprtition is allowed)

    # But how do we find the biggest and second biggest, well one approach would be to just
    # sort the array!

    # sorted num - [4, 3, 2, 1]

    # here the first pair is (4, 3) and the min of those is 3
    # but we already know that, since index 0 will be the biggest num and index 1 will be the
    # second biggest number, we can just directly take value at index 0

    # Now this algorithm is greedy so lets pretend that the pair (4, 3) has been eliminated
    # from the array and we're left with [2, 1]
    # here again the biggest will be at index 1

    # Can you see the pattern, despite needing to remove any pairs from the original array
    # the biggest num is the even index, and the second biggest (The num we'll actaully get
    # on doing min(biggest, second biggest)) is at odd indices
    # Using this to our advantage, we can just add all elements at the odd index
    # Also we can easily adapt it to ascending arrays by just starting from index 0

    # Sorting Approach - Time = O(n log n) - Space = O(1)
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total
