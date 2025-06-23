from typing import List


class Solution:
    # Kadane Algo - Time = O(n) - Space = O(1)

    # The greatest subarray could be in the middle or the array like normal or circling
    # through the edges
    # If its circling then we can go and sum up from the boundaries but a better way to do it
    # is by looking at total - min subarray
    # Total contains all the element, the contiguos greatest subarray is just total but without
    # the elements that bring the total down
    # So if we eliminate the biggest contiguos group of elements that bring the total down then
    # we'll automatically have the biggest array!
    
    # Also keep note that there might be many distributed elements that bring the total down
    # But we need to keep the subarray contiguos, so we only eliminate the biggest "obstacle"
    # which is the minimim subarray
    
    # Also another thing to note is that if all elements of the array are negative then total
    # will be equal to minimum subarray and total - min subarray will give us the incorrect answer
    # 0, in that case we can just check if maximum subarray is negative, if it is then just return
    # that since that will contain the greatest element in the all negative array
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_max = nums[0]
        min_min = nums[0]
        total = 0
        cur_max = 0
        cur_min = 0

        for n in nums:
            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0

            cur_max += n
            cur_min += n
            max_max = max(max_max, cur_max)
            min_min = min(min_min, cur_min)

            total += n

        # If all numbers were negative therefore max_max is negative
        # Then just return max_max, since that will be the greatest element and the greatest
        # subarray in the array
        if max_max < 0:
            return max_max

        return max(max_max, total - min_min)


test = Solution()
# ans = 10
arr = [5, -3, 5]
