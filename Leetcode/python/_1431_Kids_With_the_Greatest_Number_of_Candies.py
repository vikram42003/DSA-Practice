# Input:
#     - we have n kids with candies in form of an array
#         - candies[n] - where candies[i] is the number of candies the ith kid has
#     - extraCandies - the extra candies that we have

# To Do:
#     - for each kid (taking as i), if candies[i] + extra candies >= greatestCandies

# Approach:
#     - find the max
#     - iterate over candies, add extra candies and see if it exceends max
#     - store results in a boolean array and return results

# Output:
#     - boolean array result (of length n)

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = []

        for candy_amount in candies:
            if candy_amount + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        
        return result
    
    # 2 line solution
    def kidsWithCandies2Line(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]