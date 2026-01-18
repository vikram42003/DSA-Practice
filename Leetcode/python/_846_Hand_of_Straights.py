from typing import Counter, List


class Solution:
    # Greedy, Sorting and Tallying - Time = O(n log n) - Space = O(n)
    # First sort the cards, the group needs to have consecutive increasing cards so it makes sense to
    # sort it and look from the start. Then to prevent the n^2 loop of checking the whole pile if the
    # card next to i is not bigger than it, tally up the cards in a dict (we'll call it freq)
    # Then just itearte over the sorted cards, If the number of cards in freq of that value are
    # greater than 0 then that means it has not been used yet so we can look for a group starting from
    # this one, and mark this card used (by doing freq[card] -= 1)
    # So look for the next cards, if they're all unused then mark then as we use it, otherwise if we
    # find that a card is missing (freq[card + 1] <= 0) then immediately return False
    # Otherwise return true
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        freq = Counter(hand)

        for card in hand:
            if freq[card] > 0:
                freq[card] -= 1
                for i in range(1, groupSize):
                    if freq[card + i] <= 0:
                        return False
                    freq[card + i] -= 1

        return True
