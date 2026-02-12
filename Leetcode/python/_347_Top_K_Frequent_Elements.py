from typing import Counter, List


class Solution:
    # Buckets and Shii - Time = O(n) - Space = O(n)
    # To eliminate the sorting step and get the time complexity under O(n log n), we make buckets of arrays for all 
    # the possible frequencies of numbers (max would be freq equal to len(nums)), and then put each number by frequency
    # into its bucket, and now to get the top K, iterate over the buckets from the back, put it in res
    # return when len(res) == k
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted((c := Counter(nums)), key=c.get, reverse=True)[:k]
