from typing import List


class Solution:
    # Greedy I guess - Time = O(n) - Space = O(1)
    # the only operation we have available to use is to convert alll elements of triplet A and B into a new
    # one which is the max of of A and B for each triplet within it. So that means, for whatever triplet we do pick
    # if any of its values is greater than target, then it would make it invalid. So just iterate through the array
    # find a triplet where its 0, 1 and 2 elements are equal to triplet and its all other values are either less than
    # or equal to target, then when we combine we'd get the resulting array
    
    # (Clean version)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False

        for x, y, z in triplets:
            a |= x == target[0] and y <= target[1] and z <= target[2]
            b |= x <= target[0] and y == target[1] and z <= target[2]
            c |= x <= target[0] and y <= target[1] and z == target[2]

            if a and b and c:
                return True
        
        return False
    
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        res = [False, False, False]

        for i in range(n):
            if (
                triplets[i][0] == target[0]
                and triplets[i][1] <= target[1]
                and triplets[i][2] <= target[2]
            ):
                res[0] = True
            if (
                triplets[i][1] == target[1]
                and triplets[i][0] <= target[0]
                and triplets[i][2] <= target[2]
            ):
                res[1] = True
            if (
                triplets[i][2] == target[2]
                and triplets[i][0] <= target[0]
                and triplets[i][1] <= target[1]
            ):
                res[2] = True

        return all(res)
