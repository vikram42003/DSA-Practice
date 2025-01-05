package GFG.Searching;

class Majority_Element {
    static int majorityElement(int arr[]) {
        // Moore's Voting Algorithm

        // Find the majority candidate
        int majIndex = 0, count = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == arr[majIndex]) {
                count++;
            } else {
                count--;
            }

            if (count == 0) {
                majIndex = i;
                count = 1;
            }
        }

        // Confirm that the majority element indeed is the majority element
        count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == arr[majIndex])
                count++;
            if (count > arr.length / 2)
                return arr[majIndex];
        }

        return -1;
    }
}