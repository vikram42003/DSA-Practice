from collections import deque
import heapq
from typing import Counter, List


class Solution:
    # Dicts, MaxHeap and DQ - Time = O(n * log k) - Space - O(n)

    # We first count the number of occurences of each letter with a dict (using inbuilt python func)
    # Then we take only the count of values and heapify it, because we need to wait n time before doing the same task again so we start by the
    # max occuring task so that we can fit as many small tasks in between as we need

    # Then we go through the top task, decrement it to mark completion, and add it to a queue as [count, time we can do it again] at the end of the queue
    # if the current time is 1 and n is 3 and we're doing task "A" which has a count of 5, we'll reduce it to 4 and increase current time to 2, and the
    # next time we can do it again is 2 + 3 = 5, so we'll add (4, 5) to the queue

    # Because of this, at each step, we'll also check if there is any task that shoud re enter the heap and pop the top of queue if true
    # Do this until both heap and queue are empty and return the result
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap = Counter(tasks)

        heap = [-v for v in countMap.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                # We add 1 to reduce its value cause we're using negative values in the max heap
                top = 1 + heapq.heappop(heap)
                if top != 0:
                    q.append((top, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time
    
    # (Attempted but didnt work, I thought of a better way to solve it, but this approach may be worth considering if fixed)
    # HashMap - Time = O(n) - Space = O(n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        for t in tasks:
            mp[t] = mp.get(t, 0) + 1

        count = 0
        cd = 0

        while mp:
            # If the cooldown is greater than 0 then we wait for remaining cd time
            if cd > 0:
                count += cd
            cd = n + 1

            toDel = []

            for key in mp:
                count += 1
                mp[key] -= 1
                cd -= 1

                if mp[key] <= 0:
                    toDel.append(key)

            for key in toDel:
                del mp[key]

        return count
