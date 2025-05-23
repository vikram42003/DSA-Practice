# We start at "a", and we can move clockwise or counter clockwise to get to w in word
# total will be at least len(word) since it takes 1 sec to add the character
# We can instantly get the distance we need to travel by doing `w - curr`
# Yeah but what if curr is "c" and w is "a", then it would result to a negative number
# Well thats where the modulo comes in, it will always give us a positive number bw 0-25
# If ("a" - "c") is -2 then -2 % 26 will give us 24, think of it `right num - left num`
# But ("a" - "c") is just 2 movements, so ans should be 2 here but its 24 right now
# For that we'll do 26 - 24 to see how much we need to travel counter clockwise (("w" - "c")
# was negative) and just 24 (or rem) to see clockwise movement
# And then add the smaller of the two
# And update curr to be w
# Repeat for each character and return the result


class Solution:
    # Greedy - Time = O(n) - Space = O(1)
    def minTimeToType(self, word: str) -> int:
        curr = "a"
        total = len(word)
        for w in word:
            rem = (ord(w) - ord(curr)) % 26
            total += min(rem, 26 - rem)
            curr = w
        return total
