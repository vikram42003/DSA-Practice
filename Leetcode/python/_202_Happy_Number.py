class Solution:
    # Floyd's Cycle Detection - Time = O(log n) - Space = O(1)
    # Each number maps deterministically to the next, forming a functional graph. Since the values are bounded
    # the sequence must either reach 1 or enter a cycle, So Floyd's Cycle Detection works here
    def isHappy(self, n: int) -> bool:
        def next_n(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s

        slow = n
        fast = next_n(n)
        while fast != 1 and slow != fast:
            slow = next_n(slow)
            fast = next_n(next_n(fast))

        return fast == 1

    # Math or Something - Time = O() - Space = O(n)
    # All numbers will eventually be reduced to singe digit but some single digit number's square's will be
    # 2 digit so compare with n * n, and some numbers (like starting at 2) will keep looping infinitely
    # so record it in seen
    # Then in the end check if we broke the loop beacuse the number was in seen or if it was reduced to single
    # digit, and return n == 1 if latter
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n * n > 9 and n not in seen:
            seen.add(n)
            x = 0
            while n > 0:
                i = n % 10
                x += i * i
                n //= 10
            n = x

        if n in seen:
            return False
        else:
            return n == 1
