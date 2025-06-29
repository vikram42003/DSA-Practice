from typing import List


class Solution:
    # The basic idea is - start from left and keep a prefix sum we can get from left to current
    # index and store it in a hashmap. Also store the frequency of the prefix sum cause there are
    # negative values in the array so there might be more than one subarrays that can get us the
    # same sum - eg. in [2, -1, 1] both [2] and [2, -1, 1] would give us the sum of 2
    # After that just solve it like two sum!
    # From that I mean if nums = [1, 1, 1] and k = 2
    # imagine if we keep prefixing and now we are at index 2 and the prefix sum here is 3
    # that means its greater than 2, so how do we make it smaller, by excluding some values
    # 3 - k = 1, so we need to exclude any subarray that has the prefix sum of 1 from the array
    # We would have stored all the prefix sums for all the elements before this in the hashmap so
    # we can instantly know how many subarrays sum up to 1, So we can just add their value
    # Here in that example only [1] adds up to sum of 1, so we only to add 1 cause
    # current subarray will not give us 2 but if we exclude 1 another subarray from it which is
    # [1] then we'll get the answer (if there were 3 different subarrays that add up to 1 then
    # we'd add 3 to total)
    # Do that for each element and then we'll get our answer!
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        # We initialize prefixSums with 0 so that we dont have to handle the case curr == k separately
        prefixSums = {0: 1}

        for n in nums:
            curr += n
            diff = curr - k

            count += prefixSums.get(diff, 0)
            prefixSums[curr] = prefixSums.get(curr, 0) + 1

        return count
