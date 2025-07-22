from typing import List


class Solution:
    # True Naive (Will TLE) - Simulation - Time = O(n^2) - Space = O(1)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if lower <= cur <= upper:
                    ans += 1

        return ans
    
    # Naive Solution (Will also TLE) - Time = O(n^2) - Space = O(n)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        ans = 0
        # i basically says, whats the subarray sum if we start from i in nums, and then include 1 digit after i, then 2 and so on
        # the loop calculates the sum from [0, j) - that means for nums = [-2,5,-1] and i = 0 j = 2, then were getting sum including
        # element 0 and right before element 2 - meaning from 0 to 1
        for i in range(len(nums)):
            # j basically sets the right bound of the window, including the element itself, then 1 another element after it, then the
            # next and so on. Also i starts from i + 1 cause we include an extra 0 to the prefix sum array to make calculations from
            # 0 to j more uniform
            for j in range(i + 1, len(prefixSums)):
                num = prefixSums[j] - prefixSums[i]
                print(num)
                if lower <= num <= upper:
                    ans += 1

        print(prefixSums)
        return -1
    
    # Prefix Sums, Merge Sort, Range Sum Approach - Time = (n log n) - Space = O(n)
    # Oh this one genuinely sucks, long explanation below...
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        ans = 0

        def magicalMergeSort(left, right):
            nonlocal ans
            if left >= right:
                return
            mid = left + (right - left) // 2
            magicalMergeSort(left, mid)
            magicalMergeSort(mid + 1, right)

            j = k = mid + 1
            for i in range(left, mid + 1):
                while j <= right and prefixSums[j] - prefixSums[i] < lower:
                    j += 1
                while k <= right and prefixSums[k] - prefixSums[i] <= upper:
                    k += 1
                ans += k - j
            magicalMerge(left, mid, right)
        
        def magicalMerge(left, mid, right):
            temp = []
            i, j = left, mid + 1

            while i <= mid and j <= right:
                if prefixSums[i] < prefixSums[j]:
                    temp.append(prefixSums[i])
                    i += 1
                else:
                    temp.append(prefixSums[j])
                    j += 1

            while i <= mid:
                temp.append(prefixSums[i])
                i += 1

            while j <= right:
                temp.append(prefixSums[j])
                j += 1
            
            for n in temp:
                prefixSums[left] = n
                left += 1

        magicalMergeSort(0, len(prefixSums) - 1)
        return ans
    
    # What we doin...
    # we have an array like this `nums = [-2,5,-1], lower = -2, upper = 2` and we need to find the count of subarrays where the sum 
    # lies between upper and lower. Simple Enough for a naive solution - just do an n^2 simulation, get all arrays and sum up those 
    # that lie between the bounds.
    
    # but thats not fast enough. From the keywords "sum" and "subarray" the idea of prefix sums comes up. So lets do that for now
    # prefixSums = [0, -2, 3, 2] (adding 0 at start for easy nums[j] - nums[i] calculations, so that we dont have to handle that with an if-else
    # case and so that it works with stuff like modified merge sort)
    # Now to get values for subarrays that say start from nums[1] to nums[2], we can just subtract the part right before nums[1]
    # so 2 - -2 = 4 (in original array 5 + -1 = 4)
    # but to get sum for all subarrays, its n^2 oeprations again and thats where merge sort comes in
    
    # what if we split the array and sort left half and right half
    # then both the halves will be sorted right, so next what if we take an element from the left as i and say what are the prefixSums
    # in the right half (aka the subarrys), that lie between the bounds if we exclude elements upto i
    
    # like if left = [1, 2, 3]    right = [3, 4, 5]    lower = 2    upper = 3
    # we look at i = 0 so left[0] = 1 and exclude it from right[0] getting 3 - 2 = 2, and that lies within the bounds so ans += 1
    # then left[0] = 1 and right[1] = 4 getting 4 - 3, does not lie within bounds so skip
    # same for right[2] and do that for each i and do ans += 1 for each valid value
    
    # But another thing to note is that the right array is sorted, so we dont need to iterate over each element, we just need to
    # find the first and last element that get us the valid answer and count all elements in between. This is exactly why we're 
    # merge sort
    # Also left array is sorted too, so we dont need to start looking for the first and last element from the beginning, just 
    # continue from where they previously were
    
    # For all this to work we do need to sort the array, so do that after count ans
    # Another optimization we can do is to conbine the counting and merge sort's merging, but im out of brain power so thats for 
    # another day


test = Solution()
# ans = 3
nums = [-2,5,-1]
lower = -2
upper = 2
print(test.countRangeSum(nums, lower, upper))