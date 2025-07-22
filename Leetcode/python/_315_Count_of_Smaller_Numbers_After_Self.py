from typing import List


class Solution:
    # Merge Sort Modified - Time = O(n log n) - Space = O(n)
    # Try Fenwick Tree when you come back
    def countSmaller(self, nums: List[int]) -> List[int]:
        numsPair = [(nums[i], i) for i in range(len(nums))]
        ans = [0] * len(nums)
        self.mergeSortModified(ans, numsPair, 0, len(nums) - 1)
        return ans

    def mergeSortModified(self, ans, numsPair, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSortModified(ans, numsPair, left, mid)
        self.mergeSortModified(ans, numsPair, mid + 1, right)
        self.merge(ans, numsPair, left, mid, right)

    def merge(self, ans, numsPair, left, mid, right):
        temp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if numsPair[i][0] > numsPair[j][0]:
                temp.append(numsPair[i])
                ans[numsPair[i][1]] += right - j + 1
                i += 1
            else:
                temp.append(numsPair[j])
                j += 1
                

        while i <= mid:
            temp.append(numsPair[i])
            i += 1
        while j <= right:
            temp.append(numsPair[j])
            j += 1

        for n in temp:
            numsPair[left] = n
            left += 1

test = Solution()
# ans = [2,1,1,0]
nums = [5,2,6,1]
print(test.countSmaller(nums))