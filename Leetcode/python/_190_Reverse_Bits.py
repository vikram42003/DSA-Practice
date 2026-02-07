class Solution:
    # Output gotta be 32 digits long so we have to iterate 32 times, but as you can see output is just bits of
    # input but in reverse order, so just start filling the output from the leftside, we can do it in an array
    # and that would help us fill it intuitively but calculating the final ans would be a pain in the ass so
    # we just make a res variable, then left shift first, put the current LSB at current res's LSB, and then
    # iterate 32 times
    def reverseBits(self, n: int) -> int:
        res = 0
        # "For those who come after"
        for i in range(1, 33):
            res <<= 1
            res += n & 1
            n >>= 1
        return res
