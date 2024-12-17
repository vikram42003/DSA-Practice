// link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

public class Two_Sum_II_Input_Array_Is_Sorted_167 {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        for (int i = 0; i < n; i++) {
            int required = target - numbers[i];
            if (required >= numbers[0] && required <= numbers[n - 1]) {
                int otherIndex = binarySearch(numbers, required);

                if (otherIndex == i) {
                    if (numbers[otherIndex + 1] == required) {
                        otherIndex++;
                    } else if (numbers[otherIndex - 1] == required) {
                        otherIndex--;
                    } else {
                        otherIndex = -1;
                    }
                }

                if (otherIndex != -1)
                    return new int[] { i + 1, otherIndex + 1 };
            }
        }
        return new int[] { -1, -1 };
    }

    public int binarySearch(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (numbers[mid] == target) {
                return mid;
            } else if (numbers[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
}
