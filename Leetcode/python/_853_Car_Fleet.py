from typing import List


class Solution:
    # Math - Time = O(n log n) - Space = O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prevTime = 0

        for p, s in pairs:
            t = (target - p) / s

            # If current car takes more time than prev time then it'll be its own fleet
            # otherwise if it takes less time than prev time it'll become part of the prev fleet
            # We iterate in sorted reverse order so we only need to track if current car can be
            # combined into its immediate previous fleet cause anything before that will already be
            # calculated by this point
            if t > prevTime:
                fleets += 1
                prevTime = t

        return fleets
    
    # Math + Stack - Time = O(n log n) - Space = O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First we need to zip up the positions and speeds and sort it in reverse
        # We sort in reverse because we start putting together fleets from the end, cause that will
        # give us the actual real time the cars ahead of the fleet will be travelling at, because a
        # faster cart at idx -2 might need to slow down to move with the fleet, so its real speed would
        # be reduced
        pairs = sorted(zip(position, speed), reverse=True)
        # Put the finalTime for the cars in a stack so we can combine cars in fleets while keeping separate fleets separate
        # The sorted order of our pairs ensures that a fleet deep in the stack wont be used again
        # otherwise the fleets on top would've merged into the lower one
        stack = []

        for p, s in pairs:
            # the time when this car would reach target
            finalTime = (target - p) / s
            # If theres nothing in stack or if this car reaches target slower than whats at the top of
            # the stack then we need to append it to stack to create its own separate fleet
            if not stack or finalTime > stack[-1]:
                stack.append(finalTime)

        return len(stack)
