import java.util.HashMap;

class Solution {
    // Function to find all elements in array that appear more than n/k times.
    public int countOccurence(int[] arr, int k) {
        // HashMap Approach
        double nk = 1.0 * arr.length / k;

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i : arr) {
            hashMap.put(i, hashMap.getOrDefault(i, 0) + 1);
        }

        int total = 0;
        for (int i : hashMap.keySet()) {
            if (hashMap.get(i) > nk)
                total++;
        }

        return total;
    }
}