// link - https://leetcode.com/problems/first-bad-version/

class First_Bad_Version_278 {
    public int firstBadVersion(int n) {
        int l = 0, r = n, prevBad = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            boolean isBad = isBadVersion(mid);
            if (isBad) {
                r = mid - 1;
                prevBad = mid;
            } else {
                l = mid + 1;
            }
        }
        return prevBad;
    }
}