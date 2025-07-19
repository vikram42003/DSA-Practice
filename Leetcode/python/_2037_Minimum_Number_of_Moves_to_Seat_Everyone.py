from typing import List


class Solution:
    # Sort and Diff - Time = O(n log n) - Space = O(n)
    # The value at seats[i] or students[i] is the actual position of the student or seat, so its
    # order in the array is meaningless. So we can just sort the lists and get 
    # abs(seats[i] - students[i]) to get the actual distance different between students. The leftmost
    # student should occupy the leftmost seat so that thr one at the right doesnt have to move extra
    # turns
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(a - b) for a, b in zip(seats, students))



# Working notes -
# Going over examples
# 1 3 5
# 2 4 7
# 1 1 2 = 4

# 1 4 5 9
# 1 2 3 6
# 0 2 2 3 = 7

# 2 2 6 6
# 1 2 3 6

