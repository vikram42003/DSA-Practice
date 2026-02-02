from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is less than 9, then increase it would never overflow, and we can increment and
            # return the answer here
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise digits[i] must be 9 and increasing it should make it 10, so current digit should be set
            # to 0 and we should look at the digit to its left to add another +1
            digits[i] = 0

        # If we didint return already till now then that means this is a case where even the 0th idx digit overflowed
        return [1] + digits

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                digits[i] += 1
                if digits[i] > 9:
                    digits[i] %= 10
                else:
                    carry = 0
            else:
                break

        return [1] + digits if carry else digits
