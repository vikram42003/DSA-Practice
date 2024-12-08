class Solution {
    int floorSqrt(int n) {
        int l = 0, r = n;
        int closest = -1;

        while (l <= r) {
            int mid = l + ((r - l) / 2);
            int sq = mid * mid;
            if (sq == n) {
                return mid;
            } else if (sq < n) {
                l = mid + 1;
                if (closest == -1 || closest < mid)
                    closest = mid;
            } else {
                r = mid - 1;
            }
        }

        return closest;
    }
}