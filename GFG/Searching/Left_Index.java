class LeftIndex {
    static int leftIndex(int N, int arr[], int X) {
        int l = 0, r = N - 1, leftMost = -1;
        
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (arr[mid] == X) {
                if (leftMost == -1 || mid < leftMost)
                    leftMost = mid;
                r = mid - 1;
            } else if (arr[mid] < X) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return leftMost;
    }
}