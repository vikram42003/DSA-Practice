// link - https://www.geeksforgeeks.org/problems/rotation4723/1

package GFG.Searching;

import java.util.List;

public class Find_Kth_Rotation {
    public int findKRotation(List<Integer> arr) {
        int l = 0, r = arr.size() - 1;
        while (l < r) {
            int mid = l + ((r - l) / 2);
            if (arr.get(mid) > arr.get(r)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}
