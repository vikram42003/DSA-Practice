from typing import List


class Solution:
    # Brute Force - Time = O(n^2) - Space = O(n)
    # Just linear search nums1[i] in nums2, and then move right until end or elem > nums1[i] is found
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in nums1:
            found = False
            num = -1

            for j in nums2:
                if i == j:
                    found = True
                elif found and j > i:
                    num = j
                    break

            res.append(num)

        return res

    # Monotonic Stack Approach - Time = O(m + n) - Space = O(3n)

    # Instead of calculating what first largest digit of nums2 comes after the current digit n by moving forward for each digit,
    # We see which digits were smaller than the current digit
    #
    # for nums1 = [2, 1, 3]    nums2 = [2, 1, 4, 3]
    # stack =        - In the beginning the list is empty so add 2 to the stack
    # stack = [2]    - now n = 1, check if n is greater than stack top (stack[-1]), if yes then thats the first digit larger than
    #                  2, otherwise add it to the stack. 1 is smaller than 2 so we add it to the stack
    # stack = [2, 1] - now n = 4, 4 is larger than stack[-1] so 4 is the first digit larger than 1, pop 1 from stack and repeat for
    #                  rest of the digits to check if theres more, which there is, so we pop again. Since 4 is not in nums1, we will
    #                  not add it to stack
    # stack = []     - now n = 3 but theres nothing in stack, just add it to stack (although adding last digit to stack does nothing)
    #
    # Now res is ready [4, 4, -1]

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {val: idx for idx, val in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                res[hash_map[stack.pop()]] = n

            if n in hash_map:
                stack.append(n)

        return res
