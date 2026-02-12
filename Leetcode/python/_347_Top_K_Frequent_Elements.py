from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted((c := Counter(nums)), key=c.get, reverse=True)[:k]
