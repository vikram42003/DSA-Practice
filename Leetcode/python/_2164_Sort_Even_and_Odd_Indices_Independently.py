from typing import List


class Solution:
    # Bubble Sort - Time = O(n^2) - Space = O(1)
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(0, n, 2):
            swapped = False

            for i in range(n - 2 - j):
                if i & 1 == 0:
                    if nums[i] > nums[i + 2]:
                        nums[i], nums[i + 2] = nums[i + 2], nums[i]
                        swapped = True
                else:
                    if nums[i] < nums[i + 2]:
                        nums[i], nums[i + 2] = nums[i + 2], nums[i]
                        swapped = True

            if not swapped:
                break

        return nums
    
    # Concise and Quicker - Time = O(n log n) - Space = O(n)
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Get odd and even parts of the list
        odd, even = nums[1::2], nums[::2]
        # Sort and store the odd and even parts and overwrite
        odd, even = sorted(odd, reverse=True), sorted(even)
        # Assign the sorted odd and even lists to the odd and even parts of the array
        # (yes this shit is valid in python, you can even one line this problem with this concept)
        nums[1::2], nums[::2] = odd, even
        
        return nums
