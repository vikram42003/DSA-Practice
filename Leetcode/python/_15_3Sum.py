class Solution:
    # Two Pointers and Sorting - Time = O(n log n) + O(n^2) = O(n^2) - Space = O(n)
    # The core idea is - First we sort the list, now that the list is sorted we can set an anchor
    # num (the first num) through a normal for loop, and within that loop we can do a two pointer
    # search from the bounds to center, and increase/decrease left/right pointers to get our sum
    # value to 0
    # And be sure to skip any duplicates, for i, and for l and r when we find a valid res value
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the list to ensure no duplicate adding to res and for efficiency for two pointers
        nums.sort()
        n, res = len(nums), []

        for i in range(n - 2):
            # i will be the anchor, it'll be the first num we set
            # if i is same as prev then we'll end up finding a duplicate res value, so skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Make them move until they're no longer on duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
