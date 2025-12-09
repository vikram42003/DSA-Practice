class Solution:
    # Bottom-Up DP (Fibonacci Optimization) - Time = O(n) - Space = O(1)
    
    # Intuition: The number of ways to reach step i, is dependent upon the number of ways we could
    # reach jump i - 1, and i - 2, and thats kinda the pattern of fibonacci series, we can memo the
    # common computations for n steps but since its fibinacci and we know we can only jump 1 or 2
    # steps, so we can optimize by removing dimension state
    def climbStairs(self, n: int) -> int:
        # prevprev is 2 step before curr step variable, or the jumps it'd take to get to step 0
        prevprev = 0
        # prev is the 1 step before curr step variable, or the jumps it'd take to get to step 1
        prev = 1
        # curr tracks the current step we're at, and its value is the number of jumps it took to
        #  get to 1 step before it and 2 steps before it

        # And we do that until we reach i'th step and + 1 time so that the nth value gets assigned
        # to prevprev and we can make it cleaner
        for i in range(n + 1):
            temp = prev
            prev += prevprev
            prevprev = temp

        return prevprev
