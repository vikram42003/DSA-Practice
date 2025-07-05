from typing import List


class Solution:
    # Linear Search - Time = O(n) - Space = O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        idx = 0
        num = 0
        while idx < len(arr) and k > 0:
            num += 1
            if num == arr[idx]:
                idx += 1
            else:
                k -= 1

        return num if k < 0 else num + k

    # Binary Search - Time = (n log n) - Space = O(1)
    # Working notes -
    ## [2,3,4,7,11]
    # l = 0   r = 4   mid = 0 + 4 // 2 = 2
    # mid = 2
    # 4 current number - 2 numbers present before four - 1 to exclude the four itself
    # = 1 number missing till 4 at index 2
    # we need to find the 5th number so look right

    # l = 3   r = 4   mid = 3 + 4 // 2 = 7 // 2 = 3
    # mid = 3
    # 7 - 3 - 1 = 3
    # 3 numbers missing till index 3 so look right

    # l = 4   r = 4   mid = 4 + 4 // 2 = 8 // 2 = 4
    # mid = 4
    # 11 - 4 - 1 = 6
    # 6 numbers missing, we need to find the 5th
    # 6th missing number will be the number before 11 which is 10, 5th missing is the number before that so 9
    # basically curNum - (6 - (k - 1)) = 11 - (6 - (5 - 1)) = 11 - (6 - 4) = 11 - 2 = 9
    # but wait, index 4 means there are 4 numbers before 11 taht are present, so to find whats not present, we can just do l + k = 4 + 5 = 9
    # 4 elements that are there and the 5th thats not there will give us the answer

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid - 1

        return l + k


test = Solution()
# ans = 9
arr = [2, 3, 4, 7, 11]
k = 5
print(test.findKthPositive(arr, k))
