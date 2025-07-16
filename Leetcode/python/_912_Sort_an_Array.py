from typing import List


class Solution:
    # Merge Sort - Time = O(n log n) - Space = O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            # Base Case
            if r - l == 1:
                return

            mid = l + (r - l) // 2

            # Sort left half
            mergeSort(l, mid)
            # Sort right half
            mergeSort(mid, r)
            # Merge the sorted halves
            merge(l, mid, r)

        def merge(l, mid, r):
            # Create a temp array for storing values
            temp = []

            # Iterate over both and get the minimum
            i, j = l, mid
            while i < mid and j < r:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            # Add values leftover in left half
            while i < mid:
                temp.append(nums[i])
                i += 1

            # Add values leftover in right half
            while j < r:
                temp.append(nums[j])
                j += 1

            # Overwrite nums with sorted values
            for n in temp:
                nums[l] = n
                l += 1

        mergeSort(0, len(nums))
        return nums
