// link - https://www.naukri.com/code360/problems/minimise-max-distance_7541449

import java.util.PriorityQueue;

class Minimize_Max_Distance_To_Gas_Stations {

    public static double MinimiseMaxDistance(int[] arr, int K) {
        // Binary Search Solution - Time = O(n log n) - Space = O(1)
        double l = 0, r = 0;
        for (int i = 0; i < arr.length - 1; i++) {
            r = Math.max(arr[i + 1] - arr[i], r);
        }

        while (r - l > 1e-6) {
            double mid = l + ((r - l) / 2.0);

            if (check(mid, arr, K)) {
                r = mid;
            } else {
                l = mid;
            }
        }

        return r;
    }

    public static boolean check(double mid, int[] arr, int K) {
        for (int i = 0; i < arr.length - 1; i++) {
            double dist = arr[i + 1] - arr[i];
            int placed = (int) (dist / mid);
            if (dist % mid == 0)
                placed--;
            K -= placed;
        }
        return K >= 0;
    }

    public static class Pair {
        double key;
        int value;

        Pair(double key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public static double MinimiseMaxDistancePQ(int[] arr, int K) {
        // Priority Queue Solution - Time = O(n log n) - Space = O(n)
        int[] placed = new int[arr.length - 1];

        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> Double.compare(b.key, a.key));
        for (int i = 0; i < arr.length - 1; i++) {
            pq.add(new Pair(arr[i + 1] - arr[i], i));
        }

        for (int i = 0; i < K; i++) {
            int idx = pq.poll().value;
            placed[idx]++;
            double dist = arr[idx + 1] - arr[idx];
            dist /= placed[idx] + 1;
            pq.add(new Pair(dist, idx));
        }

        return pq.poll().key;
    }

    public static double MinimiseMaxDistanceNaive(int[] arr, int K) {
        // Naive Solution - Time = O(n^2) - Space = O(n)
        int[] placed = new int[arr.length - 1];

        for (int i = 0; i < K; i++) {
            double max = -1;
            int idx = -1;

            for (int j = 0; j < arr.length - 1; j++) {
                double dist = arr[j + 1] - arr[j];
                dist /= placed[j] + 1;

                if (dist >= max) {
                    max = dist;
                    idx = j;
                }
            }

            placed[idx]++;
        }

        double ans = -1;
        for (int i = 0; i < arr.length - 1; i++) {
            double dist = arr[i + 1] - arr[i];
            dist /= placed[i] + 1;
            ans = Math.max(ans, dist);
        }

        return ans;
    }
}