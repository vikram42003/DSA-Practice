class Solution {
    // Function to find equilibrium point in the array.
    public static int equilibriumPoint(int arr[]) {
        int[] prefix = new int[arr.length];
        int[] postfix = new int[arr.length];

        prefix[0] = arr[0];
        postfix[arr.length - 1] = arr[arr.length - 1];
        for (int l = 1, r = arr.length - 2; l < arr.length; l++, r--) {
            prefix[l] += prefix[l - 1] + arr[l];
            postfix[r] += postfix[r + 1] + arr[r];
        }

        for (int i = 0; i < arr.length; i++) {
            if (prefix[i] == postfix[i])
                return i + 1;
        }

        return -1;
    }
}