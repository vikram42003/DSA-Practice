// Input - int

// Constraints - 10^5 (within int range)
//             - cannot use a loop in solution

// Approach - optimized? S(O(n)) T(O(n))
//          - reduce the number untill <= 0 then increase it till n

// Output - list (of numbers to print)

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> pattern(int N) {
        // code here
        List<Integer> list = new ArrayList<>();
        recursivePattern(list, N);
        return list;
    }

    public void recursivePattern(List<Integer> list, int curr) {
        list.add(curr);
        if (curr <= 0)
            return;
        recursivePattern(list, curr - 5);
        list.add(curr);
    }
}