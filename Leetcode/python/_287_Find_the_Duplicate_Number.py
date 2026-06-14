from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
    # The core idea is - Since the array elements will be in range [1, n], we can treat the graph as a linked list
    # Where val = idx and next = nums[idx]. With this, each node points to the next node, and the duplicates would
    # point to the same node, creating a cycle.
    #
    # Because 0 is not a valid value in the array, no node can ever point back to index 0. This makes index 0
    # a guaranteed entry point from outside the cycle, bypassing any self-referencing traps (like nums[1] = 1).
    #
    # Phase 1: Move 'slow' by 1 step and 'fast' by 2 steps until they intersect. This confirms a cycle exists
    # and locates a meeting point inside the loop.
    #
    # Phase 2: Reset 'slow' (or a new pointer) back to index 0 and keep 'fast' at the intersection point.
    # Move both pointers at a speed of 1 step. The mathematical distance from index 0 to the cycle entrance
    # is exactly equal to the distance from the intersection point to the cycle entrance, forcing them to
    # meet precisely at the duplicate number.
    
    # FLOYD'S CYCLE DETECTION VISUALIZATION & PROOF (P = X):
    # ----------------------------------------------------
    #
    #       (Start)
    #          0
    #          |
    #          v  [P Steps]
    #          1 <-------------------+  <- Cycle Entrance (Duplicate Number)
    #         / \                    |
    #        v   v                   |
    #       2     5 (Intersection)   |  <- Where slow & fast pointers met
    #        \   /                   |
    #         v v   [C - X Steps]    |  <- (Remaining loop distance)
    #          3 --------> 4 --------+
    #
    # DEFINITIONS:
    # P = Distance from index 0 to the cycle entrance (1).
    # C = Total length of the cycle loop (1 -> 2 -> 3 -> 4 -> 5 -> 1).
    # X = Distance from cycle entrance (1) to the first intersection point (5).
    # The remaining distance to complete the loop back to the entrance is (C - X).
    #
    # PROOF EQUATIONS:
    # slow_distance = P + (C - X)
    # fast_distance = P + C + (C - X)  [Fast travels an extra full cycle loop]
    #
    # Because fast moves exactly twice as fast as slow (2 * slow = fast):
    # 2 * (P + C - X) = P + 2C - X
    # 2P + 2C - 2X    = P + 2C - X
    #
    # Cancel out '2C' and simplify the algebra:
    # 2P - 2X = P - X
    # P = X
    #
    # CONCLUSION:
    # The distance from the array start to the cycle entry (P) is identical to 
    # the distance from the intersection point to the cycle entry (X). 
    # Resetting one pointer to 0 and moving both at 1x speed ensures they 
    # collide exactly at the cycle entrance (the duplicate number).
