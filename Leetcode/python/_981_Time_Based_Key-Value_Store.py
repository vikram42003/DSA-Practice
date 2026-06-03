from collections import defaultdict


class TimeMap:
    # Binary Search - Time = O(log n) - Space = O(n)
    # The problem statement states that the timestamps will be strictly increasing, so that part is sorted
    # We can just put the entries in a dict of lists
    # For looking for the last value smaller than or equal to the given timestamp, we can use a bisect template
    # binary search
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]

        if len(arr) == 0 or timestamp < arr[0][1]:
            return ""

        # With the template, we look for the first entry thats larger than timestamp, and then move 1 step back
        # to get last <= value to the given timestamp
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid][1] > timestamp:
                r = mid
            else:
                l = mid + 1

        return arr[l - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
