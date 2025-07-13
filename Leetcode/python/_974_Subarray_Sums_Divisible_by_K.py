from typing import List


class Solution:
    # Prefix Sum and HashMap - Time = O(n) - Space - O(n)
    # Intuition -
    #     We need to count the number of subarrays where sum(subarray) % k == 0
    #     the sum of subarray nums[i+1..j] is prefixSum[j] - prefixSum[i], and we track those prefixes in a dict/HashMap
    #     if (prefixSum_j - prefixSum_i) % k == 0    then subarray nums[i+1..j] is divisible by k.
    #     prefixSum[j] % k - prefixSum[i] % k == 0     ((a - b) % k = a % k - b % k)
    #     prefixSum[j] % k == prefixSum[i] % k         (moving prefixSum[i] % k to other side)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        cur = 0
        prefixSums = {0: 1}

        for n in nums:
            cur += n
            toExclude = cur % k

            count += prefixSums.get(toExclude, 0)
            prefixSums[toExclude] = 1 + prefixSums.get(toExclude, 0)
            
        return count
