import random
from typing import List


# Randomized Quick Sort - Lomuto Partition Scheme
# Time = O(n log n) - Space = O(1) (Rec Stack Space Inclusive = O(n))
def sortArray(nums: List[int]) -> List[int]:
    quickSort(nums, 0, len(nums) - 1)
    return nums


def quickSort(nums, left, right):
    if left >= right:
        return
    rand_idx = random.randint(left, right)
    nums[rand_idx], nums[right] = nums[right], nums[rand_idx]

    partition_idx = partition(nums, left, right)
    quickSort(nums, left, partition_idx - 1)
    quickSort(nums, partition_idx + 1, right)


def partition(nums, left, right):
    pivot = nums[right]
    i = left

    for j in range(left, right):
        if nums[j] <= pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1

    nums[i], nums[right] = nums[right], nums[i]
    return i
