// link - https://leetcode.com/problems/first-bad-version/

class _278_First_Bad_Version {
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

    // Making a mock isBadVersion method to supress vscode warning
    public boolean isBadVersion(int mid) {
        return true;
    }
}